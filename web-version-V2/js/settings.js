function setupSettings(){
  qs("#settingsTheme").value=state.theme;qs("#currencySelect").value=state.currency;
  qs("#settingsTheme").onchange=e=>applyTheme(e.target.value);
  qs("#currencySelect").onchange=e=>{state.currency=e.target.value;localStorage.setItem(KEYS.currency,state.currency);renderAll();toast("Currency updated.")};
  qs("#clearTransactionsBtn").onclick=()=>{if(!state.transactions.length)return toast("There are no transactions.");if(confirm("Clear every transaction?")){state.transactions=[];save(KEYS.transactions,state.transactions);renderAll();toast("Transactions cleared.")}};
  qs("#clearAllBtn").onclick=()=>{if(confirm("Reset transactions, budgets and savings goals?")){state.transactions=[];state.budgets={};state.savings=[];persist();renderAll();toast("Finance data reset.")}};
}

function applyTheme(theme){state.theme=theme==="light"?"light":"dark";document.body.classList.toggle("light",state.theme==="light");document.body.classList.toggle("dark",state.theme==="dark");localStorage.setItem(KEYS.theme,state.theme);const s=qs("#settingsTheme");if(s)s.value=state.theme;setTimeout(()=>{renderCashChart();renderDonut();if(qs("#analytics").classList.contains("active-page"))renderAnalytics()},50)}
