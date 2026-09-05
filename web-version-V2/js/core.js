const KEYS = {
  transactions:"financeTrackerV3FreshTransactions",
  budgets:"financeTrackerV3FreshBudgets",
  savings:"financeTrackerV3FreshSavings",
  theme:"financeTrackerV3FreshTheme",
  currency:"financeTrackerV3FreshCurrency",
  categories:"financeTrackerV3FreshCategories"
};
const DEFAULT_CATEGORIES=["Food","Transportation","School","Bills","Entertainment","Shopping","Salary","Allowance","Health","Subscriptions","Other"];
const state={transactions:load(KEYS.transactions,[]),budgets:load(KEYS.budgets,{}),savings:load(KEYS.savings,[]),categories:load(KEYS.categories,DEFAULT_CATEGORIES),currency:localStorage.getItem(KEYS.currency)||"PHP",theme:localStorage.getItem(KEYS.theme)||"dark",dashboardMonth:monthKey(new Date()),reportMonth:monthKey(new Date()),txType:"Expense",cashChart:null,donutChart:null,trendChart:null};

document.addEventListener("DOMContentLoaded",init);

function load(key,fallback){try{const v=localStorage.getItem(key);return v?JSON.parse(v):fallback}catch{return fallback}}

function save(key,value){localStorage.setItem(key,JSON.stringify(value))}

function persist(){save(KEYS.transactions,state.transactions);save(KEYS.budgets,state.budgets);save(KEYS.savings,state.savings);save(KEYS.categories,state.categories)}

function normalizeTransaction(t){return {...t,id:t.id||Date.now()+Math.random(),type:t.type==="Income"?"Income":"Expense",amount:Number(t.amount)||0,category:t.category||"Other",description:t.description||"",date:t.date||today(),paymentMethod:t.paymentMethod||"Cash",recurring:!!t.recurring}}

function today(){const d=new Date();return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`}

function monthKey(d){return `${d.getFullYear()}-${pad(d.getMonth()+1)}`}

function pad(n){return String(n).padStart(2,"0")}

function money(n){const codes={PHP:"PHP",USD:"USD",EUR:"EUR",GBP:"GBP",JPY:"JPY"};return new Intl.NumberFormat("en-US",{style:"currency",currency:codes[state.currency],maximumFractionDigits:state.currency==="JPY"?0:2}).format(Number(n)||0)}

function shortMoney(n){const v=Number(n)||0;if(Math.abs(v)>=1000000)return (v/1000000).toFixed(1)+"M";if(Math.abs(v)>=1000)return (v/1000).toFixed(1)+"K";return Math.round(v).toString()}

function dateText(v){if(!v)return "—";return new Date(v+"T00:00:00").toLocaleDateString("en-US",{month:"short",day:"numeric",year:"numeric"})}

function escape(v){return String(v??"").replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[m]))}

function qs(s){return document.querySelector(s)}

function qsa(s){return [...document.querySelectorAll(s)]}

function sum(arr){return arr.reduce((a,b)=>a+(Number(b)||0),0)}

function txInMonth(month){return state.transactions.filter(t=>t.date?.startsWith(month))}

function income(month){return sum(txInMonth(month).filter(t=>t.type==="Income").map(t=>t.amount))}

function expenses(month){return sum(txInMonth(month).filter(t=>t.type==="Expense").map(t=>t.amount))}

function net(month){return income(month)-expenses(month)}

function categoryTotals(month=state.dashboardMonth){const map={};txInMonth(month).filter(t=>t.type==="Expense").forEach(t=>map[t.category]=(map[t.category]||0)+t.amount);return map}
