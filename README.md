# 🍽 Zomato Analytics Pro

A full-stack Food Ordering & Analytics Web Application built using Flask, MySQL, Pandas, and Matplotlib.

This project simulates a mini Zomato-style food ordering system with a built-in analytics dashboard to analyze revenue, top-selling items, and daily revenue trends.

---

## 🚀 Features

### 🛒 Food Ordering System
- Add items to cart
- Dynamic cart updates (JavaScript)
- Place order with delivery address
- Orders stored in MySQL database
- Relational order & order_items mapping

### 📊 Analytics Dashboard
- ✅ Total Revenue Calculation (SQL Aggregation)
- ✅ Top Ordered Item (GROUP BY + ORDER BY)
- ✅ Daily Revenue (Pandas Data Processing)
- ✅ Revenue Trend Visualization (Matplotlib Chart)
- ✅ JSON API endpoints

---

## 🛠 Tech Stack

### Backend
- Python 3
- Flask
- MySQL
- mysql-connector-python

### Data & Analytics
- Pandas
- Matplotlib

### Frontend
- HTML5
- CSS3 (Modern UI Styling)
- JavaScript (Cart & API calls)
- Font Awesome Icons

---

## 📂 Project Structure

```
Zomato_data_analysis/
│
├── app_index.py              # Flask backend application
├── data_sql.sql              # Database schema and sample data
├── order_of_execution.txt    # Execution flow notes
├── templates/
│   └── index.html            # Frontend UI
├── static/
│   └── images/               # Food images
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🗄 Database Schema

The project uses a relational MySQL database with:

- users
- menu_items
- orders
- order_items

Relationships:
- One user → Many orders
- One order → Many order_items
- One menu_item → Many order_items

Key SQL Concepts Used:
- JOIN
- GROUP BY
- ORDER BY
- Aggregate Functions (SUM)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/zomato-analytics-pro.git
cd zomato-analytics-pro
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup MySQL Database

- Open MySQL
- Run the SQL script inside `data_sql.sql`

It will:
- Create database `zomato_db`
- Create tables
- Insert sample data

Make sure your MySQL credentials in `app_index.py` match:

```python
host="localhost"
user="root"
password="root"
database="zomato_db"
```

---

### 4️⃣ Run Application

```bash
python app_index.py
```

Visit:

```
http://127.0.0.1:5000/
```

---

## 📊 API Endpoints

| Endpoint | Description |
|----------|------------|
| `/` | Home page |
| `/place_order` | Place new order |
| `/analytics/revenue` | Get total revenue |
| `/analytics/top-item` | Get most ordered item |
| `/analytics/daily-revenue` | Daily revenue JSON |
| `/analytics/plot-revenue` | Revenue trend chart |

---

## 📈 Example Analytics Output

- Total revenue calculation using SQL JOIN
- Daily revenue grouped using Pandas
- Revenue trend plotted using Matplotlib

---

## 🔮 Future Improvements

- User authentication system
- Admin dashboard
- REST API documentation (Swagger)
- Deployment to Render / Railway
- Docker containerization
- Payment gateway integration
- JWT-based authentication
- Production-ready configuration using environment variables

---

## 🧠 Concepts Demonstrated

- Relational database modeling
- Backend API development
- Server-client architecture
- Data aggregation queries
- Data visualization
- REST endpoint design
- Full-stack integration

---

## 👨‍💻 Author

Paul  
Aspiring SaaS & Data-Focused Backend Developer  
