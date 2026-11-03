# Customer Shopping Behavior Analysis

End-to-end analysis of 3,900 retail transactions to uncover spending patterns, customer segments, product preferences, and subscription behavior, turning raw data into actionable business recommendations.

**Tech stack:** Python (pandas) · PostgreSQL · SQL · Power BI

---

## Dataset

| Item | Detail |
|---|---|
| Rows / Columns | 3,900 / 18 |
| Customer demographics | Age, Gender, Location, Subscription Status |
| Purchase details | Item, Category, Purchase Amount, Season, Size, Color |
| Shopping behavior | Discount Applied, Promo Code Used, Previous Purchases, Purchase Frequency, Review Rating, Shipping Type |
| Data quality issue | 37 missing values in `Review Rating` |

---

## Workflow

**1. Data Preparation (Python)**
- Loaded the data with pandas and profiled it using `df.info()` and `.describe()`
- Imputed missing `Review Rating` values with the median rating of each product category
- Standardized column names to snake_case
- Engineered features: `age_group` (age binning) and `purchase_frequency_days`
- Dropped the redundant `promo_code_used` column after confirming it duplicated `discount_applied`
- Loaded the cleaned data into PostgreSQL for analysis

**2. Business Analysis (SQL)**
Answered 10 business questions, including:
- Revenue by gender and by age group
- High-spending customers who still used discounts
- Top 5 products by average rating and top 3 products per category
- Standard vs. Express shipping: average purchase amount
- Subscribers vs. non-subscribers: average spend and total revenue
- Products most dependent on discounts
- Customer segmentation: New, Returning, and Loyal
- Whether repeat buyers (>5 purchases) are more likely to subscribe

**3. Dashboard (Power BI)**
Built an interactive dashboard to present the findings visually for stakeholders.

---

## Business Recommendations

- **Boost subscriptions:** promote exclusive subscriber benefits
- **Loyalty programs:** reward repeat buyers to move them into the "Loyal" segment
- **Review discount policy:** balance sales lift against margin control
- **Product positioning:** feature top-rated and best-selling products in campaigns
- **Targeted marketing:** focus on high-revenue age groups and express-shipping users

---

## Skills Demonstrated

Data cleaning · Feature engineering · Python-to-PostgreSQL integration · Advanced SQL · Customer segmentation · Dashboarding · Translating data into business recommendations

---

## Author

**Faizan Riaz** · riazfaizan237@gmail.com
