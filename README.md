# Personal Finance Tracker

A beginner-friendly **Personal Finance Tracker** project built with **Python and Web Technologies**. The application allows users to manage their income and expenses, organize transactions by category, search and filter financial records, view financial summaries, and visualize spending activity.

This project contains **two versions of the application**:

* **Python Version** — Desktop application built with Python, CustomTkinter, SQLite, and Matplotlib.
* **Web Version** — Browser-based application built with HTML, CSS, and Vanilla JavaScript.

Both versions are designed to provide the same core purpose while demonstrating different approaches to application development.

---

# Features

## Transaction Management

* Add income and expenses
* Edit existing transactions
* Delete transactions
* Categorize transactions
* Add transaction descriptions
* Record transaction dates
* View complete transaction history
* Automatically calculate transaction totals

## Search and Filtering

* Search transactions
* Filter transactions by category
* Filter transactions by transaction type
* Find specific financial records quickly
* View filtered transaction results

## Financial Summary

The application provides an overview of the user's financial situation.

* Total income
* Total expenses
* Current balance
* Transaction count
* Financial activity summary
* Income and expense comparisons

Balance is calculated using:

```text
Balance = Total Income - Total Expenses
```

## Categories

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

Categories make it easier to understand where money is being earned and spent.

---

# Python Version

The Python version is a desktop application with a graphical user interface.

## Python Features

* Modern desktop interface
* CustomTkinter GUI
* SQLite database
* Transaction management
* Search and filtering
* Financial summaries
* Financial charts
* Separate application pages
* Settings page
* Persistent local data storage

## Python Technologies

* **Python** — Main programming language
* **CustomTkinter** — GUI framework
* **SQLite** — Local database
* **Matplotlib** — Data visualization

## Python Libraries

```text
customtkinter
matplotlib
```

SQLite is included with Python through the built-in:

```python
sqlite3
```

## Python Project Structure

```text
finance-tracker/
│
├── Python/
│   ├── main.py
│   ├── database.py
│   ├── transactions.py
│   ├── charts.py
│   └── settings.py
│
└── README.md
```

### Python File Descriptions

| File              | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| `main.py`         | Starts the Python application and creates the main window              |
| `database.py`     | Creates and manages the SQLite database                                |
| `transactions.py` | Handles adding, editing, deleting, searching, and viewing transactions |
| `charts.py`       | Displays financial charts and summaries                                |
| `settings.py`     | Handles application settings and preferences                           |

---

# Web Version

The Web version is a browser-based implementation of the Personal Finance Tracker.

It uses **HTML, CSS, and Vanilla JavaScript** without requiring a backend server.

## Web Features

* Add income and expenses
* Edit transactions
* Delete transactions
* Search transactions
* Filter transactions
* Categorize transactions
* Add transaction descriptions
* Record transaction dates
* Calculate total income
* Calculate total expenses
* Calculate current balance
* Display transaction history
* Financial charts and visualizations
* Dark and light theme support
* Responsive user interface
* Local data storage
* Persistent transactions using browser storage
* Dashboard overview
* Balance overview cards
* Income and expense summary cards
* Recent transactions display
* Quick transaction actions
* Transaction modal/form interface
* Transaction type selection
* Transaction amount validation
* Dynamic transaction updates
* Automatic dashboard updates
* Spending category breakdown
* Financial overview statistics
* Interactive financial charts
* Income versus expense visualization
* Category-based spending visualization
* Transaction filtering and sorting
* Empty-state messages when no transactions exist
* Confirmation prompts for deleting transactions
* Form reset after adding transactions
* Automatic LocalStorage synchronization
* Data persistence across browser sessions
* Dynamic theme switching
* Theme preference persistence
* Modern responsive dashboard layout
* Sidebar navigation
* Mobile-friendly navigation
* Responsive transaction tables
* Responsive financial cards
* Interactive navigation sections
* Smooth UI interactions
* Visual feedback for user actions
* Currency formatting
* Philippine Peso (₱) support

## Web Technologies

* **HTML5** — Application structure
* **CSS3** — Styling and responsive interface
* **JavaScript** — Application logic and functionality
* **LocalStorage** — Saving financial data in the browser
* **Canvas** — Financial chart rendering
* **Chart.js** — Interactive financial charts and data visualization
* **CSS Variables** — Dynamic theme colors and UI customization
* **DOM API** — Dynamic interface updates and user interactions

