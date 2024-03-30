from flask import Flask, request, render_template, url_for
from aws_bill_calculator import calculate_aws_bill
from ip_address import get_ip_address
from tabulate import tabulate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        # Get credentials from the form
        aws_access_key_id = request.form['aws_access_key_id']
        aws_secret_access_key = request.form['aws_secret_access_key']
        aws_region = "us-east-1"

        start_date_str = request.form['start_date']
        end_date_str = request.form['end_date']

        # Calculate AWS bill
        formatted_amount, unit = calculate_aws_bill(aws_access_key_id, aws_secret_access_key, aws_region, start_date_str, end_date_str)

        # Prepare output message and table data
        output_message = f"For period {start_date_str} - {end_date_str}\nYour total amount is {formatted_amount} {unit}"
        table_data = [
            ["Period", "Total Amount"],
            [f"{start_date_str} - {end_date_str}", f"{formatted_amount} {unit}"]
        ]

        # Generate HTML table
        html_table = f"""
        <div class="title", align="center">
            <h2>This is a simple call to calculate your bill for the specified period</h2>
        </div>
        <style>
            table {{
                border-collapse: collapse;
                width: 50%;
                margin: auto;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
        </style>
        <div class="table-container">
            {tabulate(table_data, tablefmt="html")}
        </div>
        
        <br>
        <div align="center">
            <a href="{url_for('root')}" class="btn btn-primary">Go Back</a>
        </div>
        """

        return html_table

    # Render the form for providing AWS credentials
    client_ip, public_ip = get_ip_address(request)
    return render_template('index.html', client_ip=client_ip, public_ip=public_ip)

if __name__ == '__main__':
    app.run(debug=True)
