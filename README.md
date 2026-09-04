# Personal Finance Tracker

A beginner-friendly **Personal Finance Tracker** built with **Python and Web Technologies**.

The application allows users to manage income and expenses, organize transactions by category, create budgets, set savings goals, view financial reports, analyze spending activity, and monitor their overall financial balance.

This project contains **two versions of the application**:

- **Python Version** — Desktop application built with Python, CustomTkinter, SQLite, and Matplotlib.
- **Web Version** — Browser-based application built with HTML, CSS, and Vanilla JavaScript.

Both versions are designed around the same goal: making personal financial management simple, organized, and easy to understand.

---

# Features

## Transaction Management

The application provides complete transaction management functionality.

- Add income
- Add expenses
- Edit transactions
- Delete transactions
- Categorize transactions
- Add descriptions
- Record transaction dates
- View transaction history
- Automatically calculate financial totals
- Display recent transactions
- Store transactions locally

Transactions are used throughout the application to calculate balances, reports, budgets, and financial statistics.

---

## Search and Filtering

Users can quickly find financial records using transaction search and filtering features.

- Search transactions
- Filter by transaction type
- Filter by category
- View specific financial records
- Organize transaction information
- Sort financial records

These features make it easier to locate specific transactions without manually checking the entire transaction history.

---

# Dashboard

The Finance Tracker includes a dashboard that provides an overview of the user's financial activity.

## Dashboard Information

- Total income
- Total expenses
- Current balance
- Recent transactions
- Financial activity
- Spending information
- Quick access to application sections
- Financial summary cards

The dashboard automatically calculates the user's financial position based on stored transactions.

### Balance Calculation

```text
Balance = Total Income - Total Expenses
````

Example:

```text
Total Income:     ₱25,000
Total Expenses:   ₱15,000
---------------------------
Current Balance:  ₱10,000
```

If expenses are greater than income, the balance becomes negative.

---

# Budget Tracking

The Python version includes a dedicated **Budgets** section.

Users can create budgets for different spending categories.

## Budget Features

* Create a budget
* Select a budget category
* Set a budget amount
* Assign a budget month
* View saved budgets
* Organize budgets by month
* Track planned spending

Example:

```text
Food
Budget: ₱5,000
Month: September 2026
```

Budget tracking helps users plan how much they want to spend in different categories.

---

# Savings Goals

The application includes a dedicated **Savings Goals** section.

Users can create financial goals and track their progress.

## Savings Features

* Create savings goals
* Set a target amount
* Enter current savings
* Set a target date
* View savings goals
* Update savings progress
* Delete savings goals
* Track progress toward financial targets

Example:

```text
Goal: New Laptop

Target:      ₱50,000
Saved:       ₱20,000
Remaining:   ₱30,000
Target Date: December 2026
```

Savings goals help users keep track of long-term financial plans.

---

# Financial Reports

The application includes a dedicated **Reports** section.

The Reports page provides a summarized view of the user's financial activity.

## Report Features

* Total income
* Total expenses
* Current balance
* Expense breakdown
* Spending by category
* Income by category
* Recent financial activity
* Monthly financial totals
* Percentage-based expense breakdown
* Financial activity overview

The report information is generated directly from the stored transaction data.

---

# Monthly Financial Reports

The database includes support for calculating financial information by month.

Monthly reports can calculate:

* Monthly income
* Monthly expenses
* Monthly balance

The calculation follows:

```text
Monthly Balance = Monthly Income - Monthly Expenses
```

Example:

```text
September 2026

Income:     ₱30,000
Expenses:   ₱18,000
--------------------
Balance:    ₱12,000
```

This allows the application to analyze financial activity over individual months.

---

# Expense Breakdown

The Reports section provides a category-based breakdown of expenses.

Example:

```text
Food             ₱5,000    30%
Transportation   ₱3,000    18%
Bills            ₱4,000    24%
Shopping         ₱2,500    15%
Entertainment    ₱2,000    12%
Other            ₱500       3%
```

The application calculates the percentage of total expenses represented by each category.

This makes it easier to identify where most of the user's money is being spent.

---

# Income Breakdown

Income can also be organized by category.

Example:

```text
Salary       ₱25,000
Allowance     ₱5,000
Other         ₱1,000
--------------------
Total        ₱31,000
```

This helps users understand the different sources of their income.

---

# Recent Transactions

The Dashboard and Reports sections can display recent financial activity.

Recent transaction information includes:

* Transaction category
* Transaction amount
* Transaction type
* Description
* Date

Income and expenses are visually separated to make financial activity easier to understand.

Example:

```text
Salary
+ ₱25,000.00

