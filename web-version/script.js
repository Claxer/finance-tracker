/* =========================================================
   PERSONAL FINANCE TRACKER
   Vanilla JavaScript
   Version 2.0
   ========================================================= */

"use strict";


/* =========================================================
   STORAGE
   ========================================================= */

const STORAGE_KEY = "financeTrackerTransactions";
const THEME_KEY = "financeTrackerTheme";
const BUDGET_KEY = "financeTrackerBudgets";
const SAVINGS_KEY = "financeTrackerSavings";


/* =========================================================
   CATEGORIES
   ========================================================= */

const DEFAULT_CATEGORIES = [
    "Food",
    "Transportation",
    "School",
    "Bills",
    "Entertainment",
    "Shopping",
    "Salary",
    "Allowance",
    "Other"
];


/* =========================================================
   DATA
   ========================================================= */

let transactions = loadTransactions();
let budgets = loadBudgets();
let savingsGoals = loadSavingsGoals();


/* =========================================================
   DOM READY
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
    initializeApp();
});


/* =========================================================
   INITIALIZE
   ========================================================= */

function initializeApp() {

    setupNavigation();
    setupTransactionForm();
    setupFilters();
    setupTheme();
    setupBudgetForm();
    setupSavingsForm();
    setupReportControls();

    updateDate();

    initializeReportMonth();

    renderDashboard();
    renderTransactions();
    renderBudgets();
    renderSavingsGoals();
    renderMonthlyReport();
    renderCharts();

    console.log(
        "Finance Tracker initialized successfully."
    );
}


/* =========================================================
   LOCAL STORAGE
   ========================================================= */

function loadTransactions() {

    try {

        const saved =
            localStorage.getItem(STORAGE_KEY);

        if (!saved) {
            return [];
        }

        const parsed =
            JSON.parse(saved);

        return Array.isArray(parsed)
            ? parsed
            : [];

    } catch (error) {

        console.error(
            "Could not load transactions:",
            error
        );

        return [];
    }
}


function saveTransactions() {

    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(transactions)
    );
}


function loadBudgets() {

    try {

        const saved =
            localStorage.getItem(BUDGET_KEY);

        if (!saved) {
            return {};
        }

        const parsed =
            JSON.parse(saved);

        return parsed &&
            typeof parsed === "object"
            ? parsed
            : {};

    } catch (error) {

        console.error(
            "Could not load budgets:",
            error
        );

        return {};
    }
}


function saveBudgets() {

    localStorage.setItem(
        BUDGET_KEY,
        JSON.stringify(budgets)
    );
}


function loadSavingsGoals() {

    try {

        const saved =
            localStorage.getItem(SAVINGS_KEY);

        if (!saved) {
            return [];
        }

        const parsed =
            JSON.parse(saved);

        return Array.isArray(parsed)
            ? parsed
            : [];

    } catch (error) {

        console.error(
            "Could not load savings goals:",
            error
        );

        return [];
    }
}


function saveSavingsGoals() {

    localStorage.setItem(
        SAVINGS_KEY,
        JSON.stringify(savingsGoals)
    );
}


/* =========================================================
   NAVIGATION
   ========================================================= */

function setupNavigation() {

    const navItems =
        document.querySelectorAll(
            "[data-page]"
        );

    navItems.forEach((item) => {

        item.addEventListener(
            "click",
            () => {

                const page =
                    item.dataset.page;

                if (page) {
                    showPage(page);
                }

            }
        );

    });
}


function showPage(pageName) {

    const pages =
        document.querySelectorAll(
            ".page"
        );

    pages.forEach((page) => {

        page.classList.toggle(
            "active-page",
            page.id === pageName
        );

    });


    const navItems =
        document.querySelectorAll(
            ".nav-btn"
        );

    navItems.forEach((item) => {

        item.classList.toggle(
            "active",
            item.dataset.page === pageName
        );

    });


    if (pageName === "dashboard") {

        renderDashboard();
        renderRecentTransactions();

    }


    if (pageName === "transactions") {

        renderTransactions();

    }


    if (pageName === "budgets") {

        renderBudgets();

    }


    if (pageName === "savings") {

        renderSavingsGoals();

    }


    if (pageName === "reports") {

        renderMonthlyReport();

    }


    if (pageName === "analytics") {

        setTimeout(() => {
            renderCharts();
        }, 50);

    }

}


/* =========================================================
   ADD TRANSACTION
   ========================================================= */

function openAddTransaction() {

    showPage("transactions");

    const amountInput =
        document.getElementById(
            "transactionAmount"
        );

    if (amountInput) {

        setTimeout(() => {

            amountInput.focus();

        }, 100);

    }
}


/* =========================================================
   TRANSACTION FORM
   ========================================================= */

function setupTransactionForm() {

    const form =
        document.getElementById(
            "transactionForm"
        );

    if (!form) {
        return;
    }

    form.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();

            addTransactionFromForm();

        }
    );
}


