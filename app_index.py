from flask import Flask, render_template, request, jsonify
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="zomato_db",
        port=3306
    )

# ---------------------------
# HOME
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------
# PLACE ORDER
# ---------------------------
@app.route("/place_order", methods=["POST"])
def place_order():
    try:
        data = request.get_json()
        cart = data.get("cart")
        address = data.get("address")

        if not cart or not address:
            return jsonify({"error": "Missing cart or address"}), 400

        connection = create_connection()
        cursor = connection.cursor()

        user_id = 1

        cursor.execute(
            "INSERT INTO orders (user_id, delivery_address) VALUES (%s, %s)",
            (user_id, address)
        )

        order_id = cursor.lastrowid

        for item in cart:
            cursor.execute(
                """
                INSERT INTO order_items (order_id, item_id, quantity)
                VALUES (%s, %s, %s)
                """,
                (order_id, item["item_id"], item["quantity"])
            )

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Order placed successfully",
            "order_id": order_id
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------
# ANALYTICS - TOTAL REVENUE
# ---------------------------
@app.route("/analytics/revenue")
def total_revenue():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT SUM(mi.price * oi.quantity) AS total_revenue
    FROM order_items oi
    JOIN menu_items mi ON oi.item_id = mi.id
    """

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    print(result)
    return jsonify(result)

# ---------------------------
# ANALYTICS - TOP ITEM
# ---------------------------
@app.route("/analytics/top-item")
def top_item():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT mi.item_name, SUM(oi.quantity) AS total_quantity
    FROM order_items oi
    JOIN menu_items mi ON oi.item_id = mi.id
    GROUP BY mi.item_name
    ORDER BY total_quantity DESC
    LIMIT 1
    """

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    print(result)
    return jsonify(result)

# ---------------------------
# ANALYTICS - DAILY REVENUE (PANDAS)
# ---------------------------
@app.route("/analytics/daily-revenue")
def daily_revenue():
    connection = create_connection()

    query = """
    SELECT o.order_date, mi.price, oi.quantity
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN menu_items mi ON oi.item_id = mi.id
    """

    df = pd.read_sql(query, connection)
    if df.empty:
        return jsonify({"message": "No data available"})

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["date"] = df["order_date"].dt.date
    df["revenue"] = df["price"] * df["quantity"]

    daily = df.groupby("date")["revenue"].sum().reset_index()

    connection.close()

    return daily.to_json(orient="records")

# ---------------------------
# ANALYTICS - VISUALIZATION
# ---------------------------
@app.route("/analytics/plot-revenue")
def plot_revenue():
    connection = create_connection()

    query = """
    SELECT o.order_date, mi.price, oi.quantity
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN menu_items mi ON oi.item_id = mi.id
    """

    df = pd.read_sql(query, connection)

    if df.empty:
        return "No data available"

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["date"] = df["order_date"].dt.date
    df["revenue"] = df["price"] * df["quantity"]

    daily = df.groupby("date")["revenue"].sum()

    plt.figure()
    daily.plot()
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode() # encodes img to txt

    connection.close()

    return f"<img src='data:image/png;base64,{plot_url}'/>"

# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