Food
- ₱500.00

Transportation
- ₱150.00
```

---

# Categories

Transactions can be organized into categories such as:

* Food
* Transportation
* School
* Bills
* Entertainment
* Shopping
* Salary
* Allowance
* Other

Categories are used for:

* Transaction organization
* Expense analysis
* Income analysis
* Reports
* Spending breakdowns
* Budget planning

---

# Python Version

The Python version is a desktop application built using **CustomTkinter**.

It provides a graphical interface for managing personal finances locally.

## Python Features

* Modern desktop interface
* Apple-inspired design
* CustomTkinter GUI
* SQLite database
* Dashboard
* Transaction management
* Budget tracking
* Savings goals
* Financial reports
* Monthly financial calculations
* Expense category breakdown
* Income category breakdown
* Recent transaction activity
* Financial summaries
* Data visualization
* Settings
* Persistent local data storage
* Philippine Peso formatting

---

# Python Technologies

The Python version uses:

* **Python** — Main programming language
* **CustomTkinter** — Desktop GUI framework
* **SQLite** — Local database
* **Matplotlib** — Financial data visualization

SQLite is included with Python through:

```python
sqlite3
```

---

# Python Libraries

```text
customtkinter
matplotlib
```

The project also uses Python's built-in libraries:

```text
sqlite3
os
datetime
```

---

# Python Project Structure

```text
Finance Tracker V2/
│
├── main.py
├── database.py
├── theme.py
├── dashboard.py
├── transactions.py
├── budgets.py
├── savings.py
├── reports.py
├── settings.py
└── finance.db
```

---

# Python File Descriptions

| File              | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `main.py`         | Starts the application and manages the main window and navigation            |
| `database.py`     | Creates and manages the SQLite database and financial data                   |
| `theme.py`        | Stores application colors, fonts, and theme settings                         |
| `dashboard.py`    | Displays the main financial dashboard and summary information                |
| `transactions.py` | Handles adding, editing, deleting, searching, and viewing transactions       |
| `budgets.py`      | Handles budget creation and budget information                               |
| `savings.py`      | Handles savings goals and savings progress                                   |
| `reports.py`      | Displays financial reports, totals, category breakdowns, and recent activity |
| `settings.py`     | Handles application settings and preferences                                 |
| `finance.db`      | SQLite database containing locally stored financial information              |

---

# Python Application Pages

The Python version is organized into multiple sections.

## Dashboard

Provides an overview of:

* Total income
* Total expenses
* Current balance
* Recent transactions
* Financial activity

## Transactions

Used for:

* Adding transactions
* Editing transactions
* Deleting transactions
* Viewing transaction history
* Managing transaction information

## Budgets

Used for:

* Creating budgets
* Selecting categories
* Setting budget amounts
* Assigning months
* Viewing saved budgets

## Savings

Used for:

* Creating savings goals
* Setting target amounts
* Tracking saved amounts
* Setting target dates
* Updating savings progress
* Deleting savings goals

## Reports

Used for:

* Viewing financial totals
* Reviewing expense categories
* Reviewing income categories
* Viewing recent activity
* Reviewing monthly financial information

## Settings

Used for:

* Application preferences
* Interface configuration
* User settings

---

# Apple-Inspired User Interface

The Python version uses a clean interface inspired by modern Apple-style design principles.

The interface focuses on:

* Minimalism
* Clean spacing
* Rounded cards
* Simple navigation
* Clear typography
* White and light-gray surfaces
* Black text
* Blue accent colors
* Clear financial indicators
* Simple visual hierarchy

The primary accent color uses an Apple-inspired blue:

```text
#0071E3
```

The application theme also includes colors for:

* Background
* Cards
* Sidebar
* Text
* Secondary text
* Muted text
* Accent
* Success
* Warning
* Danger
* Borders
* Hover states

The design is intended to make the application look professional while remaining easy to understand.

---

# Python Database

The Python application uses **SQLite** for local data storage.

The database is automatically created when the application starts.

The database contains the following main tables:

```text
transactions
budgets
savings_goals
```

---

# Transactions Database

The `transactions` table stores:

* Transaction ID
* Transaction type
* Category
* Amount
* Description
* Date

Example:

```text
ID:          1
Type:        Expense
Category:    Food
Amount:      ₱500
Description: Lunch
Date:        2026-09-04
```

---

# Budgets Database

The `budgets` table stores:

* Budget ID
* Category
* Budget amount
* Budget month

Example:

```text
Category: Food
Amount:   ₱5,000
Month:    2026-09
```

---

# Savings Goals Database

The `savings_goals` table stores:

* Goal ID
* Goal name
* Target amount
* Saved amount
* Target date

Example:

```text
Goal:        New Laptop
Target:      ₱50,000
Saved:       ₱20,000
Target Date: 2026-12-31
```

---

# Database Functions

The Python database system supports the following operations.

## Transactions

* Add transaction
* Get transactions
* Get individual transaction
* Update transaction
* Delete transaction

## Financial Totals

* Calculate total income
* Calculate total expenses
* Calculate current balance

## Budgets

* Add budget
* Get budgets

## Savings

* Add savings goal
* Get savings goals
* Update savings goal
* Delete savings goal

## Reports

* Calculate monthly totals
* Get expenses by category
* Get income by category
* Get recent transactions

---

# Web Version

The project also includes a browser-based version built using:

* HTML
* CSS
* Vanilla JavaScript
* LocalStorage
* Chart.js
* Canvas

The Web version does not require Python or a backend server.

---

# Web Features

The Web version includes:

* Add income
* Add expenses
* Edit transactions
* Delete transactions
* Search transactions
* Filter transactions
* Categorize transactions
* Add descriptions
* Record dates
* Calculate total income
* Calculate total expenses
* Calculate current balance
* Display transaction history
* Recent transaction information
* Dashboard summary
* Spending breakdown
* Financial charts
* Income versus expense visualization
* Dark Mode
* Light Mode
* Theme persistence
* LocalStorage
* Responsive layout
* Sidebar navigation
* Mobile-friendly interface
* Transaction validation
* Delete confirmation
* Empty-state messages
* Currency formatting
* Philippine Peso support

---

# Web Technologies

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| HTML5         | Application structure                  |
| CSS3          | Interface design and responsive layout |
| JavaScript    | Application logic                      |
| LocalStorage  | Browser-based data storage             |
| Chart.js      | Interactive financial charts           |
| Canvas        | Chart rendering                        |
| CSS Variables | Theme management                       |
| DOM API       | Dynamic interface updates              |

---

# Web Project Structure

```text
Web/
│
├── index.html
├── style.css
└── script.js
```

---

# Web File Descriptions

| File         | Description                                                                     |
| ------------ | ------------------------------------------------------------------------------- |
| `index.html` | Contains the structure and layout of the Finance Tracker                        |
| `style.css`  | Controls the design, themes, animations, layout, and responsive styling         |
| `script.js`  | Handles transactions, calculations, filtering, LocalStorage, themes, and charts |

---

# Web Dashboard

The Web version includes a dashboard that provides a quick overview of financial information.

## Dashboard Components

* Total balance
* Total income
* Total expenses
* Transaction count
* Recent transactions
* Spending breakdown
* Financial activity
* Income versus expense information
* Quick transaction actions
* Summary cards

The dashboard updates automatically whenever financial information changes.

---

# Web Theme System

The Web version supports:

* Dark Mode
* Light Mode
* Theme switching
* Persistent theme preferences
* CSS variable-based colors
* Dynamic interface updates

The selected theme is stored in LocalStorage so the user's preference can remain available between browser sessions.

---

# Web Data Management

The Web version uses the browser's **LocalStorage**.

This allows financial information to remain available after:

* Page refresh
* Browser restart
* Closing the browser

The Web version can:

* Save transactions
* Load transactions
* Update transactions
* Delete transactions
* Synchronize dashboard information
* Maintain financial records locally

---

# Web Validation

The Web version includes input validation to help prevent incorrect financial records.

Validation includes:

* Required fields
* Transaction amount validation
* Transaction type validation
* Category selection
* Date validation
* Description handling
* Delete confirmation
* Empty transaction handling
* Form reset after successful submission

---

# Web Responsive Design

The Web application is designed to work across multiple screen sizes.

Supported layouts include:

* Desktop
* Laptop
* Tablet
* Mobile

The interface dynamically adjusts:

* Sidebar navigation
* Financial cards
* Transaction displays
* Forms
* Charts
* Navigation
* Content spacing

---

# Python vs Web Version

| Feature              | Python Version | Web Version             |
| -------------------- | -------------- | ----------------------- |
| Add Transactions     | Yes            | Yes                     |
| Edit Transactions    | Yes            | Yes                     |
| Delete Transactions  | Yes            | Yes                     |
| Search               | Yes            | Yes                     |
| Filtering            | Yes            | Yes                     |
| Categories           | Yes            | Yes                     |
| Dashboard            | Yes            | Yes                     |
| Financial Summary    | Yes            | Yes                     |
| Budget Tracking      | Yes            | Planned / Web expansion |
| Savings Goals        | Yes            | Planned / Web expansion |
| Reports              | Yes            | Basic financial reports |
| Monthly Totals       | Yes            | Yes                     |
| Expense Breakdown    | Yes            | Yes                     |
| Income Breakdown     | Yes            | Yes                     |
| Recent Transactions  | Yes            | Yes                     |
| Charts               | Matplotlib     | Chart.js / Canvas       |
| Data Storage         | SQLite         | LocalStorage            |
| User Interface       | CustomTkinter  | HTML/CSS                |
| Programming Language | Python         | JavaScript              |
| Runs In              | Desktop        | Web Browser             |
| Theme Support        | Settings       | Dark/Light Mode         |
| Responsive Design    | Desktop        | Yes                     |

The two versions demonstrate how the same application concept can be implemented using different technologies.

---

# Financial Calculations

The application uses financial calculations to determine the user's current financial position.

## Overall Balance

```text
Balance = Total Income - Total Expenses
```

## Monthly Balance

```text
Monthly Balance = Monthly Income - Monthly Expenses
```

## Expense Percentage

```text
Expense Percentage =
Category Expense / Total Expenses × 100
```

These calculations are used by the Dashboard and Reports sections.

---

# Data Visualization

The project supports financial data visualization.

## Python

The Python version uses:

```text
Matplotlib
```

for financial charts.

## Web

The Web version uses:

```text
Chart.js
Canvas
JavaScript
```

for browser-based visualizations.

Charts help users understand:

* Income
* Expenses
* Spending categories
* Financial activity
* Income versus expenses

---

# Philippine Peso Support

The application uses the Philippine Peso symbol:

```text
₱
```

Financial amounts are formatted using comma separators and two decimal places.

Examples:

```text
₱25,000.00
₱5,500.50
₱750.00
```

---

# Installation

## Python Version

### 1. Install Python

Make sure Python 3.x is installed.

Check your version:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/finance-tracker.git
```

