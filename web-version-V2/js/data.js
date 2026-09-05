function populateCategories(){
  const options=state.categories.map(c=>`<option>${escape(c)}</option>`).join("");
  ["transactionCategory","budgetCategory"].forEach(id=>{const e=qs("#"+id);if(e)e.innerHTML=options});
  const filter=qs("#categoryFilter");if(filter){const current=filter.value;filter.innerHTML='<option>All categories</option>'+state.categories.map(c=>`<option>${escape(c)}</option>`).join("");filter.value=current||"All categories"}
}

function setupFilters(){
  ["searchInput","typeFilter","categoryFilter","sortFilter"].forEach(id=>qs("#"+id).addEventListener(id==="searchInput"?"input":"change",renderTransactions));
  qs("#clearFilters").onclick=()=>{qs("#searchInput").value="";qs("#typeFilter").value="All types";qs("#categoryFilter").value="All categories";qs("#sortFilter").value="newest";renderTransactions()}
}
