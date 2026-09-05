function renderAll(){populateCategories();renderDashboard();renderTransactions();renderBudgets();renderSavings();renderReport();renderAnalytics()}

function renderDashboard(){
  const m=state.dashboardMonth,inc=income(m),exp=expenses(m),bal=inc-exp,rate=inc?Math.max(0,bal/inc*100):0;
  qs("#balance").textContent=money(bal);qs("#income").textContent=money(inc);qs("#expenses").textContent=money(exp);qs("#savingsRate").textContent=rate.toFixed(0)+"%";
  qs("#dashboardMonth").textContent=new Date(m+"-01T00:00:00").toLocaleDateString("en-US",{month:"long",year:"numeric"});
  qs("#todayText").textContent=new Date().toLocaleDateString("en-US",{weekday:"long",month:"long",day:"numeric",year:"numeric"});
  qs("#cashFlowLabel").textContent=new Date(m+"-01T00:00:00").toLocaleDateString("en-US",{month:"long"});
  qs("#incomeTrend").textContent=inc?"+ active":"—";qs("#expenseTrend").textContent=exp?`${txInMonth(m).filter(t=>t.type==="Expense").length} items`:"—";qs("#savingsTrend").textContent=rate>=20?"Healthy":rate>0?"Building":"Start saving";
  renderCashChart();renderDonut();renderDashboardBudgets();renderDashboardGoals();renderRecent();
}

function shiftDashboardMonth(delta){const d=new Date(state.dashboardMonth+"-01T00:00:00");d.setMonth(d.getMonth()+delta);state.dashboardMonth=monthKey(d);renderDashboard()}

function renderCashChart(){
  const canvas=qs("#cashFlowChart");if(!canvas)return;const ctx=canvas.getContext("2d");const days=new Date(Number(state.dashboardMonth.slice(0,4)),Number(state.dashboardMonth.slice(5))-0,0).getDate();const labels=[],ins=[],outs=[];
  for(let i=1;i<=days;i++){const key=`${state.dashboardMonth}-${pad(i)}`;labels.push(i);ins.push(sum(state.transactions.filter(t=>t.date===key&&t.type==="Income").map(t=>t.amount)));outs.push(sum(state.transactions.filter(t=>t.date===key&&t.type==="Expense").map(t=>t.amount)))}
  if(state.cashChart)state.cashChart.destroy();
  state.cashChart=new Chart(ctx,{type:"line",data:{labels,datasets:[{label:"Income",data:ins,borderColor:"#75d6a4",backgroundColor:"rgba(117,214,164,.08)",fill:true,tension:.35,pointRadius:0,borderWidth:2},{label:"Expenses",data:outs,borderColor:"#ff8585",backgroundColor:"rgba(255,133,133,.05)",fill:true,tension:.35,pointRadius:0,borderWidth:2}]},options:chartOptions(true)})
}

function renderDonut(){
  const map=categoryTotals(),entries=Object.entries(map).sort((a,b)=>b[1]-a[1]).slice(0,7),labels=entries.map(x=>x[0]),values=entries.map(x=>x[1]);qs("#donutTotal").textContent=money(sum(values));
  if(state.donutChart)state.donutChart.destroy();state.donutChart=new Chart(qs("#categoryChart"),{type:"doughnut",data:{labels,datasets:[{data:values,backgroundColor:["#f4f5f7","#8fb7ff","#75d6a4","#f4c86b","#c9a7ff","#ff9e9e","#8f969f"],borderWidth:0}]},options:{responsive:true,maintainAspectRatio:false,cutout:"76%",plugins:{legend:{display:false}}}});
  qs("#categoryLegend").innerHTML=entries.length?entries.map((x,i)=>`<div class="legend-item"><i class="legend-dot" style="--dot:${["#f4f5f7","#8fb7ff","#75d6a4","#f4c86b","#c9a7ff","#ff9e9e","#8f969f"][i]}"></i>${escape(x[0])} <b>${money(x[1])}</b></div>`).join(""):'<div class="empty">No expenses this month.</div>'
}

function chartOptions(y=true){return{responsive:true,maintainAspectRatio:false,interaction:{mode:"index",intersect:false},plugins:{legend:{labels:{color:getComputedStyle(document.body).getPropertyValue("--muted"),font:{size:10},boxWidth:8}}},scales:{x:{grid:{display:false},ticks:{color:getComputedStyle(document.body).getPropertyValue("--muted2"),font:{size:9}}},y:{display:y,grid:{color:getComputedStyle(document.body).getPropertyValue("--line")},ticks:{color:getComputedStyle(document.body).getPropertyValue("--muted2"),font:{size:9},callback:v=>shortMoney(v)}}}}}

function renderRecent(){
  const box=qs("#recentTransactions"),items=state.transactions.slice().sort((a,b)=>new Date(b.date)-new Date(a.date)).slice(0,6);box.innerHTML=items.length?items.map(t=>recentHTML(t)).join(""):'<div class="empty">No transactions yet. Add your first transaction.</div>'
}

function recentHTML(t){return `<div class="transaction-row"><div class="tx-icon">${t.type==="Income"?"↑":"↓"}</div><div class="tx-main"><strong>${escape(t.description||t.category)}</strong><small>${escape(t.category)} · ${escape(t.paymentMethod||"Cash")}</small></div><div class="tx-date">${dateText(t.date)}</div><div class="tx-amount ${t.type==="Income"?"income-text":"expense-text"}">${t.type==="Income"?"+":"−"}${money(t.amount)}</div><button class="action-btn" onclick="editTransaction(${t.id})">Edit</button></div>`}