---

### 3. Open the Project

```bash
cd finance-tracker
```

---

### 4. Install Dependencies

```bash
pip install customtkinter matplotlib
```

---

### 5. Run the Application

Navigate to the Finance Tracker V2 folder and run:

```bash
python main.py
```

The SQLite database will be created automatically if it does not already exist.

---

# Running the Web Version

The Web version does not require Python or additional packages.

## Option 1 — Open Directly

Open:

```text
Web/index.html
```

in a modern web browser.

---

## Option 2 — VS Code

Open the project in Visual Studio Code.

You can use a local development extension such as **Live Server** to launch:

```text
index.html
```

The Web version will then open in your browser.

---

# How the Application Works

1. Open the Python or Web version.
2. Open the Dashboard.
3. Add an income or expense transaction.
4. Enter the amount.
5. Select a category.
6. Enter a description if needed.
7. Select the transaction date.
8. Save the transaction.
9. View the transaction in the transaction history.
10. Search or filter transactions.
11. Edit transactions when necessary.
12. Delete transactions when necessary.
13. Check the Dashboard for updated totals.
14. Open Budgets to create spending limits.
15. Open Savings to create financial goals.
16. Open Reports to analyze financial activity.
17. Review spending categories.
18. Review income categories.
19. Review recent transactions.
20. Check monthly financial totals.
21. View financial charts.
22. Switch between available themes.
23. Continue using the application with locally stored data.