function addTransactionFromForm() {

    const typeInput =
        document.getElementById(
            "transactionType"
        );

    const amountInput =
        document.getElementById(
            "transactionAmount"
        );

    const categoryInput =
        document.getElementById(
            "transactionCategory"
        );

    const descriptionInput =
        document.getElementById(
            "transactionDescription"
        );

    const dateInput =
        document.getElementById(
            "transactionDate"
        );


    const type =
        typeInput
            ? typeInput.value
            : "Expense";


    const amount =
        Number(
            String(
                amountInput.value
            ).replace(/,/g, "")
        );


    const category =
        categoryInput
            ? categoryInput.value
            : "Other";


    const description =
        descriptionInput
            ? descriptionInput.value.trim()
            : "";


    const transactionDate =
        dateInput &&
        dateInput.value
            ? dateInput.value
            : getToday();


    if (
        !Number.isFinite(amount) ||
        amount <= 0
    ) {

        showMessage(
            "Please enter a valid amount.",
            "error"
        );

        return;
    }


    const transaction = {

        id:
            Date.now(),

        type:
            normalizeType(type),

        amount:
            amount,

        category:
            category || "Other",

        description:
            description,

        date:
            transactionDate

    };


    transactions.unshift(
        transaction
    );


    saveTransactions();

    clearTransactionForm();

    renderDashboard();
    renderTransactions();
    renderBudgets();
    renderMonthlyReport();
    renderCharts();


    showMessage(
        "Transaction added successfully.",
        "success"
    );
}


function clearTransactionForm() {

    const form =
        document.getElementById(
            "transactionForm"
        );

    if (form) {
        form.reset();
    }


    const dateInput =
        document.getElementById(
            "transactionDate"
        );

    if (dateInput) {
        dateInput.value = getToday();
    }

}


/* =========================================================
   FILTERS
   ========================================================= */

function setupFilters() {

    const searchInput =
        document.getElementById(
            "searchInput"
        );

    const typeFilter =
        document.getElementById(
            "typeFilter"
        );

    const categoryFilter =
        document.getElementById(
            "categoryFilter"
        );


    if (searchInput) {

        searchInput.addEventListener(
            "input",
            renderTransactions
        );

    }


    if (typeFilter) {

        typeFilter.addEventListener(
            "change",
            renderTransactions
        );

    }


    if (categoryFilter) {

        categoryFilter.addEventListener(
            "change",
            renderTransactions
        );

    }

}


function getFilteredTransactions() {

    const searchInput =
        document.getElementById(
            "searchInput"
        );

    const typeFilter =
        document.getElementById(
            "typeFilter"
        );

    const categoryFilter =
        document.getElementById(
            "categoryFilter"
        );


    const searchText =
        searchInput
            ? searchInput.value
                .toLowerCase()
                .trim()
            : "";


    const selectedType =
        typeFilter
            ? typeFilter.value
            : "All Types";


    const selectedCategory =
        categoryFilter
            ? categoryFilter.value
            : "All Categories";


    return transactions.filter(
        (transaction) => {

            const searchableText = [

                transaction.type,
                transaction.amount,
                transaction.category,
                transaction.description,
                transaction.date

            ]
                .join(" ")
                .toLowerCase();


            const matchesSearch =
                searchText === "" ||
                searchableText.includes(
                    searchText
                );


            const matchesType =
                selectedType === "All Types" ||
                normalizeType(
                    transaction.type
                ) ===
                normalizeType(
                    selectedType
                );


            const matchesCategory =
                selectedCategory === "All Categories" ||
                transaction.category ===
                selectedCategory;


            return (
                matchesSearch &&
                matchesType &&
                matchesCategory
            );

        }
    );
}


/* =========================================================
   TRANSACTION TABLE
   ========================================================= */

function renderTransactions() {

    const tableBody =
        document.getElementById(
            "transactionTable"
        );

    if (!tableBody) {
        return;
    }


    const filtered =
        getFilteredTransactions();


    tableBody.innerHTML = "";


    if (filtered.length === 0) {

        tableBody.innerHTML = `
            <tr>
                <td colspan="6">
                    <div class="empty-state">
                        No transactions found.
                    </div>
                </td>
            </tr>
        `;

        return;
    }


    filtered.forEach(
        (transaction) => {

            tableBody.appendChild(
                createTransactionElement(
                    transaction
                )
            );

        }
    );

}


function createTransactionElement(transaction) {

    const row =
        document.createElement("tr");


    const isIncome =
        normalizeType(
            transaction.type
        ) === "Income";


    const typeClass =
        isIncome
            ? "type-income"
            : "type-expense";


    const sign =
        isIncome
            ? "+"
            : "-";


    row.innerHTML = `

        <td class="${typeClass}">
            ${escapeHTML(
                transaction.type
            )}
        </td>

        <td class="${typeClass}">
            ${sign}
            ${formatCurrency(
                transaction.amount
            )}
        </td>

        <td>
            ${getCategoryIcon(
                transaction.category
            )}
            ${escapeHTML(
                transaction.category
            )}
        </td>

        <td>
            ${escapeHTML(
                transaction.description ||
                "No description"
            )}
        </td>

        <td>
            ${formatDate(
                transaction.date
            )}
        </td>

        <td>

            <button
                class="delete-btn"
                type="button"
            >
                Delete
            </button>

        </td>

    `;


    const deleteButton =
        row.querySelector(
            ".delete-btn"
        );


    if (deleteButton) {

        deleteButton.addEventListener(
            "click",
            () => {

                deleteTransaction(
                    transaction.id
                );

            }
        );

    }


    return row;
}


/* =========================================================
   RECENT TRANSACTIONS
   ========================================================= */

