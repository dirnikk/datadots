import boto3
from datetime import datetime, timedelta

def calculate_aws_bill(aws_access_key_id, aws_secret_access_key, aws_region, start_date_str, end_date_str):
    # Create a boto3 client for the AWS Cost Explorer Service with provided credentials
    ce_client = boto3.client('ce', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # Get cost data for each month in the range and sum up the monthly values
    total_amount = 0
    current_date = start_date
    while current_date < end_date:
        next_month_date = current_date.replace(day=1) + timedelta(days=32)
        next_month_date = next_month_date.replace(day=1)  # Ensure it's the first day of the next month
        next_month_date = min(next_month_date, end_date)  # Ensure it doesn't go beyond the end_date

        response = ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': current_date.strftime('%Y-%m-%d'),
                'End': next_month_date.strftime('%Y-%m-%d')
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )
        total_amount += float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])

        current_date = next_month_date

    # Format the total amount
    formatted_amount = "{:.2f}".format(total_amount)
    unit = response['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']

    return formatted_amount, unit