---

# Requirements

## Python Version

* Python 3.x
* CustomTkinter
* Matplotlib
* SQLite3

## Web Version

* Modern web browser
* HTML5 support
* CSS3 support
* JavaScript support
* LocalStorage support
* Canvas support
* Chart.js support

No external JavaScript framework is required.

---

# Project Architecture

The project demonstrates a multi-page application structure.

```text
                 Finance Tracker
                       │
          ┌────────────┴────────────┐
          │                         │
     Python Version             Web Version
          │                         │
   CustomTkinter GUI          HTML/CSS/JavaScript
          │                         │
       SQLite                  LocalStorage
          │                         │
     Matplotlib                  Chart.js
```

The Python and Web versions use different technologies while following the same general finance-tracking concept.

---

# Application Data Flow

## Python Version

```text
User
  │
  ▼
CustomTkinter Interface
  │
  ▼
Application Pages
  │
  ├── Dashboard
  ├── Transactions
  ├── Budgets
  ├── Savings
  ├── Reports
  └── Settings
  │
  ▼
SQLite Database
  │
  ▼
Financial Data
```

## Web Version

```text
User
  │
  ▼
HTML/CSS Interface
  │
  ▼
JavaScript
  │
  ├── Dashboard
  ├── Transactions
  ├── Reports
  └── Charts
  │
  ▼
LocalStorage
  │
  ▼
Financial Data
```

