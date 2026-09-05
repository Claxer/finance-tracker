# Personal Finance Tracker

A modern and beginner-friendly **Personal Finance Tracker** built with **Python and Web Technologies**.

The project is designed to help users record, organize, monitor, and understand their personal finances through income and expense tracking, budgets, savings goals, financial reports, analytics, and data visualization.

The project currently contains two main implementations:

* **Python Version V2** — built with Python, CustomTkinter, SQLite, and Matplotlib.
* **Web Version V2** — built with HTML, CSS, Vanilla JavaScript, LocalStorage, and Chart.js.

The Web V3 version has been reorganized into a modular folder structure to make the project easier to understand, maintain, expand, and develop.

---

# Table of Contents

* [Project Overview](#project-overview)
* [Project Goals](#project-goals)
* [Main Features](#main-features)

  * [Dashboard](#dashboard)
  * [Transaction Management](#transaction-management)
  * [Search, Filtering, and Sorting](#search-filtering-and-sorting)
  * [Budget Tracking](#budget-tracking)
  * [Savings Goals](#savings-goals)
  * [Financial Reports](#financial-reports)
  * [Analytics](#analytics)
  * [Categories](#categories)
  * [Theme and Currency Settings](#theme-and-currency-settings)
  * [Import and Export](#import-and-export)
* [Financial Calculations](#financial-calculations)
* [Data Storage](#data-storage)
* [Fresh V3 Data Isolation](#fresh-v3-data-isolation)
* [Web Version](#web-version)
* [Web Technologies](#web-technologies)
* [Web Project Structure](#web-project-structure)
* [Web File Responsibilities](#web-file-responsibilities)
* [JavaScript Architecture](#javascript-architecture)
* [Reusable Components](#reusable-components)
* [Python Desktop Version](#python-desktop-version)
* [Python Technologies](#python-technologies)
* [Python Project Structure](#python-project-structure)
* [User Interface and Design](#user-interface-and-design)
* [Responsive Design](#responsive-design)
* [Charts and Data Visualization](#charts-and-data-visualization)
* [Application Data Flow](#application-data-flow)
* [How to Run the Web Version](#how-to-run-the-web-version)
* [How to Run the Python Version](#how-to-run-the-python-version)
* [Development Workflow](#development-workflow)
* [Data Privacy](#data-privacy)
* [Current Limitations](#current-limitations)
* [Future Improvements](#future-improvements)
* [Learning Objectives](#learning-objectives)
* [Python vs Web Version](#python-vs-web-version)
* [Project Status](#project-status)
* [Roadmap](#roadmap)
* [Purpose of the Project](#purpose-of-the-project)
* [Author](#author)
* [License](#license)

---

# Project Overview

The **Personal Finance Tracker** is a financial management application designed to provide users with a simple way to understand and manage their money.

The application allows users to:

* Record income
* Record expenses
* Edit transactions
* Delete transactions
* Categorize transactions
* Search transactions
* Filter transactions
* Sort transactions
* Create budgets
* Monitor spending against budgets
* Create savings goals
* Track savings progress
* Generate financial reports
* Analyze spending patterns
* View financial charts
* Export financial data
* Import previously exported data
* Change application themes
* Change currency formatting

The main purpose of the project is to combine practical financial management with programming concepts learned through Python and Web Development.

---

# Project Goals

The project was created with several goals in mind.

## 1. Personal Financial Management

The application provides a centralized place where users can record and review their financial activity.

## 2. Financial Awareness

Users can see where their money is going through summaries, charts, reports, and category breakdowns.

## 3. Budget Management

Users can establish spending limits and compare their planned budgets with actual spending.

## 4. Savings Management

Users can create savings goals and monitor their progress toward each target.

## 5. Programming Practice

The project provides practical experience with:

* Python
* JavaScript
* HTML
* CSS
* SQLite
* LocalStorage
* Data structures
* Functions
* Modules
* CRUD operations
* Event handling
* Data visualization
* File import/export
* User interface design

## 6. Software Organization

The Web V3 version was reorganized into separate modules so that different parts of the application are easier to maintain and update.

---

# Main Features

## Dashboard

The Dashboard provides a quick overview of the user's current financial situation.

It displays information such as:

* Current balance
* Total income
* Total expenses
* Savings rate
* Recent transactions
* Cash-flow information
* Spending by category
* Budget health
* Savings progress

The dashboard is intended to answer the most important financial questions quickly:

> How much money do I have?

> How much did I earn?

> How much did I spend?

> Where did I spend my money?

> How are my budgets doing?

> How close am I to my savings goals?

---

# Transaction Management

Transactions are the main source of financial data in the application.

Users can create both:

* Income transactions
* Expense transactions

Each transaction can contain information such as:

* Transaction type
* Amount
* Date
* Category
* Payment method
* Description
* Recurring transaction status

## Supported Transaction Types

### Income

Examples include:

* Salary
* Allowance
* Freelance income
* Other sources of income

### Expense

Examples include:

* Food
* Transportation
* School
* Bills
* Entertainment
* Shopping
* Health
* Subscriptions
* Other expenses

---

# Transaction CRUD Operations

The application supports the basic CRUD operations.

### Create

Users can add a new income or expense transaction.

### Read

Users can view their saved transactions.

### Update

Users can edit existing transactions.

### Delete

Users can remove transactions that are no longer needed.

CRUD functionality is an important part of the project because it demonstrates how applications manage user-created data.

---

# Search, Filtering, and Sorting

The Transactions page provides tools for finding specific financial records.

## Search

Users can search transactions using information such as descriptions and transaction-related text.

## Filtering

Transactions can be filtered by:

* Income
* Expense
* Category

## Sorting

Transactions can be sorted by:

* Newest
* Oldest
* Highest amount
* Lowest amount

A reset option is also available to return the transaction list to its default state.

---

# Budget Tracking

The Budget system allows users to create spending plans for different categories.

A budget can be used to establish a maximum amount that the user wants to spend.

For example:

```text
Food Budget
Planned: ₱5,000
Spent:   ₱3,200
Left:    ₱1,800
```

The application can display:

* Total planned budget
* Total amount spent
* Remaining budget
* Individual budget progress
* Budget health

Budget tracking helps users compare their planned spending with their actual spending.

---

# Savings Goals

The Savings feature allows users to create financial goals.

Examples include:

* New laptop
* Emergency fund
* School expenses
* Vacation
* New phone
* Personal savings

Each goal can contain:

* Goal name
* Target amount
* Current saved amount
* Progress toward the goal

For example:

```text
Goal: New Laptop

Target: ₱50,000
Saved:  ₱30,000

Progress: 60%
```

The application provides visual progress indicators to make savings goals easier to understand.

---

# Financial Reports

The Reports page provides a more detailed view of financial activity.

Users can select a month and view information such as:

* Monthly income
* Monthly expenses
* Net cash flow
* Savings rate
* Top spending categories
* Monthly financial details

The report system makes it easier to compare financial performance from month to month.

---

# Analytics

The Analytics page provides additional information about spending behavior.

Current analytics include:

* Average expense
* Largest expense
* Top spending category
* Transaction count
* 12-month expense trend
* Category analysis

Analytics are useful for identifying spending patterns.

For example, a user may discover that:

```text
Food       → 35%
Transport  → 20%
Shopping   → 15%
Bills      → 15%
Other      → 15%
```

This can help the user identify categories where spending may need to be reduced.

---

# Categories

The application provides default transaction categories.

Current categories include:

* Food
* Transportation
* School
* Bills
* Entertainment
* Shopping
* Salary
* Allowance
* Health
* Subscriptions
* Other

Categories make it easier to organize financial information and generate spending breakdowns.

The category system is designed so that it can be expanded in future versions.

---

# Theme and Currency Settings

The Settings page allows users to customize parts of the application's appearance and financial display.

## Theme

The Web V3 version supports:

* Light mode
* Dark mode

The selected theme is saved in browser storage.

## Currency

The application supports formatting for:

* Philippine Peso (PHP)
* US Dollar (USD)
* Euro (EUR)
* British Pound (GBP)
* Japanese Yen (JPY)

### Important Currency Note

Changing the currency setting changes the **display formatting**.

It does not perform live currency exchange-rate conversion.

For example, changing PHP to USD does not automatically convert:

```text
₱1,000
```

into its current USD equivalent.

---

# Import and Export

The application provides tools for backing up and transferring financial information.

## JSON Export

Users can export application data as a JSON file.

JSON export can be useful for:

* Backups
* Data transfer
* Development
* Restoring information later

## CSV Export

Transaction data can also be exported as a CSV file.

CSV files can be opened using applications such as:

* Microsoft Excel
* Google Sheets
* LibreOffice Calc

## JSON Import

Previously exported JSON data can be imported back into the application.

This allows users to restore or transfer their financial data.

---

# Financial Calculations

The application performs several basic financial calculations.

## Total Income

The total income is calculated by adding all income transactions.

```text
Total Income = Sum of Income Transactions
```

## Total Expenses

The total expenses are calculated by adding all expense transactions.

```text
Total Expenses = Sum of Expense Transactions
```

## Current Balance

The current balance is calculated as:

```text
Balance = Total Income - Total Expenses
```

For example:

```text
Income:   ₱30,000
Expenses: ₱20,000

Balance:  ₱10,000
```

## Net Monthly Cash Flow

```text
Net Cash Flow = Monthly Income - Monthly Expenses
```

## Savings Rate

The savings rate represents the percentage of income remaining after expenses.

Conceptually:

```text
Savings Rate = (Income - Expenses) / Income × 100
```

The application handles cases where income is zero to avoid invalid calculations.

## Category Spending

The application groups expenses by category to determine where money is being spent.

---

# Data Storage

The two versions of the application use different storage systems.

## Web Version

The Web V3 application uses:

```text
Browser LocalStorage
```

This means financial data is stored locally in the user's browser.

No external database server is required for the current Web V3 implementation.

## Python Version

The Python desktop version uses:

```text
SQLite
```

SQLite provides local database storage for the desktop application.

---

# Fresh V3 Data Isolation

The organized Web V3 version was specifically designed to start with a **fresh data environment**.

Earlier versions of the application used different LocalStorage keys.

The organized V3 version uses a new namespace:

```text
financeTrackerV3FreshTransactions
financeTrackerV3FreshBudgets
financeTrackerV3FreshSavings
financeTrackerV3FreshTheme
financeTrackerV3FreshCurrency
financeTrackerV3FreshCategories
```

Because these keys are different from the older application's keys, the organized V3 application does not automatically load the previous V1/V2 financial data.

This means the fresh V3 application starts with:

```text
Income:   ₱0.00
Expenses: ₱0.00
Balance:  ₱0.00
Budgets:  Empty
Savings:  Empty
```

This is useful when testing a new version without mixing it with older application data.

---

# Web Version

The Web Version is a browser-based implementation of the Personal Finance Tracker.

The current Web V3 version was reorganized from a larger JavaScript file into smaller modules.

This makes the application easier to:

* Understand
* Debug
* Maintain
* Expand
* Reuse
* Test

The Web V3 version does not require a Python backend.

---

# Web Technologies

The Web V3 application uses:

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| HTML5              | Application structure         |
| CSS3               | Styling and layout            |
| Vanilla JavaScript | Application logic             |
| LocalStorage       | Local data persistence        |
| Chart.js           | Charts and data visualization |
| ES Modules         | JavaScript organization       |

The application does not depend on a JavaScript framework such as:

* React
* Vue
* Angular

This keeps the project beginner-friendly and demonstrates core Web Development concepts.

---

# Web Project Structure

The organized Web V3 project follows this structure:

```text
web-version-V2/
│
├── index.html
├── README.md
├── .gitignore
│
├── css/
│   ├── variables.css
│   ├── layout.css
│   ├── components.css
│   ├── pages.css
│   ├── modals.css
│   ├── responsive.css
│   └── style.css
│
├── data/
│   └── categories.js
│
└── js/
    ├── core.js
    ├── app.js
    ├── navigation.js
    ├── data.js
    ├── settings.js
    │
    ├── components/
    │   ├── budget-card.js
    │   ├── charts.js
    │   ├── goal-card.js
    │   ├── modal.js
    │   ├── toast.js
    │   └── transaction-card.js
    │
    ├── features/
    │   ├── budgets.js
    │   ├── import-export.js
    │   ├── savings.js
    │   └── transactions.js
    │
    └── pages/
        ├── analytics.js
        ├── dashboard.js
        └── reports.js
```

---

# Web File Responsibilities

## `index.html`

The main HTML document.

It contains the application's:

* Sidebar
* Navigation
* Dashboard
* Transactions page
* Budgets page
* Savings page
* Reports page
* Analytics page
* Settings page
* Modals
* Forms
* Main application layout

---

# CSS Folder

## `variables.css`

Contains reusable design variables such as:

* Colors
* Spacing
* Border radius
* Typography values
* Shadows
* Other design settings

Centralizing variables makes the interface easier to customize.

## `layout.css`

Controls the main page structure and layout.

## `components.css`

Contains reusable component styles.

Examples include:

* Cards
* Buttons
* Badges
* Inputs
* Tables
* Financial summaries

## `pages.css`

Contains styles specific to application pages.

## `modals.css`

Controls modal windows and transaction forms.

## `responsive.css`

Contains responsive styles for different screen sizes.

## `style.css`

Acts as the main CSS entry point and connects the application's styles together.

---

# Data Folder

## `categories.js`

Contains the application's default transaction categories.

This keeps category information separate from the main application logic.

---

# JavaScript Folder

## `core.js`

Contains shared application functionality.

Examples include:

* Data loading
* Data saving
* LocalStorage keys
* State management
* Currency formatting
* Date formatting
* Transaction calculations
* Category totals
* Utility functions
* HTML escaping
* Common selectors

It also contains the fresh V3 LocalStorage namespace.

---

## `app.js`

Acts as one of the main application entry points.

It connects the different parts of the application and initializes the Web V3 system.

---

## `navigation.js`

Controls navigation between application pages.

It handles switching between:

* Dashboard
* Transactions
* Budgets
* Savings
* Reports
* Analytics
* Settings

---

## `data.js`

Handles application data-related functionality and shared data operations.

---

## `settings.js`

Handles settings such as:

* Theme
* Currency
* Settings persistence

---

# Components

The `components` folder contains reusable interface components.

## `budget-card.js`

Creates and manages budget card interfaces.

## `charts.js`

Handles Chart.js visualizations.

## `goal-card.js`

Creates savings goal cards and progress displays.

## `modal.js`

Handles modal windows used by the application.

## `toast.js`

Displays notification messages to the user.

## `transaction-card.js`

Creates reusable transaction display elements.

---

# Features

The `features` folder contains the application's major functional systems.

## `transactions.js`

Handles:

* Adding transactions
* Editing transactions
* Deleting transactions
* Searching transactions
* Filtering transactions
* Sorting transactions
* Rendering transactions

## `budgets.js`

Handles:

* Creating budgets
* Calculating budget totals
* Calculating spending
* Calculating remaining amounts
* Rendering budget cards

## `savings.js`

Handles:

* Savings goals
* Target amounts
* Saved amounts
* Progress calculations
* Savings goal rendering

## `import-export.js`

Handles:

* JSON export
* CSV export
* JSON import

---

# Pages

The `pages` folder contains logic specific to individual application pages.

## `dashboard.js`

Controls the Dashboard.

It calculates and displays:

* Balance
* Income
* Expenses
* Savings rate
* Recent transactions
* Spending categories
* Budget information
* Savings information
* Cash-flow charts

## `reports.js`

Controls the Reports page.

It provides:

* Monthly reports
* Income summaries
* Expense summaries
* Net cash flow
* Savings rate
* Top spending categories
* Monthly details

## `analytics.js`

Controls the Analytics page.

It provides:

* Average expenses
* Largest expense
* Top category
* Transaction count
* Expense trends
* Category analysis

---

# JavaScript Architecture

The Web V3 project follows a modular JavaScript architecture.

Instead of placing the entire application inside one large JavaScript file, functionality is divided into smaller modules.

Conceptually:

```text
Application
│
├── Core
│   ├── State
│   ├── Storage
│   ├── Calculations
│   └── Utilities
│
├── Navigation
│
├── Features
│   ├── Transactions
│   ├── Budgets
│   ├── Savings
│   └── Import/Export
│
├── Pages
│   ├── Dashboard
│   ├── Reports
│   └── Analytics
│
└── Components
    ├── Cards
    ├── Charts
    ├── Modals
    └── Notifications
```

This structure reduces the amount of code that needs to be changed when adding or fixing a specific feature.

---

# Reusable Components

The Web V3 architecture makes use of reusable components.

For example, instead of manually creating every transaction display separately, the transaction card component can generate transaction interfaces from data.

The same concept applies to:

* Budget cards
* Savings goal cards
* Charts
* Modals
* Toast notifications

This improves consistency throughout the application.

---

# Python Desktop Version

The Python version is a desktop implementation of the Personal Finance Tracker.

It uses a graphical user interface instead of a browser.

The desktop version focuses on demonstrating how the same financial management concept can be implemented using Python.

---

# Python Technologies

The Python version uses:

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| CustomTkinter | Graphical user interface  |
| SQLite        | Local database            |
| Matplotlib    | Charts and visualization  |

---

# Python Features

The Python version includes functionality for managing financial information through a desktop interface.

Major areas include:

* Transaction management
* Financial summaries
* Database storage
* Charts
* Settings
* Financial tracking

The Python implementation is separate from the Web V3 implementation.

The two versions share the same overall project idea but use different technologies and storage systems.

---

# Python Project Structure

A typical organized Python implementation can be structured around separate modules for:

```text
web-version-V2/
│
├── main.py
├── database.py
│
├── transactions/
│   └── ...
│
├── charts/
│   └── ...
│
├── settings/
│   └── ...
│
└── assets/
    └── ...
```

The exact Python structure may evolve as additional features are added.

---

# User Interface and Design

The project uses a modern, clean, and professional interface.

The design direction is inspired by modern technology products, with emphasis on:

* Simplicity
* Clean layouts
* Minimal visual clutter
* Clear typography
* Consistent spacing
* Rounded interface elements
* Financial summary cards
* Visual progress indicators
* Professional dashboards

The interface is intended to feel modern while remaining easy for beginner users to understand.

---

# Design Principles

The application follows several basic UI principles.

## Simplicity

Important information should be easy to find.

## Consistency

Buttons, cards, inputs, and navigation should behave consistently.

## Readability

Financial values should be clearly displayed.

## Visual Hierarchy

Important information such as:

* Balance
* Income
* Expenses
* Budget progress
* Savings progress

should receive appropriate visual emphasis.

## Feedback

Actions such as adding, editing, importing, and deleting information should provide user feedback.

---

# Responsive Design

The Web version includes responsive CSS.

The goal is to allow the application to adapt to different screen sizes, including:

* Desktop computers
* Laptops
* Tablets
* Smaller screens

Responsive design is handled primarily through:

```text
css/responsive.css
```

The interface can therefore be developed further for mobile-friendly use in future versions.

---

# Charts and Data Visualization

The Web V3 version uses **Chart.js** to display financial information visually.

Charts are used to make financial patterns easier to understand.

Current visualization areas include:

## Cash Flow

Displays financial movement involving income and expenses.

## Spending by Category

Shows how expenses are distributed among categories.

## Expense Trends

Displays expense activity over a longer period, including a 12-month trend.

## Category Analysis

Provides additional information about spending distribution.

Charts are dynamically generated based on the user's stored transaction data.

---

# Application Data Flow

The general Web V3 data flow is:

```text
User
  |
  v
HTML Interface
  |
  v
JavaScript Event
  |
  v
Feature Module
  |
  v
Core Data Functions
  |
  v
LocalStorage
  |
  v
Updated Application State
  |
  v
Page / Component Rendering
  |
  v
User Interface
```

For example, when a user adds an expense:

```text
User enters expense
        |
        v
Transaction form
        |
        v
transactions.js
        |
        v
Transaction validation
        |
        v
Core state
        |
        v
LocalStorage
        |
        v
Dashboard / Reports / Analytics
        |
        v
Updated financial information
```

---

# How to Run the Web Version

The Web V3 version does not require Python.

## Option 1: Open `index.html`

1. Download or clone the project.
2. Open the project folder.
3. Locate:

```text
index.html
```

4. Open the file in a modern browser.

Recommended browsers include:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox

Because the project uses JavaScript modules, running the project through a local development server is recommended.

---

# Option 2: VS Code Live Server

For development in Visual Studio Code:

1. Open the project folder in VS Code.
2. Install the **Live Server** extension if needed.
3. Open:

```text
index.html
```

4. Right-click the file.
5. Select:

```text
Open with Live Server
```

The application should then open in your browser.

---

# Web Version Requirements

The Web V3 version primarily requires:

* A modern web browser
* Visual Studio Code if developing locally
* A local server such as Live Server for the best development experience

No Python installation is required for the Web V3 application.

No Node.js installation is required for the current basic Web V3 version.

No database server is required.

---

# Chart.js Dependency

The Web V3 application loads Chart.js through a CDN.

This means an internet connection may be required for the charts to load when using the current setup.

The rest of the application is designed around browser-side JavaScript and LocalStorage.

A future version could store Chart.js locally to make the application more completely offline.

---

# How to Run the Python Version

The Python version requires Python and its required packages.

A typical setup process is:

```bash
python --version
```

or:

```bash
py --version
```

Then install the required dependencies.

Depending on the current Python version of the project, the installation may include packages such as:

```bash
pip install customtkinter
pip install matplotlib
```

SQLite is included with standard Python installations through the `sqlite3` module.

After installing the requirements, run the application's main Python file.

For example:

```bash
python main.py
```

The exact command depends on the final Python project structure.

---

# Development Workflow

A recommended development workflow is:

## 1. Open the Project

Open the project folder in Visual Studio Code.

## 2. Run the Application

For the Web version, use Live Server.

For the Python version, run the Python entry point.

## 3. Test Existing Features

Test:

* Adding transactions
* Editing transactions
* Deleting transactions
* Filtering
* Sorting
* Budgets
* Savings goals
* Reports
* Analytics
* Import/export
* Theme settings
* Currency settings

## 4. Make Changes

Modify the appropriate module rather than placing all new code in one file.

For example:

```text
New transaction feature
        ↓
js/features/transactions.js
```

or:

```text
New chart
        ↓
js/components/charts.js
```

## 5. Test Again

Check that the change does not break other pages.

## 6. Commit Changes

Use Git to save development milestones.

Example:

```bash
git add .
git commit -m "Update finance tracker"
git push
```

---

# Data Privacy

The current Web V3 application is designed around local browser storage.

Financial data is stored in the browser's LocalStorage rather than being sent to a project-owned online database.

This provides a simple offline-first architecture.

However, users should understand that browser storage is not the same as encrypted cloud storage.

Users should avoid treating the current version as a secure financial banking system.

---

# Current Limitations

Although the project contains many features, there are still limitations.

## 1. LocalStorage Storage

Web data is stored in the browser.

Clearing browser storage can remove the application's saved information.

## 2. No User Accounts

The current Web V3 version does not include:

* Login
* Registration
* User authentication
* Multiple user accounts

## 3. No Cloud Synchronization

The application does not currently synchronize financial information between different devices.

## 4. No Online Database

The Web V3 version does not currently use:

* MySQL
* PostgreSQL
* MongoDB
* Firebase
* Supabase

## 5. Currency Formatting Only

Currency selection does not provide real-time exchange-rate conversion.

## 6. Recurring Transactions

Transactions can contain a recurring transaction attribute, but the current implementation does not automatically generate future recurring transactions like a full banking application would.

## 7. Chart.js CDN Dependency

Charts currently rely on Chart.js being loaded from the CDN.

---

# Future Improvements

Possible future features include:

## Authentication

Add:

* User registration
* Login
* Logout
* Password protection
* User-specific data

## Cloud Database

Possible technologies include:

* Firebase
* Supabase
* PostgreSQL
* MySQL

This would allow financial information to be synchronized between devices.

## Mobile Application

The Web version could eventually be converted into:

* Progressive Web App
* Android application
* iOS application

## Advanced Recurring Transactions

Future versions could automatically create:

* Daily transactions
* Weekly transactions
* Monthly transactions
* Yearly transactions

## Advanced Budgeting

Possible additions:

* Budget alerts
* Spending warnings
* Budget history
* Budget recommendations
* Automatic budget calculations

## Advanced Savings

Possible additions:

* Savings contribution history
* Goal deadlines
* Monthly savings targets
* Estimated completion dates
* Savings reminders

## More Reports

Future reports could include:

* Yearly financial reports
* Income vs expense reports
* Net worth reports
* Category comparisons
* Budget performance
* Savings performance

## Data Visualization

Future charts could include:

* Monthly income trends
* Monthly balance trends
* Net worth trends
* Budget vs actual spending
* Savings growth
* Year-over-year comparisons

## Offline Chart.js

Chart.js could be stored locally instead of being loaded from a CDN.

This would improve offline reliability.

---

# Learning Objectives

This project is also designed as a learning project.

It demonstrates practical programming concepts including:

## Python

* Variables
* Functions
* Classes
* Modules
* Object-oriented programming
* Exception handling
* Database operations
* GUI programming
* Data visualization

## HTML

* Semantic structure
* Forms
* Buttons
* Navigation
* Tables
* Modals
* Page layouts

## CSS

* Flexbox
* Grid
* Responsive design
* CSS variables
* Components
* Animations and transitions
* Dark/light themes

## JavaScript

* Variables
* Functions
* Arrays
* Objects
* Events
* DOM manipulation
* Modules
* LocalStorage
* CRUD operations
* Data processing
* Dynamic rendering

## Databases

The Python version introduces:

* SQLite
* Tables
* Records
* Queries
* Database persistence

## Data Visualization

The project demonstrates how financial data can be transformed into visual charts.

---

# Python vs Web Version

| Feature                  | Python Version           | Web V3              |
| ------------------------ | ------------------------ | ------------------- |
| Platform                 | Desktop                  | Browser             |
| Language                 | Python                   | JavaScript          |
| UI                       | CustomTkinter            | HTML/CSS            |
| Database                 | SQLite                   | LocalStorage        |
| Charts                   | Matplotlib               | Chart.js            |
| Transactions             | Yes                      | Yes                 |
| Income Tracking          | Yes                      | Yes                 |
| Expense Tracking         | Yes                      | Yes                 |
| Budgets                  | Supported                | Supported           |
| Savings Goals            | Supported                | Supported           |
| Reports                  | Supported                | Supported           |
| Analytics                | Supported                | Supported           |
| Search                   | Supported                | Supported           |
| Filtering                | Supported                | Supported           |
| Sorting                  | Supported                | Supported           |
| JSON Export              | Varies by implementation | Yes                 |
| CSV Export               | Varies by implementation | Yes                 |
| JSON Import              | Varies by implementation | Yes                 |
| Theme                    | Supported                | Light/Dark          |
| Currency Formatting      | Supported                | PHP/USD/EUR/GBP/JPY |
| Cloud Database           | No                       | No                  |
| User Accounts            | No                       | No                  |
| Requires Python          | Yes                      | No                  |
| Requires Database Server | No                       | No                  |

---

# Project Status

## Current Status: Active Development

The project has progressed beyond a basic transaction tracker.

The current Web V3 version includes:

* Modern dashboard
* Transaction management
* Search
* Filtering
* Sorting
* Budget tracking
* Savings goals
* Financial reports
* Analytics
* Financial charts
* Categories
* Theme settings
* Currency settings
* JSON export
* CSV export
* JSON import
* Modular JavaScript architecture
* Organized CSS architecture
* Fresh V3 LocalStorage namespace
* Responsive layout

The project is still considered an ongoing learning and development project.

---

# Roadmap

## Phase 1 — Basic Finance Tracker

Completed:

* Income tracking
* Expense tracking
* Transaction history
* Categories
* Basic financial calculations

## Phase 2 — Improved Interface

Completed:

* Modern dashboard
* Improved navigation
* Financial cards
* Responsive design
* Theme support

## Phase 3 — Financial Management

Completed:

* Budgets
* Savings goals
* Reports
* Analytics
* Charts

## Phase 4 — Project Organization

Completed:

* Modular JavaScript
* Separate feature modules
* Separate page modules
* Reusable components
* Organized CSS
* Data separation
* Fresh V3 storage namespace

## Phase 5 — Data Management

Completed:

* JSON export
* CSV export
* JSON import

## Phase 6 — Future Development

Planned possibilities:

* User authentication
* Cloud database
* Multi-device synchronization
* Advanced recurring transactions
* Financial notifications
* More advanced reports
* Mobile support
* Progressive Web App functionality
* Improved data backup
* More advanced financial analytics

---

# Purpose of the Project

The Personal Finance Tracker is not intended to replace professional banking or financial management software.

Its main purpose is to provide a practical way to:

1. Practice programming.
2. Learn software organization.
3. Understand data storage.
4. Build a real-world application.
5. Practice frontend development.
6. Practice database concepts.
7. Learn data visualization.
8. Create a useful personal finance tool.

The project demonstrates how a simple idea can gradually evolve into a larger software application.

---

# Project Highlights

The project demonstrates several important software development principles.

### Modular Development

Large parts of the application are divided into smaller modules.

### Reusable Components

Common interface elements are designed to be reused.

### Data Persistence

The application can save financial information locally.

### CRUD Functionality

Users can create, read, update, and delete financial records.

### Data Visualization

Financial information can be represented through charts.

### Responsive UI

The Web version is designed to work across different screen sizes.

### User Customization

Users can change themes and currency formatting.

### Data Portability

Users can export and import financial information.

### Version Isolation

The V3 version uses its own LocalStorage namespace to prevent old application data from automatically appearing in the fresh V3 environment.

---

# Recommended GitHub Repository Organization

For a GitHub repository containing both versions, a future structure could look like:

```text
Personal-Finance-Tracker/
│
├── README.md
│
├── Python-Version/
│   ├── main.py
│   ├── database.py
│   ├── ...
│   └── requirements.txt
│
└── Web-Version/
    ├── index.html
    ├── css/
    ├── data/
    └── js/
```

This keeps the desktop and Web implementations clearly separated.

---

# GitHub Development

The project can be managed using Git and GitHub.

Basic commands include:

```bash
git init
```

```bash
git add .
```

```bash
git commit -m "Initial finance tracker project"
```

```bash
git branch -M main
```

```bash
git remote add origin YOUR_REPOSITORY_URL
```

```bash
git push -u origin main
```

Future changes can be saved using:

```bash
git add .
git commit -m "Update finance tracker"
git push
```

---

# Recommended `.gitignore`

For the Python version, files such as the following should generally not be committed:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
```

For the Web version, browser LocalStorage data is not stored as a normal project file, so there is no LocalStorage database file that needs to be committed.

---

# Security Considerations

The current application is a learning-focused personal finance tool.

It should not be treated as a production banking application.

Future production versions would need additional security features such as:

* Authentication
* Authorization
* Encryption
* Secure server communication
* Database security
* Input validation
* Secure session management
* Backup and recovery
* Protection against common Web vulnerabilities

---

# Conclusion

The Personal Finance Tracker has evolved from a simple transaction-recording application into a more complete financial management project.

The current Web V3 version provides a modern and organized experience with:

```text
Transactions
     +
Budgets
     +
Savings Goals
     +
Reports
     +
Analytics
     +
Charts
     +
Data Import/Export
     +
Customization
```

The project also demonstrates how software can be improved over time by moving from a large, difficult-to-maintain codebase toward a more organized modular architecture.

The combination of a **Python desktop implementation** and an **organized Web V3 implementation** provides an opportunity to compare two different approaches to building the same type of application.

---

# Author

**Jose Navoa**

Information Technology Student

Philippines

---

# License

This project is currently intended primarily for **educational and personal development purposes**.

A formal open-source license can be added in the future if the project is released for public reuse.

---

# Final Project Summary

**Personal Finance Tracker** is a full-featured educational finance management project developed using Python and Web technologies.

### Current Web V3 Features

* Dashboard
* Income tracking
* Expense tracking
* Transaction CRUD
* Categories
* Search
* Filtering
* Sorting
* Budgets
* Savings goals
* Reports
* Analytics
* Financial charts
* Light/Dark themes
* Multiple currency formatting options
* JSON import/export
* CSV export
* LocalStorage persistence
* Modular JavaScript
* Reusable components
* Responsive interface
* Fresh V3 data isolation

### Main Technologies

```text
Python
CustomTkinter
SQLite
Matplotlib
HTML5
CSS3
JavaScript
LocalStorage
Chart.js
Git
GitHub
```

The project is continuously being improved as new programming concepts, design techniques, and software development practices are learned.