function renderRecentTransactions() {

    const container =
        document.getElementById(
            "recentTransactions"
        );

    if (!container) {
        return;
    }


    const recent =
        transactions.slice(0, 5);


    if (recent.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No transactions yet.
            </div>
        `;

        return;
    }


    container.innerHTML = "";


    recent.forEach(
        (transaction) => {

            container.appendChild(
                createRecentTransactionElement(
                    transaction
                )
            );

        }
    );

}


function createRecentTransactionElement(transaction) {

    const row =
        document.createElement("div");


    const isIncome =
        normalizeType(
            transaction.type
        ) === "Income";


    const amountClass =
        isIncome
            ? "income"
            : "expense";


    const sign =
        isIncome
            ? "+"
            : "-";


    row.className =
        "transaction-row";


    row.innerHTML = `

        <div class="transaction-icon ${amountClass}">
            ${getCategoryIcon(
                transaction.category
            )}
        </div>

        <div class="transaction-info">

            <strong>
                ${escapeHTML(
                    transaction.description ||
                    transaction.category
                )}
            </strong>

            <span>
                ${escapeHTML(
                    transaction.category
                )}
            </span>

        </div>

        <div class="transaction-date">
            ${formatDate(
                transaction.date
            )}
        </div>

        <div class="transaction-amount ${amountClass}">
            ${sign}
            ${formatCurrency(
                transaction.amount
            )}
        </div>

    `;


    return row;
}


/* =========================================================
   DELETE TRANSACTION
   ========================================================= */

function deleteTransaction(id) {

    const transaction =
        transactions.find(
            (item) =>
                item.id === id
        );


    if (!transaction) {
        return;
    }


    const confirmed =
        window.confirm(
            "Are you sure you want to delete this transaction?"
        );


    if (!confirmed) {
        return;
    }


    transactions =
        transactions.filter(
            (item) =>
                item.id !== id
        );


    saveTransactions();


    renderDashboard();
    renderTransactions();
    renderBudgets();
    renderMonthlyReport();
    renderCharts();


    showMessage(
        "Transaction deleted successfully.",
        "success"
    );
}


/* =========================================================
   DASHBOARD
   ========================================================= */

function renderDashboard() {

    const income =
        getTotalIncome();


    const expenses =
        getTotalExpenses();


    const balance =
        income - expenses;


    updateElement(
        ["balance"],
        formatCurrency(balance)
    );


    updateElement(
        ["income"],
        formatCurrency(income)
    );


    updateElement(
        ["expenses"],
        formatCurrency(expenses)
    );


    const currentMonth =
        getCurrentMonth();


    const monthly =
        getMonthlyData(
            currentMonth
        );


    updateElement(
        ["dashboardMonthlyIncome"],
        formatCurrency(
            monthly.income
        )
    );


    updateElement(
        ["dashboardMonthlyExpenses"],
        formatCurrency(
            monthly.expenses
        )
    );


    updateElement(
        ["dashboardMonthlySavings"],
        formatCurrency(
            monthly.savings
        )
    );


    renderRecentTransactions();
    renderDashboardSavings();

}


function getTotalIncome() {

    return transactions

        .filter(
            (transaction) =>
                normalizeType(
                    transaction.type
                ) === "Income"
        )

        .reduce(
            (total, transaction) =>
                total +
                Number(
                    transaction.amount
                ),

            0
        );

}


function getTotalExpenses() {

    return transactions

        .filter(
            (transaction) =>
                normalizeType(
                    transaction.type
                ) === "Expense"
        )

        .reduce(
            (total, transaction) =>
                total +
                Number(
                    transaction.amount
                ),

            0
        );

}


/* =========================================================
   BUDGET TRACKING
   ========================================================= */

function setupBudgetForm() {

    const form =
        document.getElementById(
            "budgetForm"
        );


    if (!form) {
        return;
    }


    form.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();

            const category =
                document.getElementById(
                    "budgetCategory"
                ).value;


            const amount =
                Number(
                    document.getElementById(
                        "budgetAmount"
                    ).value
                );


            if (
                !Number.isFinite(amount) ||
                amount <= 0
            ) {

                showMessage(
                    "Please enter a valid budget amount.",
                    "error"
                );

                return;
            }


            budgets[category] =
                amount;


            saveBudgets();

            form.reset();

            renderBudgets();

            showMessage(
                `${category} budget saved.`,
                "success"
            );

        }
    );

}


function renderBudgets() {

    const container =
        document.getElementById(
            "budgetList"
        );


    if (!container) {
        return;
    }


    const categories =
        Object.keys(
            budgets
        );


    if (categories.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No budgets created yet.
            </div>
        `;

        updateBudgetSummary();

        return;
    }


    container.innerHTML = "";


    categories.forEach(
        (category) => {

            const budget =
                Number(
                    budgets[category]
                );


            const spent =
                getCurrentMonthCategoryExpense(
                    category
                );


            const remaining =
                budget - spent;


            const percentage =
                budget > 0
                    ? (
                        spent /
                        budget
                    ) *
                    100
                    : 0;


            const progress =
                Math.min(
                    Math.max(
                        percentage,
                        0
                    ),
                    100
                );


            let statusClass =
                "budget-good";


            if (percentage >= 100) {

                statusClass =
                    "budget-danger";

            } else if (
                percentage >= 80
            ) {

                statusClass =
                    "budget-warning";

            }


            const card =
                document.createElement(
                    "div"
                );


            card.className =
                "budget-card";


            card.innerHTML = `

                <div class="budget-card-header">

                    <div>

                        <div class="budget-category">
                            ${getCategoryIcon(category)}
                            ${escapeHTML(category)}
                        </div>

                        <span class="budget-label">
                            Monthly budget
                        </span>

                    </div>

                    <button
                        class="small-danger-btn"
                        type="button"
                    >
                        Delete
                    </button>

                </div>


                <div class="budget-amounts">

                    <div>
                        <span>Spent</span>
                        <strong>
                            ${formatCurrency(spent)}
                        </strong>
                    </div>

                    <div>
                        <span>Budget</span>
                        <strong>
                            ${formatCurrency(budget)}
                        </strong>
                    </div>

                </div>


                <div class="progress-track">

                    <div
                        class="progress-bar ${statusClass}"
                        style="width: ${progress}%"
                    ></div>

                </div>


                <div class="budget-footer">

                    <span>
                        ${percentage.toFixed(0)}% used
                    </span>

                    <strong class="${remaining < 0 ? "negative" : ""}">
                        ${
                            remaining >= 0
                                ? formatCurrency(remaining) + " remaining"
                                : formatCurrency(Math.abs(remaining)) + " over budget"
                        }
                    </strong>

                </div>

            `;


            const deleteButton =
                card.querySelector(
                    ".small-danger-btn"
                );


            deleteButton.addEventListener(
                "click",
                () => {

                    deleteBudget(
                        category
                    );

                }
            );


            container.appendChild(card);

        }
    );


    updateBudgetSummary();

}


