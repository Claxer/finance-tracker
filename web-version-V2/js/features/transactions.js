function setupForms(){
  qs("#transactionForm").onsubmit=e=>{e.preventDefault();saveTransaction()};
  qs("#budgetForm").onsubmit=e=>{e.preventDefault();saveBudget()};
  qs("#goalForm").onsubmit=e=>{e.preventDefault();saveGoal()};
}

function setTodayDefaults(){qs("#transactionDate").value=today();qs("#reportMonth").value=state.reportMonth}

function resetTransactionForm(){
  qs("#transactionForm").reset();qs("#editTransactionId").value="";qs("#transactionModalTitle").textContent="Add transaction";qs("#modalEyebrow").textContent="NEW TRANSACTION";qs("#saveTransactionBtn").textContent="Save transaction";qs("#transactionDate").value=today();state.txType="Expense";qsa("[data-tx-type]").forEach((x,i)=>x.classList.toggle("active",i===0))
}

function saveTransaction(){
  const amount=Number(qs("#transactionAmount").value);if(!amount||amount<=0)return toast("Enter a valid amount.");
  const id=qs("#editTransactionId").value;
  const item=normalizeTransaction({id:id?Number(id):undefined,type:state.txType,amount,category:qs("#transactionCategory").value,description:qs("#transactionDescription").value.trim(),date:qs("#transactionDate").value,paymentMethod:qs("#paymentMethod").value,recurring:qs("#recurringTransaction").checked});
  if(id){const i=state.transactions.findIndex(t=>String(t.id)===String(id));if(i>=0)state.transactions[i]=item;toast("Transaction updated.")}else{state.transactions.unshift(item);toast("Transaction added.")}
  save(KEYS.transactions,state.transactions);closeModals();renderAll()
}

function editTransaction(id){
  const t=state.transactions.find(x=>String(x.id)===String(id));if(!t)return;
  openModal("transactionModal");qs("#editTransactionId").value=t.id;qs("#transactionModalTitle").textContent="Edit transaction";qs("#modalEyebrow").textContent="EDIT TRANSACTION";qs("#saveTransactionBtn").textContent="Update transaction";
  state.txType=t.type;qsa("[data-tx-type]").forEach(x=>x.classList.toggle("active",x.dataset.txType===t.type));populateCategories();qs("#transactionAmount").value=t.amount;qs("#transactionCategory").value=t.category;qs("#transactionDate").value=t.date;qs("#paymentMethod").value=t.paymentMethod||"Cash";qs("#transactionDescription").value=t.description||"";qs("#recurringTransaction").checked=!!t.recurring
}

function deleteTransaction(id){if(!confirm("Delete this transaction?"))return;state.transactions=state.transactions.filter(t=>String(t.id)!==String(id));save(KEYS.transactions,state.transactions);toast("Transaction deleted.");renderAll()}
