# Personal Finance Tracker - Python

A beginner-friendly **Personal Finance Tracker** built with Python. The application allows users to manage their income and expenses, organize transactions by category, and monitor their overall financial status through a graphical user interface.

The project uses **CustomTkinter** for the interface, **SQLite** for storing financial data, and **Matplotlib** for displaying financial charts.

## Features

### Transaction Management

* Add income and expenses
* Edit existing transactions
* Delete transactions
* Categorize transactions
* Add transaction descriptions
* Record transaction dates
* View complete transaction history

### Search and Filtering

* Search transactions
* Filter transactions by category
* Filter transactions by transaction type
* Easily view specific financial records

### Financial Summary

* Calculate total income
* Calculate total expenses
* Calculate current balance
* Display financial summaries
* Monitor spending and income

### Charts and Visualization

* Display financial data using charts
* Visualize income and expenses
* View spending by category
* Get a quick overview of financial activity

### Database

* Store transactions using SQLite
* Keep financial records after closing the application
* Automatically create the required database
* Manage transaction records through the database

### User Interface

* Modern graphical user interface
* Separate pages for different functions
* Transactions page
* Charts page
* Settings page
* User-friendly navigation

## Technologies Used

* **Python** - Main programming language
* **CustomTkinter** - Graphical user interface
* **SQLite** - Local database for storing transactions
* **Matplotlib** - Charts and data visualization

## Python Libraries

The project uses the following Python libraries:

```text
customtkinter
matplotlib
```

SQLite is included with Python through the built-in `sqlite3` module.

## Project Structure

```text
finance-tracker/
│
├── main.py
├── database.py
├── transactions.py
├── charts.py
├── settings.py
└── README.md
```

### File Descriptions

| File              | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| `main.py`         | Starts the application and creates the main window                     |
| `database.py`     | Creates and manages the SQLite database                                |
| `transactions.py` | Handles adding, editing, deleting, searching, and viewing transactions |
| `charts.py`       | Displays financial charts and summaries                                |
| `settings.py`     | Contains application settings and preferences                          |
| `README.md`       | Project documentation                                                  |

## How to Install

### 1. Install Python

Make sure Python is installed on your computer.

You can check your Python version using:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/finance-tracker.git
```

### 3. Open the Project Folder

```bash
cd finance-tracker
```

### 4. Install the Required Libraries

```bash
pip install customtkinter matplotlib
```

## How to Run

Run the following command inside the project folder:

```bash
python main.py
```

The Personal Finance Tracker application should open in a graphical window.

## How It Works

1. Open the application.
2. Add your income or expenses.
3. Assign a category to each transaction.
4. View your transactions in the transaction history.
5. Edit or delete transactions when needed.
6. Use the search and filter options to find specific records.
7. Check your total income, expenses, and balance.
8. Open the Charts page to visualize your financial activity.
9. Use the Settings page to manage application preferences.

## Financial Calculation

The application calculates the current balance using:

```text
Balance = Total Income - Total Expenses
```

For example:

```text
Total Income:     ₱25,000
Total Expenses:   ₱15,000
---------------------------
Current Balance:  ₱10,000
```

## Categories

Transactions can be organized using categories such as:

* Food
* Transportation
* School
* Bills
* Entertainment
* Shopping
* Salary
* Allowance
* Other

Categories can be used to make it easier to understand where money is coming from and where it is being spent.

## Database

The application uses **SQLite** to store transaction records locally.

This means the financial data does not need to be manually entered again every time the application is opened.

The database is created automatically when the application starts.

## Data Visualization

The Charts page uses **Matplotlib** to turn financial data into visual charts.

Charts can help users understand:

* Total income
* Total expenses
* Spending by category
* Overall financial activity

## Requirements

* Python 3.x
* CustomTkinter
* Matplotlib
* SQLite3

## Future Improvements

Possible future features include:

* Monthly financial reports
* Budget tracking
* Savings goals
* Recurring transactions
* Export transactions to CSV
* Export financial reports to PDF
* More chart types
* Dark and light themes
* Password protection
* Backup and restore database
* Monthly spending limits
* Notifications for budget limits

## Purpose of the Project

This project was created as a beginner-friendly Python application to practice:

* Python programming
* Object-oriented programming concepts
* GUI development
* Database management
* CRUD operations
* Data visualization
* File and project organization
* Basic financial calculations

## Author

**Jose Navoa**

A first-year Information Technology student building beginner-friendly programming projects while learning Python and software development.