function deleteBudget(category) {

    const confirmed =
        window.confirm(
            `Delete the ${category} budget?`
        );


    if (!confirmed) {
        return;
    }


    delete budgets[category];

    saveBudgets();

    renderBudgets();


    showMessage(
        `${category} budget deleted.`,
        "success"
    );

}


function getCurrentMonthCategoryExpense(
    category
) {

    const currentMonth =
        getCurrentMonth();


    return transactions

        .filter(
            (transaction) => {

                return (
                    normalizeType(
                        transaction.type
                    ) === "Expense" &&

                    transaction.category ===
                    category &&

                    transaction.date &&
                    transaction.date.startsWith(
                        currentMonth
                    )
                );

            }
        )

        .reduce(
            (total, transaction) =>
                total +
                Number(
                    transaction.amount
                ),

            0
        );

}


function updateBudgetSummary() {

    const categories =
        Object.keys(
            budgets
        );


    const totalBudget =
        categories.reduce(
            (total, category) =>
                total +
                Number(
                    budgets[category]
                ),

            0
        );


    const totalSpent =
        categories.reduce(
            (total, category) =>
                total +
                getCurrentMonthCategoryExpense(
                    category
                ),

            0
        );


    const remaining =
        totalBudget -
        totalSpent;


    updateElement(
        ["totalBudget"],
        formatCurrency(
            totalBudget
        )
    );


    updateElement(
        ["totalBudgetSpent"],
        formatCurrency(
            totalSpent
        )
    );


    updateElement(
        ["totalBudgetRemaining"],
        formatCurrency(
            remaining
        )
    );

}


/* =========================================================
   SAVINGS GOALS
   ========================================================= */

function setupSavingsForm() {

    const form =
        document.getElementById(
            "savingsForm"
        );


    if (!form) {
        return;
    }


    form.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();


            const name =
                document.getElementById(
                    "goalName"
                ).value.trim();


            const target =
                Number(
                    document.getElementById(
                        "goalTarget"
                    ).value
                );


            const saved =
                Number(
                    document.getElementById(
                        "goalSaved"
                    ).value
                ) || 0;


            const targetDate =
                document.getElementById(
                    "goalDate"
                ).value;


            if (!name) {

                showMessage(
                    "Please enter a goal name.",
                    "error"
                );

                return;
            }


            if (
                !Number.isFinite(target) ||
                target <= 0
            ) {

                showMessage(
                    "Please enter a valid target amount.",
                    "error"
                );

                return;
            }


            if (saved < 0) {

                showMessage(
                    "Saved amount cannot be negative.",
                    "error"
                );

                return;
            }


            const goal = {

                id:
                    Date.now(),

                name:
                    name,

                target:
                    target,

                saved:
                    Math.min(
                        saved,
                        target
                    ),

                targetDate:
                    targetDate || ""

            };


            savingsGoals.push(
                goal
            );


            saveSavingsGoals();

            form.reset();

            renderSavingsGoals();
            renderDashboardSavings();


            showMessage(
                "Savings goal created successfully.",
                "success"
            );

        }
    );

}


