# 📊 Task 7: Basic Sales Summary Using SQLite and Python

## 🎯 Objective
Analyze a small pizza sales dataset stored in an SQLite database using SQL inside Python. The goal is to pull basic sales insights like total quantity sold, revenue, and popular pizza sizes, and visualize them using bar charts.

---

## 🧰 Tools Used
- **Python**
- **SQLite** (built-in)
- **Pandas** (for data manipulation)
- **Matplotlib** (for visualization)
- **Jupyter Notebook**

---

## 🗂 Dataset
Dataset source: [Pizza Sales Dataset](https://www.kaggle.com/code/melikedilekci/eda-pizza-restaurant-sales/input)

The SQLite database `Pizza_Sales.db` contains one table:

- `sales` – with columns like:
  - `order_id`
  - `pizza_id`
  - `pizza_category`
  - `pizza_size`
  - `quantity`
  - `total_price`
  - `order_time`

---

## 🛠️ Setup Steps
1. **Create the database**  
   - Run `create_db.py` to generate `Pizza_Sales.db` from `Pizza_Sales.xlsx`

2. **Run analysis**  
   - Open and execute `task7.ipynb` to perform analysis and generate charts

---

## 🔍 Queries Performed

- Total quantity and revenue by pizza category  
- Average order price by pizza category  
- Total quantity sold by pizza size  

---

## 📊 Visualizations

- ✅ **Bar Chart** of Revenue by Pizza Category  
- ✅ **Bar Chart** of Quantity by Pizza Category  
- ✅ **Bar Chart** of Quantity Sold by Pizza Size  

Each chart helps identify sales trends and popular product segments in the pizza menu.

---

## 👨‍💻 Author
**Purnakam Shrivastava**  
Data Analyst
