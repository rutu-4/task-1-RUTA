#  Project 1

## Project Title
Data Cleaning & Preparation

## Objective
The objective of this project is to clean a raw dataset by handling missing values, checking duplicates, and verifying date formats so that the data becomes ready for analysis.

## Dataset Used
E-commerce Orders Dataset (`orders.xlsx`)

## Work Done
- Checked missing/null values in the dataset
- Found 309 missing values in the `CouponCode` column
- Filled missing `CouponCode` values with **"No Coupon"**
- Checked duplicate rows
- Checked duplicate `OrderID` values
- Checked invalid date formats in the `Date` column
- Converted the `Date` column into standard **YYYY-MM-DD** format
- Saved the cleaned dataset as `cleaned_orders.xlsx`

## Files in this Project
- `orders.xlsx` → original raw dataset
- `cleaned_orders.xlsx` → cleaned dataset
- `project1_cleaning.py` → Python code used for cleaning
- `change_log.txt` → summary of changes made

## Result
The dataset was successfully cleaned and prepared for further analysis.