---

# Future Improvements

Possible future improvements include:

* Web-based budget tracking
* Web-based savings goals
* Advanced monthly reports
* CSV export
* PDF report export
* Recurring transactions
* Backup and restore
* User accounts
* Cloud database synchronization
* Cross-device synchronization
* Advanced financial analytics
* Custom user-defined categories
* Custom currency settings
* Advanced budget notifications
* Improved mobile navigation
* Financial goal dashboard
* Transaction import
* Transaction export
* More chart types
* Advanced report filtering
* Improved data backup
* User authentication
* Cloud-based financial data synchronization

---

# Purpose of the Project

This project was created as a beginner-friendly way to practice **Python desktop development and Web development**.

The project demonstrates how a personal finance application can be developed using different technologies while maintaining similar functionality.

The project focuses on practical programming concepts such as:

* Application development
* GUI development
* Web development
* Database management
* CRUD operations
* Data storage
* Financial calculations
* Data visualization
* Search and filtering
* User input
* Responsive design
* Application organization
* User interface design

---

# Learning Goals

Through this project, the main learning goals are to understand how to:

* Build a complete application
* Create graphical user interfaces
* Create responsive web interfaces
* Work with SQLite databases
* Store and retrieve data
* Perform CRUD operations
* Handle user input
* Validate data
* Calculate financial information
* Create financial reports
* Create charts and visualizations
* Use JavaScript for application logic
* Use browser LocalStorage
* Organize a multi-file project
* Create desktop applications
* Create web applications
* Design user-friendly interfaces
* Separate application logic into multiple files
* Build reusable database functions

---

# Project Versions

## Desktop Version

**Python + CustomTkinter + SQLite + Matplotlib**

A desktop-based finance application designed to run locally on a computer.

The Python version includes:

* Dashboard
* Transactions
* Budgets
* Savings Goals
* Reports
* Settings
* SQLite database
* Financial calculations
* Category analysis
* Recent activity
* Monthly financial calculations
* Matplotlib visualization
* Apple-inspired interface
* Philippine Peso support

---

## Web Version

**HTML + CSS + JavaScript + LocalStorage + Chart.js**

A browser-based version that can be opened without installing Python.

The Web version includes:

* Dashboard
* Transactions
* Search and filtering
* Financial summaries
* Charts
* Category analysis
* Recent transactions
* Dark Mode
* Light Mode
* LocalStorage
* Responsive interface
* Philippine Peso support

---

# Project Status

The project is currently being developed as a **Personal Finance Tracker V2**.

The Python version has been expanded from a basic transaction tracker into a more complete personal finance management application with:

* Transaction management
* Dashboard
* Budget management
* Savings goals
* Financial reports
* Monthly calculations
* Category analysis
* Recent activity
* SQLite database management
* Improved application structure
* Apple-inspired interface

The Web version provides a browser-based alternative using front-end technologies and LocalStorage.

---

# Author

**Jose Navoa**

First-year Information Technology student building beginner-friendly programming projects while learning:

* Python
* JavaScript
* Web Development
* Databases
* GUI Development
* Software Development
* Data Visualization

This project is part of my learning journey in Information Technology and software development.