## Web Project Structure

```text
Web/
│
├── index.html
├── style.css
└── script.js
```

### Web File Descriptions

| File         | Description                                                                     |
| ------------ | ------------------------------------------------------------------------------- |
| `index.html` | Contains the structure and layout of the Finance Tracker                        |
| `style.css`  | Controls the design, layout, themes, and responsive styling                     |
| `script.js`  | Handles transactions, calculations, filtering, LocalStorage, themes, and charts |

---

# Web Dashboard

The updated Web version includes a dashboard designed to give users a quick overview of their financial activity.

## Dashboard Components

* Total balance
* Total income
* Total expenses
* Transaction count
* Recent transactions
* Spending breakdown
* Income versus expense information
* Financial activity charts
* Quick access to transaction management
* Responsive summary cards

The dashboard automatically updates when transactions are added, edited, or deleted.

---

# Web User Interface

The Web version includes a modern dashboard-style interface designed to make financial information easier to understand.

## Interface Features

* Sidebar navigation
* Dashboard navigation
* Transaction management interface
* Add transaction modal
* Responsive cards
* Transaction list/table
* Interactive charts
* Theme toggle
* Responsive layout
* Mobile-friendly design
* Visual transaction indicators
* User-friendly forms
* Dynamic content updates

The interface is designed to keep important financial information visible while allowing users to quickly manage their transactions.

---

# Theme System

The Web version supports both **Dark Mode** and **Light Mode**.

## Theme Features

* Dark theme
* Light theme
* Theme toggle
* Persistent theme preference
* CSS variable-based theme colors
* Automatic interface updates when changing themes

The selected theme can remain saved in the browser so the user's preferred appearance can be maintained between sessions.

---

# Web Data Management

The Web version uses **LocalStorage** to maintain financial information directly in the browser.

## Data Management Features

* Save transactions
* Load saved transactions
* Update stored transactions
* Delete stored transactions
* Persist data after page refresh
* Persist data after closing the browser
* Automatically synchronize the dashboard with stored data

All transaction calculations and dashboard information are generated from the stored transaction records.

---

# Web Validation and User Feedback

The Web version includes validation and feedback to help prevent incorrect transaction entries.

## Validation Features

* Required field validation
* Transaction amount validation
* Transaction type validation
* Category selection
* Date validation
* Description handling
* Delete confirmation
* Empty transaction handling
* Form reset after successful submission

These features help make the application easier and safer to use.

---

# Web Responsive Design

The Web version is designed to work across different screen sizes.

## Supported Layouts

* Desktop computers
* Laptops
* Tablets
* Mobile devices

The interface dynamically adjusts navigation, cards, transaction displays, forms, and charts based on the available screen size.

---

# Python vs Web Version

| Feature              | Python Version | Web Version      |
| -------------------- | -------------- | ---------------- |
| Add Transactions     | Yes            | Yes              |
| Edit Transactions    | Yes            | Yes              |
| Delete Transactions  | Yes            | Yes              |
| Search               | Yes            | Yes              |
| Filtering            | Yes            | Yes              |
| Categories           | Yes            | Yes              |
| Financial Summary    | Yes            | Yes              |
| Charts               | Matplotlib     | Canvas           |
| Data Storage         | SQLite         | LocalStorage     |
| User Interface       | CustomTkinter  | HTML/CSS         |
| Programming Language | Python         | JavaScript       |
| Runs In              | Desktop        | Web Browser      |
| Theme Support        | Settings       | Dark/Light Theme |

The two versions demonstrate how the same application concept can be developed using different technologies.

### Updated Web Capabilities

The Web version has been expanded beyond basic transaction management and now provides a more complete dashboard experience.

It includes:

* Interactive dashboard
* Responsive user interface
* Theme switching
* Persistent theme preferences
* Interactive charts
* Recent transaction information
* Dynamic financial summaries
* Browser-based data persistence
* Transaction validation
* Responsive navigation
* Mobile-friendly layouts
* Real-time interface updates

These additions make the Web version more suitable for everyday personal finance tracking while continuing to use a simple front-end technology stack.

---

# Financial Calculation

The application calculates the current balance using:

```text
Balance = Total Income - Total Expenses
```

### Example

```text
Total Income:     ₱25,000
Total Expenses:   ₱15,000
---------------------------
Current Balance:  ₱10,000
```

