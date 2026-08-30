/* =========================================================
   PERSONAL FINANCE TRACKER
   Vanilla JavaScript
   ========================================================= */

"use strict";


/* =========================================================
   DATA
   ========================================================= */

const STORAGE_KEY = "financeTrackerTransactions";
const THEME_KEY = "financeTrackerTheme";

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

let transactions = loadTransactions();


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

    updateDate();

    renderDashboard();

    renderTransactions();

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

        const isActive =
            page.id === pageName;

        page.classList.toggle(
            "active-page",
            isActive
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


    if (
        pageName === "dashboard"
    ) {

        renderDashboard();

        renderRecentTransactions();

    }


    if (
        pageName === "transactions"
    ) {

        renderTransactions();

    }


    if (
        pageName === "analytics"
    ) {

        setTimeout(() => {
            renderCharts();
        }, 50);

    }

}


/* =========================================================
   OPEN ADD TRANSACTION
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


    if (!amountInput) {
        return;
    }


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


    if (!transactionDate) {

        showMessage(
            "Please enter a date.",
            "error"
        );

        return;
    }


    const transaction = {

        id: Date.now(),

        type: normalizeType(type),

        amount: amount,

        category:
            category || "Other",

        description: description,

        date: transactionDate

    };


    transactions.unshift(
        transaction
    );


    saveTransactions();

    clearTransactionForm();

    renderDashboard();

    renderTransactions();

    renderCharts();
    


    showMessage(
        "Transaction added successfully.",
        "success"
    );
}


/* =========================================================
   CLEAR FORM
   ========================================================= */

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

        dateInput.value =
            getToday();

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


/* =========================================================
   FILTER TRANSACTIONS
   ========================================================= */

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
                selectedType ===
                    "All Types" ||

                normalizeType(
                    transaction.type
                ) ===
                normalizeType(
                    selectedType
                );


            const matchesCategory =
                selectedCategory ===
                    "All Categories" ||

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
   RENDER TRANSACTIONS
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

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td colspan="6">
                <div class="empty-state">
                    No transactions found.
                </div>
            </td>
        `;


        tableBody.appendChild(row);

        return;
    }


    filtered.forEach(
        (transaction) => {

            const row =
                createTransactionElement(
                    transaction
                );


            tableBody.appendChild(row);

        }
    );

}


/* =========================================================
   CREATE TABLE TRANSACTION
   ========================================================= */

function createTransactionElement(
    transaction
) {

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
                data-id="${transaction.id}"
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

            const row =
                createRecentTransactionElement(
                    transaction
                );


            container.appendChild(row);

        }
    );

}


/* =========================================================
   CREATE RECENT TRANSACTION
   ========================================================= */

function createRecentTransactionElement(
    transaction
) {

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
        [
            "balance",
            "totalBalance",
            "dashboardBalance"
        ],
        formatCurrency(balance)
    );


    updateElement(
        [
            "income",
            "totalIncome",
            "dashboardIncome"
        ],
        formatCurrency(income)
    );


    updateElement(
        [
            "expenses",
            "totalExpenses",
            "dashboardExpenses"
        ],
        formatCurrency(expenses)
    );


    updateElement(
        [
            "transactionCount",
            "totalTransactions"
        ],
        transactions.length.toString()
    );


    renderRecentTransactions();
}


/* =========================================================
   TOTAL INCOME
   ========================================================= */

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


/* =========================================================
   TOTAL EXPENSES
   ========================================================= */

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
   CHARTS
   ========================================================= */

function renderCharts() {

    renderIncomeExpenseChart();

    renderCategoryChart();

    renderMonthlyChart();

}


/* =========================================================
   INCOME VS EXPENSES
   ========================================================= */

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


/* =========================================================
   CATEGORY CHART
   ========================================================= */

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
                        categoryTotals[
                            category
                        ] || 0
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


/* =========================================================
   MONTHLY CHART
   ========================================================= */

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


/* =========================================================
   BAR CHART
   ========================================================= */

function drawBarChart(
    context,
    labels,
    values,
    width,
    height
) {

    const padding = 50;


    const chartWidth =
        width - padding * 2;


    const chartHeight =
        height - padding * 2;


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
                ) /
                2;


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
                shortenLabel(
                    label
                ),
                x +
                barWidth / 2,
                height -
                padding +
                20
            );


            context.fillText(
                formatCompactCurrency(
                    value
                ),
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
        height - padding
    );


    context.lineTo(
        width - padding,
        height - padding
    );


    context.stroke();

}


/* =========================================================
   EMPTY CHART
   ========================================================= */

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


    renderDashboard();

    renderTransactions();

    renderCharts();


    showMessage(
        "Finance tracker refreshed.",
        "success"
    );

}


/* =========================================================
   CLEAR ALL TRANSACTIONS
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

    renderCharts();


    showMessage(
        "All transactions have been cleared.",
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


/* =========================================================
   APPLY THEME
   ========================================================= */

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

        themeSelect.value =
            theme;

    }


    if (settingsTheme) {

        settingsTheme.value =
            theme;

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
   HELPER: NORMALIZE TYPE
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


/* =========================================================
   HELPER: TODAY
   ========================================================= */

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


/* =========================================================
   HELPER: CURRENCY
   ========================================================= */

function formatCurrency(
    amount
) {

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


/* =========================================================
   HELPER: COMPACT CURRENCY
   ========================================================= */

function formatCompactCurrency(
    amount
) {

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


/* =========================================================
   HELPER: DATE FORMAT
   ========================================================= */

function formatDate(
    dateString
) {

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


/* =========================================================
   HELPER: CATEGORY ICON
   ========================================================= */

function getCategoryIcon(
    category
) {

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


/* =========================================================
   HELPER: SHORTEN LABEL
   ========================================================= */

function shortenLabel(
    label
) {

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


/* =========================================================
   HELPER: UPDATE ELEMENT
   ========================================================= */

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


/* =========================================================
   HELPER: ESCAPE HTML
   ========================================================= */

function escapeHTML(
    value
) {

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
            getTotalExpenses()

};
