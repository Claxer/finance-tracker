function setupNavigation(){
  qsa(".nav-btn").forEach(b=>b.addEventListener("click",()=>showPage(b.dataset.page)));
  qsa("[data-page-link]").forEach(b=>b.addEventListener("click",()=>showPage(b.dataset.pageLink)));
}

function showPage(page){
  qsa(".page").forEach(p=>p.classList.toggle("active-page",p.id===page));
  qsa(".nav-btn").forEach(b=>b.classList.toggle("active",b.dataset.page===page));
  const names={dashboard:"Overview",transactions:"Transactions",budgets:"Budgets",savings:"Savings",reports:"Reports",analytics:"Analytics",settings:"Settings"};
  qs("#pageTitle").textContent=names[page]||"Finance";
  closeSidebar();
  if(page==="analytics")renderAnalytics();
  if(page==="reports")renderReport();
}

function setupUI(){
  qs("#globalAddBtn").onclick=()=>openModal("transactionModal");
  qs("#transactionsAddBtn").onclick=()=>openModal("transactionModal");
  qs("#budgetAddBtn").onclick=()=>openModal("budgetModal");
  qs("#goalAddBtn").onclick=()=>openModal("goalModal");
  qs("#prevMonth").onclick=()=>shiftDashboardMonth(-1);qs("#nextMonth").onclick=()=>shiftDashboardMonth(1);
  qs("#reportPrev").onclick=()=>shiftReportMonth(-1);qs("#reportNext").onclick=()=>shiftReportMonth(1);
  qs("#themeToggle").onclick=()=>applyTheme(state.theme==="dark"?"light":"dark");
  qs("#openSidebar").onclick=openSidebar;qs("#closeSidebar").onclick=closeSidebar;qs("#backdrop").onclick=closeSidebar;
  qsa(".close-modal").forEach(b=>b.onclick=closeModals);
  qs("#modalBackdrop").addEventListener("click",e=>{if(e.target.id==="modalBackdrop")closeModals()});
  qsa("[data-tx-type]").forEach(b=>b.onclick=()=>{state.txType=b.dataset.txType;qsa("[data-tx-type]").forEach(x=>x.classList.toggle("active",x===b))});
}
