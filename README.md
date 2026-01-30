# Sales & Revenue Analysis

## Why I did this project
While looking at retail sales data, I noticed that high sales numbers don’t always mean high profit.  
This project started from a simple question: **where exactly is the company losing money despite selling more?**

I wanted to answer that using actual data instead of assumptions.

---

## What problem I tried to solve
The main problem was understanding:
- which regions and product categories actually make money
- which products look successful but consistently lose profit
- how discounting affects profit over time

Most sample projects stop at charts. I wanted to go one step further and extract decisions from the data.

---

## How I approached it
1. Cleaned the raw sales data using Python (date fixes, duplicates, feature creation)
2. Created new fields like year, month, and profit margin to make trend analysis possible
3. Loaded the cleaned data into a SQLite database to run business-style SQL queries
4. Used SQL to analyze monthly trends, region-wise performance, and loss-making categories
5. Built a Power BI dashboard to make the insights easy to understand visually

I intentionally separated cleaning (Python) and analysis (SQL) to mirror how data flows in real teams.

---

## What surprised me
A few things stood out during the analysis:
- Some regions showed increasing sales but declining profit over time
- A few sub-categories were loss-making almost every month, even with decent sales volume
- Higher discounts often increased sales but did not always compensate for profit loss

These patterns were not obvious until the data was grouped and analyzed properly.

---

## Key insights
- Profit trends do not always follow sales trends
- Certain categories consistently reduce overall profitability
- Discounting needs tighter control, especially for low-margin products
- A small percentage of customers contribute a large share of total revenue

---

## Tools I used
- Python (pandas) for data cleaning and feature engineering
- SQL (SQLite) for structured analysis
- Power BI for visualization and dashboarding
- GitHub for version control

---

## Dashboard preview
![Dashboard](powerbi/dashboard.png)

---

## What I would improve next
If I extend this project, I would:
- add cost-based analysis to better explain profit drops
- compare performance before and after discount changes
- automate monthly reporting instead of static analysis