If expenses are greater than income, the balance will become negative.

---

# Database and Data Storage

## Python Version

The Python application uses **SQLite** to store transactions locally.

The database is automatically created when the application starts.

This allows financial records to remain available even after closing and reopening the application.

```text
Python Application
       │
       ▼
   SQLite Database
       │
       ▼
 Transaction Records
```

## Web Version

The Web application uses the browser's **LocalStorage** to save transactions.

This allows data to remain available after refreshing or closing the browser.

```text
Web Application
       │
       ▼
   LocalStorage
       │
       ▼
 Transaction Records
```

The Python and Web versions use different storage systems because they are separate implementations.

---

# Data Visualization

Both versions provide financial data visualization.

### Python

The Python version uses **Matplotlib** to create financial charts.

### Web

The Web version uses **JavaScript and Canvas** to display financial charts directly in the browser.

Charts can help users understand:

* Income
* Expenses
* Spending by category
* Financial activity
* Income versus expenses

---

# Installation

## Python Version

### 1. Install Python

Make sure Python 3.x is installed.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/finance-tracker.git
```

### 3. Open the Project

```bash
cd finance-tracker
```

### 4. Install Dependencies

```bash
pip install customtkinter matplotlib
```

### 5. Run the Application

```bash
python Python/main.py
```

---

# Running the Web Version

The Web version does not require Python or additional packages.

### Option 1 — Open Directly

Open:

```text
Web/index.html
```

in your web browser.

### Option 2 — Use VS Code

If using Visual Studio Code, you can use a local development extension such as **Live Server** to launch the website.

---

# How It Works

1. Open either the Python or Web version.
2. Add an income or expense transaction.
3. Enter the amount.
4. Select a category.
5. Add a description if needed.
6. Select the transaction date.
7. Save the transaction.
8. View the transaction in the history.
9. Search or filter transactions when needed.
10. Edit or delete transactions.
11. Check the financial summary.
12. Open the Charts section to view financial activity.
13. Use the available settings or theme options.
14. Navigate between the Dashboard and transaction sections.
15. Review updated balance, income, and expense information.
16. View recent transactions from the dashboard.
17. Review spending categories using the available charts.
18. Switch between Dark Mode and Light Mode.
19. Continue using the application with previously saved browser data.
20. Use the responsive interface on different screen sizes.

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

# Future Improvements

Possible future improvements include:

* Monthly financial reports
* Budget tracking
* Savings goals
* Recurring transactions
* Export transactions to CSV
* Export financial reports to PDF
* More chart types
* Monthly spending limits
* Budget notifications
* Backup and restore
* Improved mobile responsiveness
* User accounts
* Cloud database synchronization
* Cross-device data synchronization
* More advanced financial analytics
* Advanced dashboard customization
* More interactive chart controls
* Advanced transaction sorting
* Custom user-defined categories
* Custom currency settings
* Financial goal tracking dashboard
* Improved notification system
* Advanced budget analytics
* Transaction import functionality
* Transaction export functionality

---

# Purpose of the Project

This project was created as a beginner-friendly way to practice both **Python desktop development** and **Web development**.

The project demonstrates:

* Python programming
* JavaScript programming
* HTML and CSS
* Object-oriented programming concepts
* GUI development
* Web interface development
* CRUD operations
* Database management
* Local data storage
* Data visualization
* Search and filtering
* Financial calculations
* File and project organization
* Responsive UI design

Building both versions also helps demonstrate how the same application idea can be implemented using different programming languages and technologies.

---

# Learning Goals

Through this project, the main goals are to understand how to:

* Build a complete application from scratch
* Create graphical user interfaces
* Work with databases
* Store and retrieve data
* Perform CRUD operations
* Handle user input
* Calculate financial information
* Create charts and visualizations
* Use JavaScript for application logic
* Store data using browser LocalStorage
* Organize a multi-file project
* Create both desktop and web applications

---

# Project Versions

### Desktop

**Python + CustomTkinter + SQLite + Matplotlib**

A desktop-based version designed to run locally on a computer.

### Web

**HTML + CSS + JavaScript + LocalStorage + Canvas**

A browser-based version that can be opened without installing Python or additional dependencies.

---

# Author

**Jose Navoa**

First-year Information Technology student building beginner-friendly programming projects while learning Python, JavaScript, web development, databases, and software development.
