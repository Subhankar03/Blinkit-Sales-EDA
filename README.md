# Blinkit Sales Analysis

## Project Overview

This project presents an in-depth exploratory data analysis (EDA) of customer behavior and sales performance from a simulated dataset of **Blinkit**, a rapid grocery delivery service. The primary aim is to uncover patterns in customer behavior, product demand, order timings, and delivery outcomes, and to visualize these insights for business understanding and strategic decision-making.

The analysis was conducted using **Python** in a **Jupyter Notebook** environment.

## Objective

* Analyze the ordering and purchasing patterns of Blinkit customers

* Identify high-performing cities, top customers, and popular products

* Discover sales patterns and trends across different categories and timeframes

* Examine order timing patterns throughout the day and week

* Segment customers using clustering techniques for targeted marketing

## Methodology

* Loaded and cleaned three datasets: **Customers**, **Orders**, and **OrderDetails**.

* Created new features like `Amount`, `Delivery Duration`, `Order Hour`, and `Order Weekday`.

* Conducted univariate and bivariate analysis.

* Standardized the data using **z-score normalization**.

* Applied **K-Means clustering** on aggregated customer metrics (spending, number of orders).

* Visualized clusters to understand customer behavior segments.

## Key Visualizations

* Pie chart showing proportion of orders delivered vs canceled

* Bar chart showing order count by city

* Word cloud showing most active customers

* Pie chart showing customer spending: Android vs iOS

* Scatter plot showing customer segments

* Word cloud showing best-selling products

* Bar chart showing Most popular products by city

* Bar chart showing order count by hour of the day and day of the week

## Key Takeaways

* Majority of the orders are successfully delivered; a small percentage are canceled.

* Certain cities contribute significantly more to total orders.

* A handful of customers are highly active and influential.

* iOS users tend to spend slightly more per order compared to Android users.

* Some products show strong regional popularity.

* Customer segmentation enables more effective targeting of high-value users. 

## Conclusion

This project demonstrates the value of exploratory data analysis in understanding customer behavior, optimizing operations, and identifying opportunities for growth through targeted marketing. With visual storytelling and clustering techniques, businesses like Blinkit can derive actionable insights and make data-driven decisions.




