# 🛒 ShopSphere Analytics

## Enterprise E-Commerce Analytics Platform

ShopSphere Analytics is an end-to-end e-commerce analytics project that simulates a real-world online retail business. The project focuses on building an enterprise-scale analytical data platform using **Python**, **SQL Server**, **Power BI**, and **Excel**.

Instead of relying on publicly available datasets, this project generates realistic synthetic data from scratch using modular Python generators, applies business rules and validation, loads the data into SQL Server, and prepares it for advanced analytics and interactive dashboards.

---

# 🎯 Project Objectives

* Build a production-inspired e-commerce data warehouse
* Generate realistic enterprise-scale datasets
* Practice SQL using real business scenarios
* Develop modular Python ETL pipelines
* Create interactive Power BI dashboards
* Perform advanced business analytics
* Showcase an end-to-end Data Analyst portfolio project

---

# 🏗️ Project Architecture

```text
Reference Data
        │
        ▼
Master Data
        │
        ▼
Orders (Stage)
        │
        ▼
Order Items
        │
        ▼
Order Coupons
        │
        ▼
Financial Processing
        │
        ▼
Payments
        │
        ▼
Shipments
        │
        ▼
Returns
        │
        ▼
Reviews
        │
        ▼
Support Tickets
        │
        ▼
Website Traffic
```

---

# 📁 Project Structure

```text
ShopSphere-Analytics
│
├── config/
│
├── output/
│   └── csv/
│
├── src/
│   ├── generators/
│   │   ├── reference/
│   │   ├── master/
│   │   └── transactional/
│   │
│   ├── processors/
│   │
│   └── utils/
│
├── sql/
│
├── dashboards/
│
├── notebooks/
│
├── docs/
│
└── README.md
```

---

# 🛠️ Technology Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Data Generation & ETL     |
| Pandas     | Data Processing           |
| Faker      | Synthetic Data Generation |
| SQL Server | Database                  |
| SQL        | Data Analysis             |
| Power BI   | Business Intelligence     |
| Excel      | Data Validation           |
| Git        | Version Control           |
| GitHub     | Portfolio & Collaboration |

---

# 📊 Current Dataset

| Table          |          Records |
| -------------- | ---------------: |
| Products       |          300,000 |
| Customers      |          100,000 |
| Orders (Stage) |        1,000,000 |
| Inventory      | Enterprise Scale |

---

# ✅ Completed Modules

## Reference Tables

* ✔ States
* ✔ Cities
* ✔ Categories
* ✔ SubCategories
* ✔ Brands
* ✔ Suppliers
* ✔ Warehouses
* ✔ Payment Methods
* ✔ Couriers
* ✔ Return Reasons
* ✔ Support Issues
* ✔ Festival Calendar
* ✔ Calendar

---

## Master Tables

* ✔ Products
* ✔ Customers
* ✔ Customer Addresses
* ✔ Inventory
* ✔ Coupons

---

## Transaction Tables

* ✔ Orders (Stage)

---

# 🚧 Work In Progress

* ⏳ Order Items
* ⏳ Order Coupons
* ⏳ Financial Processing
* ⏳ Payments
* ⏳ Shipments
* ⏳ Returns
* ⏳ Reviews
* ⏳ Support Tickets
* ⏳ Website Traffic

---

# ✨ Key Features

* Enterprise-scale synthetic data generation
* Modular Python architecture
* Business rule implementation
* Referential integrity
* Data validation framework
* Progress logging
* SQL Server-ready datasets
* Production-inspired ETL workflow
* Power BI-ready data model

---

# 📈 Planned Analytics

This project will support business analysis such as:

* Sales Performance
* Revenue Analysis
* Customer Analytics
* Product Performance
* Category Analysis
* Brand Analysis
* Inventory Monitoring
* Customer Lifetime Value (CLV)
* Repeat Purchase Analysis
* RFM Analysis
* Coupon Performance
* Return Analysis
* Delivery Performance
* Executive KPI Reporting

---

# 📊 Planned Dashboards

* Executive Dashboard
* Sales Dashboard
* Customer Dashboard
* Inventory Dashboard
* Product Dashboard
* Marketing Dashboard
* Logistics Dashboard
* Returns Dashboard

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/<your-username>/ShopSphere-Analytics.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run a Generator

Example:

```bash
python -m src.generators.master.product_generator
```

Generate Orders:

```bash
python -m src.generators.transactional.orders_generator
```

---

# 📅 Project Roadmap

* ✅ Reference Data Generation
* ✅ Master Data Generation
* ✅ Orders Stage Generation
* ⏳ Order Item Generation
* ⏳ Order Coupon Generation
* ⏳ Financial Processing Pipeline
* ⏳ SQL Server Data Warehouse
* ⏳ Advanced SQL Analytics
* ⏳ Power BI Dashboards
* ⏳ Python Exploratory Data Analysis
* ⏳ Portfolio Documentation

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is intended for educational, learning, and portfolio purposes.

---

# 👨‍💻 Author

**Prasanta Kumar Deb**

Aspiring Data Analyst

### Skills

* SQL
* Python
* Power BI
* Excel
* Data Analytics
* ETL Development
* Business Intelligence

---

## ⭐ Support

If you find this project useful or interesting, please consider giving the repository a ⭐ on GitHub.
