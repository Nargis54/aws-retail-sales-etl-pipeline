# AWS Retail Sales ETL Pipeline

## Project Overview

This project implements a cloud-based ETL pipeline for retail sales data using AWS services, Python, and CSV processing.

The pipeline collects raw retail sales data, processes and cleans it using AWS Lambda, stores processed data in Amazon S3, and creates a curated sales summary for analysis.

## Architecture

Raw CSV → Amazon S3 → AWS Lambda → Processed Data → Curated Sales Summary → AWS Glue Data Catalog

## AWS Services Used

- Amazon S3 – Data storage with Raw, Processed, and Curated layers
- AWS Lambda – Automated CSV processing and transformation
- AWS IAM – Access and permissions
- AWS Glue – Data cataloging and table schema
- Amazon CloudWatch – Lambda monitoring and logs

## ETL Process

1. Uploaded raw retail sales CSV to Amazon S3.
2. Used S3 event trigger to invoke AWS Lambda.
3. Lambda reads the CSV file from the Raw layer.
4. Duplicate records are removed.
5. Cleaned data is stored in the Processed layer.
6. Category-wise sales summary is generated.
7. Summary data is stored in the Curated layer.
8. AWS Glue Data Catalog is used to define the processed dataset schema.
9. CloudWatch is used for monitoring Lambda execution.

## Data Structure

The retail sales dataset contains:

- Order ID
- Date
- Product
- Category
- Sales
- Quantity
- Profit

## Technologies Used

Python | CSV | Amazon S3 | AWS Lambda | AWS IAM | AWS Glue | Amazon CloudWatch | GitHub

## Project Outcome

The project demonstrates practical experience with:

- ETL pipeline development
- Cloud-based data processing
- Data cleaning and transformation
- AWS S3 data organization
- Serverless processing using Lambda
- Data cataloging using AWS Glue
- CloudWatch monitoring
- Preparing data for business analysis