function renderSavingsGoals() {

    const container =
        document.getElementById(
            "savingsGoalsList"
        );


    if (!container) {
        return;
    }


    if (savingsGoals.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No savings goals yet.
            </div>
        `;

        return;
    }


    container.innerHTML = "";


    savingsGoals.forEach(
        (goal) => {

            const target =
                Number(
                    goal.target
                );


            const saved =
                Number(
                    goal.saved
                );


            const remaining =
                Math.max(
                    target - saved,
                    0
                );


            const percentage =
                target > 0
                    ? Math.min(
                        (
                            saved /
                            target
                        ) * 100,
                        100
                    )
                    : 0;


            const card =
                document.createElement(
                    "div"
                );


            card.className =
                "savings-card";


            card.innerHTML = `

                <div class="savings-card-header">

                    <div>

                        <div class="goal-icon">
                            ◆
                        </div>

                        <div>
                            <h2>
                                ${escapeHTML(goal.name)}
                            </h2>

                            <span>
                                ${
                                    goal.targetDate
                                        ? "Target: " +
                                          formatDate(
                                              goal.targetDate
                                          )
                                        : "No target date"
                                }
                            </span>
                        </div>

                    </div>

                    <button
                        class="small-danger-btn"
                        type="button"
                    >
                        Delete
                    </button>

                </div>


                <div class="savings-progress">

                    <div class="progress-track">

                        <div
                            class="progress-bar savings-progress-bar"
                            style="width: ${percentage}%"
                        ></div>

                    </div>

                    <div class="savings-percent">
                        ${percentage.toFixed(0)}%
                    </div>

                </div>


                <div class="savings-values">

                    <div>

                        <span>
                            Saved
                        </span>

                        <strong>
                            ${formatCurrency(saved)}
                        </strong>

                    </div>


                    <div>

                        <span>
                            Target
                        </span>

                        <strong>
                            ${formatCurrency(target)}
                        </strong>

                    </div>


                    <div>

                        <span>
                            Remaining
                        </span>

                        <strong>
                            ${formatCurrency(remaining)}
                        </strong>

                    </div>

                </div>


                <div class="savings-add">

                    <input
                        type="number"
                        class="goal-add-input"
                        placeholder="Amount"
                        min="0"
                        step="0.01"
                    >

                    <button
                        class="primary-btn goal-add-btn"
                        type="button"
                    >
                        + Add Savings
                    </button>

                </div>

            `;


            const deleteButton =
                card.querySelector(
                    ".small-danger-btn"
                );


            deleteButton.addEventListener(
                "click",
                () => {

                    deleteSavingsGoal(
                        goal.id
                    );

                }
            );


            const addButton =
                card.querySelector(
                    ".goal-add-btn"
                );


            const addInput =
                card.querySelector(
                    ".goal-add-input"
                );


            addButton.addEventListener(
                "click",
                () => {

                    addSavingsToGoal(
                        goal.id,
                        addInput.value
                    );

                }
            );


            container.appendChild(card);

        }
    );

}


function addSavingsToGoal(
    goalId,
    amount
) {

    const value =
        Number(amount);


    if (
        !Number.isFinite(value) ||
        value <= 0
    ) {

        showMessage(
            "Please enter a valid savings amount.",
            "error"
        );

        return;
    }


    const goal =
        savingsGoals.find(
            (item) =>
                item.id === goalId
        );


    if (!goal) {
        return;
    }


    const remaining =
        Math.max(
            Number(goal.target) -
            Number(goal.saved),
            0
        );


    if (remaining <= 0) {

        showMessage(
            "This savings goal is already complete.",
            "error"
        );

        return;
    }


    goal.saved =
        Math.min(
            Number(goal.saved) +
            value,
            Number(goal.target)
        );


    saveSavingsGoals();

    renderSavingsGoals();
    renderDashboardSavings();


    showMessage(
        "Savings added successfully.",
        "success"
    );

}


function deleteSavingsGoal(goalId) {

    const goal =
        savingsGoals.find(
            (item) =>
                item.id === goalId
        );


    if (!goal) {
        return;
    }


    const confirmed =
        window.confirm(
            `Delete "${goal.name}"?`
        );


    if (!confirmed) {
        return;
    }


    savingsGoals =
        savingsGoals.filter(
            (item) =>
                item.id !== goalId
        );


    saveSavingsGoals();

    renderSavingsGoals();
    renderDashboardSavings();


    showMessage(
        "Savings goal deleted.",
        "success"
    );

}


function renderDashboardSavings() {

    const container =
        document.getElementById(
            "dashboardSavingsGoals"
        );


    if (!container) {
        return;
    }


    if (savingsGoals.length === 0) {

        container.innerHTML = `
            <div class="empty-state small">
                No savings goals yet.
            </div>
        `;

        return;
    }


    const goals =
        savingsGoals.slice(0, 3);


    container.innerHTML = "";


    goals.forEach(
        (goal) => {

            const percentage =
                goal.target > 0
                    ? Math.min(
                        (
                            goal.saved /
                            goal.target
                        ) * 100,
                        100
                    )
                    : 0;


            const item =
                document.createElement(
                    "div"
                );


            item.className =
                "dashboard-goal";


            item.innerHTML = `

                <div class="dashboard-goal-top">

                    <strong>
                        ${escapeHTML(goal.name)}
                    </strong>

                    <span>
                        ${percentage.toFixed(0)}%
                    </span>

                </div>


                <div class="progress-track">

                    <div
                        class="progress-bar savings-progress-bar"
                        style="width: ${percentage}%"
                    ></div>

                </div>

            `;


            container.appendChild(item);

        }
    );

}


/* =========================================================
   MONTHLY REPORTS
   ========================================================= */

function setupReportControls() {

    const monthInput =
        document.getElementById(
            "reportMonth"
        );


    if (!monthInput) {
        return;
    }


    monthInput.addEventListener(
        "change",
        renderMonthlyReport
    );

}


function initializeReportMonth() {

    const monthInput =
        document.getElementById(
            "reportMonth"
        );


    if (monthInput) {

        monthInput.value =
            getCurrentMonth();

    }

}


function renderMonthlyReport() {

    const monthInput =
        document.getElementById(
            "reportMonth"
        );


    if (!monthInput) {
        return;
    }


    const selectedMonth =
        monthInput.value ||
        getCurrentMonth();


    const data =
        getMonthlyData(
            selectedMonth
        );


    updateElement(
        ["reportIncome"],
        formatCurrency(
            data.income
        )
    );


    updateElement(
        ["reportExpenses"],
        formatCurrency(
            data.expenses
        )
    );


    updateElement(
        ["reportSavings"],
        formatCurrency(
            data.savings
        )
    );


    const savingsRate =
        data.income > 0
            ? (
                data.savings /
                data.income
            ) * 100
            : 0;


    updateElement(
        ["reportSavingsRate"],
        `${savingsRate.toFixed(1)}%`
    );


    updateElement(
        ["reportTransactionCount"],
        data.transactions.length.toString()
    );


    const averageExpense =
        data.expenseTransactions.length > 0
            ? data.expenses /
              data.expenseTransactions.length
            : 0;


    updateElement(
        ["reportAverageExpense"],
        formatCurrency(
            averageExpense
        )
    );


    const largestExpense =
        data.expenseTransactions.length > 0
            ? Math.max(
                ...data.expenseTransactions.map(
                    (transaction) =>
                        Number(
                            transaction.amount
                        )
                )
            )
            : 0;


    updateElement(
        ["reportLargestExpense"],
        formatCurrency(
            largestExpense
        )
    );


    renderReportCategories(
        data.categoryTotals
    );

}


function getMonthlyData(month) {

    const monthTransactions =
        transactions.filter(
            (transaction) =>
                transaction.date &&
                transaction.date.startsWith(
                    month
                )
        );


    const income =
        monthTransactions

            .filter(
                (transaction) =>
                    normalizeType(
                        transaction.type
                    ) === "Income"
            )

            .reduce(
                (total, transaction) =>
                    total +
                    Number(
                        transaction.amount
                    ),

                0
            );


    const expenseTransactions =
        monthTransactions.filter(
            (transaction) =>
                normalizeType(
                    transaction.type
                ) === "Expense"
        );


    const expenses =
        expenseTransactions.reduce(
            (total, transaction) =>
                total +
                Number(
                    transaction.amount
                ),

            0
        );


    const categoryTotals = {};


    expenseTransactions.forEach(
        (transaction) => {

            const category =
                transaction.category ||
                "Other";


            categoryTotals[category] =
                (
                    categoryTotals[category] ||
                    0
                ) +
                Number(
                    transaction.amount
                );

        }
    );


    return {

        transactions:
            monthTransactions,

        expenseTransactions:
            expenseTransactions,

        income:
            income,

        expenses:
            expenses,

        savings:
            income - expenses,

        categoryTotals:
            categoryTotals

    };

}


function renderReportCategories(
    categoryTotals
) {

    const container =
        document.getElementById(
            "reportCategories"
        );


    if (!container) {
        return;
    }


    const categories =
        Object.entries(
            categoryTotals
        ).sort(
            (a, b) =>
                b[1] - a[1]
        );


    if (categories.length === 0) {

        container.innerHTML = `
            <div class="empty-state small">
                No expenses for this month.
            </div>
        `;

        return;
    }


    const maximum =
        categories[0][1];


    container.innerHTML = "";


    categories.forEach(
        ([category, amount]) => {

            const percentage =
                maximum > 0
                    ? (
                        amount /
                        maximum
                    ) * 100
                    : 0;


            const row =
                document.createElement(
                    "div"
                );


            row.className =
                "report-category";


            row.innerHTML = `

                <div class="report-category-header">

                    <span>
                        ${getCategoryIcon(category)}
                        ${escapeHTML(category)}
                    </span>

                    <strong>
                        ${formatCurrency(amount)}
                    </strong>

                </div>

                <div class="progress-track">

                    <div
                        class="progress-bar"
                        style="width: ${percentage}%"
                    ></div>

                </div>

            `;


            container.appendChild(row);

        }
    );

}


/* =========================================================
   CHARTS
   ========================================================= */

function renderCharts() {

    renderIncomeExpenseChart();
    renderCategoryChart();
    renderMonthlyChart();

}


function renderIncomeExpenseChart() {

    const canvas =
        document.getElementById(
            "incomeExpenseChart"
        );


    if (!canvas) {
        return;
    }


    const context =
        canvas.getContext("2d");


    if (!context) {
        return;
    }


    const income =
        getTotalIncome();


    const expenses =
        getTotalExpenses();


    context.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    drawBarChart(
        context,
        [
            "Income",
            "Expenses"
        ],
        [
            income,
            expenses
        ],
        canvas.width,
        canvas.height
    );

}


function renderCategoryChart() {

    const canvas =
        document.getElementById(
            "categoryChart"
        );


    if (!canvas) {
        return;
    }


    const context =
        canvas.getContext("2d");


    if (!context) {
        return;
    }


    const categoryTotals = {};


    transactions

        .filter(
            (transaction) =>
                normalizeType(
                    transaction.type
                ) === "Expense"
        )

        .forEach(
            (transaction) => {

                const category =
                    transaction.category ||
                    "Other";


                categoryTotals[category] =
                    (
                        categoryTotals[category] ||
                        0
                    ) +
                    Number(
                        transaction.amount
                    );

            }
        );


    const labels =
        Object.keys(
            categoryTotals
        );


    const values =
        Object.values(
            categoryTotals
        );


    context.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    if (labels.length === 0) {

        drawEmptyChartMessage(
            context,
            canvas,
            "No expense data yet."
        );

        return;
    }


    drawBarChart(
        context,
        labels,
        values,
        canvas.width,
        canvas.height
    );

}


function renderMonthlyChart() {

    const canvas =
        document.getElementById(
            "monthlyChart"
        );


    if (!canvas) {
        return;
    }


    const context =
        canvas.getContext("2d");


    if (!context) {
        return;
    }


    const monthlyTotals = {};


    transactions

        .filter(
            (transaction) =>
                normalizeType(
                    transaction.type
                ) === "Expense"
        )

        .forEach(
            (transaction) => {

                const month =
                    transaction.date
                        ? transaction.date.slice(
                            0,
                            7
                        )
                        : "Unknown";


                monthlyTotals[month] =
                    (
                        monthlyTotals[month] ||
                        0
                    ) +
                    Number(
                        transaction.amount
                    );

            }
        );


    const labels =
        Object.keys(
            monthlyTotals
        ).sort();


    const values =
        labels.map(
            (label) =>
                monthlyTotals[label]
        );


    context.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    if (labels.length === 0) {

        drawEmptyChartMessage(
            context,
            canvas,
            "No monthly data yet."
        );

        return;
    }


    drawBarChart(
        context,
        labels,
        values,
        canvas.width,
        canvas.height
    );

}


function drawBarChart(
    context,
    labels,
    values,
    width,
    height
) {

    const padding = 50;


    const chartWidth =
        width -
        padding * 2;


    const chartHeight =
        height -
        padding * 2;


    const maxValue =
        Math.max(
            ...values,
            1
        );


    const slotWidth =
        chartWidth /
        labels.length;


    const barWidth =
        Math.min(
            slotWidth * 0.6,
            100
        );


    context.font =
        "12px Arial";


    context.textAlign =
        "center";


    labels.forEach(
        (label, index) => {

            const value =
                Number(
                    values[index]
                );


            const barHeight =
                (
                    value /
                    maxValue
                ) *
                chartHeight;


            const x =
                padding +
                index *
                slotWidth +
                (
                    slotWidth -
                    barWidth
                ) / 2;


            const y =
                height -
                padding -
                barHeight;


            context.fillStyle =
                "#2563eb";


            context.fillRect(
                x,
                y,
                barWidth,
                barHeight
            );


            context.fillStyle =
                "#888";


            context.fillText(
                shortenLabel(label),
                x +
                barWidth / 2,
                height -
                padding +
                20
            );


            context.fillText(
                formatCompactCurrency(value),
                x +
                barWidth / 2,
                Math.max(
                    y - 8,
                    15
                )
            );

        }
    );


    context.strokeStyle =
        "#cccccc";


    context.lineWidth = 1;


    context.beginPath();


    context.moveTo(
        padding,
        height -
        padding
    );


    context.lineTo(
        width -
        padding,
        height -
        padding
    );


    context.stroke();

}


function drawEmptyChartMessage(
    context,
    canvas,
    message
) {

    context.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    context.fillStyle =
        "#777";


    context.font =
        "14px Arial";


    context.textAlign =
        "center";


    context.fillText(
        message,
        canvas.width / 2,
        canvas.height / 2
    );

}


/* =========================================================
   REFRESH
   ========================================================= */

function refreshApp() {

    transactions =
        loadTransactions();


    budgets =
        loadBudgets();


    savingsGoals =
        loadSavingsGoals();


    renderDashboard();
    renderTransactions();
    renderBudgets();
    renderSavingsGoals();
    renderMonthlyReport();
    renderCharts();


    showMessage(
        "Finance tracker refreshed.",
        "success"
    );

}


/* =========================================================
   CLEAR TRANSACTIONS
   ========================================================= */

function clearAllTransactions() {

    if (
        transactions.length === 0
    ) {

        showMessage(
            "There are no transactions to clear.",
            "error"
        );

        return;
    }


    const confirmed =
        window.confirm(
            "This will delete all transactions. Continue?"
        );


    if (!confirmed) {
        return;
    }


    transactions = [];


    saveTransactions();


    renderDashboard();
    renderTransactions();
    renderBudgets();
    renderMonthlyReport();
    renderCharts();


    showMessage(
        "All transactions have been cleared.",
        "success"
    );

}


/* =========================================================
   CLEAR BUDGETS + SAVINGS
   ========================================================= */

function clearAllFinanceData() {

    const hasData =
        Object.keys(budgets).length > 0 ||
        savingsGoals.length > 0;


    if (!hasData) {

        showMessage(
            "There are no budgets or savings goals to clear.",
            "error"
        );

        return;
    }


    const confirmed =
        window.confirm(
            "Delete all budgets and savings goals?"
        );


    if (!confirmed) {
        return;
    }


    budgets = [];
    budgets = {};

    savingsGoals = [];


    saveBudgets();
    saveSavingsGoals();


    renderBudgets();
    renderSavingsGoals();
    renderDashboardSavings();


    showMessage(
        "Budgets and savings goals cleared.",
        "success"
    );

}


/* =========================================================
   THEME
   ========================================================= */

function setupTheme() {

    const savedTheme =
        localStorage.getItem(
            THEME_KEY
        ) || "dark";


    applyTheme(savedTheme);


    const themeSelect =
        document.getElementById(
            "themeSelect"
        );


    const settingsTheme =
        document.getElementById(
            "settingsTheme"
        );


    if (themeSelect) {

        themeSelect.value =
            savedTheme;


        themeSelect.addEventListener(
            "change",
            () => {

                applyTheme(
                    themeSelect.value
                );

            }
        );

    }


    if (settingsTheme) {

        settingsTheme.value =
            savedTheme;


        settingsTheme.addEventListener(
            "change",
            () => {

                applyTheme(
                    settingsTheme.value
                );

            }
        );

    }

}


function applyTheme(theme) {

    if (
        theme !== "light" &&
        theme !== "dark"
    ) {

        theme = "dark";

    }


    document.body.classList.toggle(
        "light",
        theme === "light"
    );


    document.body.classList.toggle(
        "dark",
        theme === "dark"
    );


    localStorage.setItem(
        THEME_KEY,
        theme
    );


    const themeSelect =
        document.getElementById(
            "themeSelect"
        );


    const settingsTheme =
        document.getElementById(
            "settingsTheme"
        );


    if (themeSelect) {
        themeSelect.value = theme;
    }


    if (settingsTheme) {
        settingsTheme.value = theme;
    }

}


/* =========================================================
   DATE
   ========================================================= */

function updateDate() {

    const dateInputs =
        document.querySelectorAll(
            "input[type='date']"
        );


    dateInputs.forEach(
        (input) => {

            if (!input.value) {

                input.value =
                    getToday();

            }

        }
    );

}


function getToday() {

    const now =
        new Date();


    const year =
        now.getFullYear();


    const month =
        String(
            now.getMonth() + 1
        ).padStart(
            2,
            "0"
        );


    const day =
        String(
            now.getDate()
        ).padStart(
            2,
            "0"
        );


    return `${year}-${month}-${day}`;

}


function getCurrentMonth() {

    const now =
        new Date();


    const year =
        now.getFullYear();


    const month =
        String(
            now.getMonth() + 1
        ).padStart(
            2,
            "0"
        );


    return `${year}-${month}`;

}


/* =========================================================
   MESSAGE
   ========================================================= */

function showMessage(
    message,
    type
) {

    const existing =
        document.querySelector(
            ".finance-message"
        );


    if (existing) {
        existing.remove();
    }


    const messageElement =
        document.createElement(
            "div"
        );


    messageElement.className =
        `finance-message ${type}`;


    messageElement.textContent =
        message;


    document.body.appendChild(
        messageElement
    );


    setTimeout(
        () => {

            if (
                messageElement.parentNode
            ) {

                messageElement.remove();

            }

        },
        3000
    );

}


/* =========================================================
   HELPERS
   ========================================================= */

function normalizeType(type) {

    const value =
        String(type || "")
            .trim()
            .toLowerCase();


    if (
        value === "income"
    ) {

        return "Income";

    }


    return "Expense";

}


function formatCurrency(amount) {

    const value =
        Number(amount) || 0;


    return value.toLocaleString(
        "en-PH",
        {
            style: "currency",
            currency: "PHP",
            minimumFractionDigits: 2
        }
    );

}


function formatCompactCurrency(amount) {

    const value =
        Number(amount) || 0;


    if (
        value >= 1000000
    ) {

        return (
            "₱" +
            (
                value /
                1000000
            ).toFixed(1) +
            "M"
        );

    }


    if (
        value >= 1000
    ) {

        return (
            "₱" +
            (
                value /
                1000
            ).toFixed(1) +
            "K"
        );

    }


    return (
        "₱" +
        value.toFixed(0)
    );

}


function formatDate(dateString) {

    if (!dateString) {
        return "-";
    }


    const date =
        new Date(
            `${dateString}T00:00:00`
        );


    if (
        Number.isNaN(
            date.getTime()
        )
    ) {

        return dateString;

    }


    return date.toLocaleDateString(
        "en-PH",
        {
            month: "short",
            day: "numeric",
            year: "numeric"
        }
    );

}


function getCategoryIcon(category) {

    const icons = {

        Food: "🍴",

        Transportation: "🚗",

        School: "🎓",

        Bills: "📄",

        Entertainment: "🎮",

        Shopping: "🛒",

        Salary: "💰",

        Allowance: "💵",

        Other: "📌"

    };


    return (
        icons[category] ||
        "📌"
    );

}


function shortenLabel(label) {

    const text =
        String(label);


    if (
        text.length <= 10
    ) {

        return text;

    }


    return (
        text.substring(
            0,
            9
        ) +
        "..."
    );

}


function updateElement(
    ids,
    value
) {

    ids.forEach(
        (id) => {

            const element =
                document.getElementById(
                    id
                );


            if (element) {

                element.textContent =
                    value;

            }

        }
    );

}


function escapeHTML(value) {

    return String(value)

        .replace(
            /&/g,
            "&amp;"
        )

        .replace(
            /</g,
            "&lt;"
        )

        .replace(
            />/g,
            "&gt;"
        )

        .replace(
            /"/g,
            "&quot;"
        )

        .replace(
            /'/g,
            "&#039;"
        );

}


/* =========================================================
   SAMPLE DATA
   ========================================================= */

function addSampleData() {

    transactions = [

        {
            id: Date.now() - 3,
            type: "Income",
            amount: 15000,
            category: "Allowance",
            description: "Monthly allowance",
            date: getToday()
        },

        {
            id: Date.now() - 2,
            type: "Expense",
            amount: 250,
            category: "Food",
            description: "Lunch",
            date: getToday()
        },

        {
            id: Date.now() - 1,
            type: "Expense",
            amount: 100,
            category: "Transportation",
            description: "Jeepney fare",
            date: getToday()
        }

    ];


    saveTransactions();


    renderDashboard();
    renderTransactions();
    renderBudgets();
    renderMonthlyReport();
    renderCharts();


    showMessage(
        "Sample transactions added.",
        "success"
    );

}


/* =========================================================
   GLOBAL ACCESS
   ========================================================= */

window.financeTracker = {

    addTransaction:
        addTransactionFromForm,

    deleteTransaction:
        deleteTransaction,

    clearAllTransactions:
        clearAllTransactions,

    refresh:
        refreshApp,

    addSampleData:
        addSampleData,

    getTransactions:
        () => transactions,

    getIncome:
        getTotalIncome,

    getExpenses:
        getTotalExpenses,

    getBalance:
        () =>
            getTotalIncome() -
            getTotalExpenses(),

    getBudgets:
        () => budgets,

    getSavingsGoals:
        () => savingsGoals

};
