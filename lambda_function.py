import json
import boto3
import csv
import io

s3 = boto3.client("s3")


def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    print("Input file:", key)

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response["Body"].read().decode("utf-8")

    rows = list(csv.DictReader(io.StringIO(content)))

    print("Original rows:", len(rows))

    # Remove duplicate rows
    unique_rows = []
    seen = set()

    for row in rows:
        row_tuple = tuple(row.items())

        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)

    print("Cleaned rows:", len(unique_rows))

    # Save processed CSV
    processed_buffer = io.StringIO()

    if unique_rows:
        writer = csv.DictWriter(
            processed_buffer,
            fieldnames=unique_rows[0].keys()
        )
        writer.writeheader()
        writer.writerows(unique_rows)

    s3.put_object(
        Bucket=bucket,
        Key="processed/cleaned_retail_sales.csv",
        Body=processed_buffer.getvalue()
    )

    print("Processed file created.")

    # Create category sales summary
    summary = {}

    for row in unique_rows:
        category = row.get("Category", "Unknown")

        try:
            sales = float(row.get("Sales", 0))
        except:
            sales = 0

        summary[category] = summary.get(category, 0) + sales

    summary_buffer = io.StringIO()

    writer = csv.writer(summary_buffer)
    writer.writerow(["Category", "Total_Sales"])

    for category, total_sales in summary.items():
        writer.writerow([category, round(total_sales, 2)])

    s3.put_object(
        Bucket=bucket,
        Key="curated/sales_summary.csv",
        Body=summary_buffer.getvalue()
    )

    print("Curated summary created.")

    return {
        "statusCode": 200,
        "body": json.dumps("ETL completed successfully")
    }
