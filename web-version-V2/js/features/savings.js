function saveGoal(){const name=qs("#goalName").value.trim(),target=Number(qs("#goalTarget").value),savedAmount=Number(qs("#goalSaved").value)||0;if(!name||!target||target<=0)return toast("Complete the goal details.");state.savings.push({id:Date.now(),name,target,saved:Math.min(savedAmount,target),targetDate:qs("#goalDate").value||""});save(KEYS.savings,state.savings);closeModals();toast("Savings goal created.");renderAll()}

function addToGoal(id,input){const v=Number(input.value);const g=state.savings.find(x=>x.id===id);if(!g||!v||v<=0)return toast("Enter a valid savings amount.");g.saved=Math.min(g.target,g.saved+v);save(KEYS.savings,state.savings);toast(g.saved>=g.target?"Goal completed!":"Savings added.");renderAll()}

function deleteGoal(id){if(!confirm("Delete this savings goal?"))return;state.savings=state.savings.filter(g=>g.id!==id);save(KEYS.savings,state.savings);toast("Goal deleted.");renderAll()}

function renderDashboardGoals(){
  const box=qs("#dashboardGoals");if(!state.savings.length){box.innerHTML='<div class="empty">No savings goals yet.</div>';return}
  box.innerHTML=state.savings.slice(0,3).map(g=>`<div class="stack-item"><div class="stack-top"><strong>${escape(g.name)}</strong><span>${Math.min(100,g.target?g.saved/g.target*100:0).toFixed(0)}%</span></div><div class="progress good"><i style="width:${Math.min(100,g.target?g.saved/g.target*100:0)}%"></i></div></div>`).join("")
}

function renderSavings(){
  const saved=sum(state.savings.map(g=>g.saved)),target=sum(state.savings.map(g=>g.target));qs("#totalSaved").textContent=money(saved);qs("#totalTarget").textContent=money(target);qs("#overallGoalProgress").textContent=(target?saved/target*100:0).toFixed(0)+"%";
  qs("#savingsGoalsList").innerHTML=state.savings.length?state.savings.map(g=>{const pct=g.target?Math.min(100,g.saved/g.target*100):0;return `<article class="goal-card"><div class="card-title"><div><h3>${escape(g.name)}</h3><span class="subtle">${g.targetDate?"Target "+dateText(g.targetDate):"No target date"}</span></div><button class="action-btn" onclick="deleteGoal(${g.id})">Delete</button></div><div class="amount-pair"><div><span>Saved</span><strong>${money(g.saved)}</strong></div><div><span>Target</span><strong>${money(g.target)}</strong></div><div><span>Remaining</span><strong>${money(Math.max(0,g.target-g.saved))}</strong></div></div><div class="progress good"><i style="width:${pct}%"></i></div><div class="card-footer"><span>${pct.toFixed(0)}% complete</span><span>${g.saved>=g.target?"Completed":"In progress"}</span></div><div class="goal-actions"><input id="goal-add-${g.id}" type="number" min="0.01" step="0.01" placeholder="Amount"><button class="primary-btn" onclick="addToGoal(${g.id},document.getElementById('goal-add-${g.id}'))">+ Add</button></div></article>`}).join(""):'<div class="empty panel">No savings goals yet. Create one to start tracking progress.</div>'
}
