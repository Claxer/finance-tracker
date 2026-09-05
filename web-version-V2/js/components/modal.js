function openModal(id){
  if(id==="transactionModal"){resetTransactionForm();populateCategories()}
  qs("#modalBackdrop").classList.add("open");qsa(".modal").forEach(m=>m.style.display=m.id===id?"block":"none");
  setTimeout(()=>{const first=qs("#"+id+" input:not([type=hidden])");first?.focus()},80)
}

function closeModals(){qs("#modalBackdrop").classList.remove("open");qsa(".modal").forEach(m=>m.style.display="none")}
