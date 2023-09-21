# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation: Display add transaction form
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        # Append the new transaction to the list
        transactions.append(transaction)

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    # Render the form template to display the add transaction form
    return render_template("form.html")

# Update operation: Display edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])
        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    # Find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

# Delete operation: Delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    # Redirect to the transactions list page
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)


# Practice Exercises
# The following are some practice exercises for the interested learners. We are not providing the solutions for these exercises to encourage the learners to try them on their own. Please feel free to use the course discussion forum for sharing your opinions on the solution with other interested learners.

# Exercise 1: Search Transactions
# In this exercise, you will add a new feature to the application that allows users to search for transactions within a specified amount range. You will create a new route called /search that handles both GET and POST requests in app.py.
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/search.gif
# Instructions:

# Create a new function named search_transactions and use the @app.route decorator to map it to the URL /search.

# Inside the function, check if the request method is POST. If it is, retrieve the minimum and maximum amount values from the form data submitted by the user. Convert these values to floating-point numbers.

# Filter the transactions list based on the amount range specified by the user. Create a new list, filtered_transactions, that contains only the transactions whose amount falls within the specified range. You can use a list comprehension for this.

# Pass the filtered_transactions list to the transactions.html template using the render_template function. In this template, display the transactions similar to the existing transactions.html template.

# If the request method is GET, render a new template called search.html. This template should contain a form that allows users to input the minimum and maximum amount values for the search.


# Exercise 2: Total Balance
# In this exercise, you will add a new feature that calculates and displays the total balance of all transactions. You will create the route in app.py.
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/balance.gif
# Instructions:

# Create a new function named total_balance and use the @app.route decorator to map it to the URL /balance.

# Inside the function, calculate the total balance by summing the amount values of all transactions in the transactions list.

# Return the total balance as a string in the format “Total Balance: {balance}”.

# To display the total balance, you do not need to create a new template. Instead, you will modify the transactions.html template to include the total balance value at the bottom of the table.

# After displaying the list of transactions in the transactions.html template, add a new row to display the total balance. You can use the same render_template function as before, passing both the transactions list and the total balance value.