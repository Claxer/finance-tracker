function renderReport(){
  const m=state.reportMonth,inc=income(m),exp=expenses(m),n=inc-exp,rate=inc?n/inc*100:0,arr=txInMonth(m),ex=arr.filter(t=>t.type==="Expense"),avg=ex.length?sum(ex.map(t=>t.amount))/ex.length:0,largest=ex.slice().sort((a,b)=>b.amount-a.amount)[0];
  qs("#reportMonth").value=m;qs("#reportNet").textContent=money(n);qs("#reportIncome").textContent=money(inc);qs("#reportExpenses").textContent=money(exp);qs("#reportSavingsRate").textContent=rate.toFixed(0)+"%";
  qs("#reportNarrative").textContent=!arr.length?"No activity recorded for this month.":n>=0?`You kept ${money(n)} after expenses this month.`:`You spent ${money(Math.abs(n))} more than you received this month.`;
  const cats=Object.entries(categoryTotals(m)).sort((a,b)=>b[1]-a[1]);
  qs("#reportCategories").innerHTML=cats.length?cats.slice(0,7).map((x,i)=>`<div class="rank-item"><div class="rank-num">${i+1}</div><div><strong>${escape(x[0])}</strong><small>${(x[1]/(exp||1)*100).toFixed(0)}% of expenses</small></div><b>${money(x[1])}</b></div>`).join(""):'<div class="empty">No expenses this month.</div>';
  qs("#reportDetails").innerHTML=`<div class="detail-item"><span>Transactions</span><b>${arr.length}</b></div><div class="detail-item"><span>Expense transactions</span><b>${ex.length}</b></div><div class="detail-item"><span>Average expense</span><b>${money(avg)}</b></div><div class="detail-item"><span>Largest expense</span><b>${largest?money(largest.amount):"₱0"}</b></div><div class="detail-item"><span>Highest category</span><b>${cats[0]?escape(cats[0][0]):"—"}</b></div>`
}

function shiftReportMonth(delta){const d=new Date(state.reportMonth+"-01T00:00:00");d.setMonth(d.getMonth()+delta);state.reportMonth=monthKey(d);renderReport()}
