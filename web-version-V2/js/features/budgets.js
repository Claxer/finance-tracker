function saveBudget(){const c=qs("#budgetCategory").value,a=Number(qs("#budgetAmount").value);if(!a||a<=0)return toast("Enter a valid budget.");state.budgets[c]=a;save(KEYS.budgets,state.budgets);closeModals();toast(`${c} budget saved.`);renderAll()}

function deleteBudget(c){if(!confirm(`Delete the ${c} budget?`))return;delete state.budgets[c];save(KEYS.budgets,state.budgets);toast("Budget removed.");renderAll()}

function renderDashboardBudgets(){
  const box=qs("#dashboardBudgets"),keys=Object.keys(state.budgets);if(!keys.length){box.innerHTML='<div class="empty">No budgets yet. Set your first limit.</div>';return}
  box.innerHTML=keys.slice(0,4).map(c=>budgetHTML(c,true)).join("")
}

function budgetHTML(c,compact=false){
  const limit=Number(state.budgets[c])||0,spent=sum(txInMonth(state.dashboardMonth).filter(t=>t.type==="Expense"&&t.category===c).map(t=>t.amount)),pct=limit?spent/limit*100:0,cl=pct>=100?"bad":pct>=80?"warn":"good";
  return `<div class="stack-item"><div class="stack-top"><strong>${escape(c)}</strong><span>${money(spent)} / ${money(limit)}</span></div><div class="progress ${cl}"><i style="width:${Math.min(100,pct)}%"></i></div>${compact?"":`<div class="card-footer"><span>${pct.toFixed(0)}% used</span><button class="action-btn" onclick="deleteBudget('${escape(c)}')">Delete</button></div>`}</div>`
}

function renderBudgets(){
  const keys=Object.keys(state.budgets),total=sum(keys.map(k=>state.budgets[k])),spent=sum(keys.map(k=>sum(txInMonth(state.dashboardMonth).filter(t=>t.type==="Expense"&&t.category===k).map(t=>t.amount))));
  qs("#totalBudget").textContent=money(total);qs("#totalBudgetSpent").textContent=money(spent);qs("#totalBudgetRemaining").textContent=money(total-spent);
  qs("#budgetList").innerHTML=keys.length?keys.map(c=>`<article class="budget-card"><div class="card-title"><div><h3>${escape(c)}</h3><span class="subtle">Monthly budget</span></div><button class="action-btn" onclick="deleteBudget('${escape(c)}')">Delete</button></div><div class="amount-pair"><div><span>Spent</span><strong>${money(sum(txInMonth(state.dashboardMonth).filter(t=>t.type==="Expense"&&t.category===c).map(t=>t.amount)))}</strong></div><div><span>Limit</span><strong>${money(state.budgets[c])}</strong></div></div>${budgetHTML(c,false)}</article>`).join(""):'<div class="empty panel">No budgets created yet. Use “Set budget” to start.</div>'
}
