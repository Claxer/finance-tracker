document.addEventListener("DOMContentLoaded", init);

function init(){
  state.transactions=state.transactions.map(normalizeTransaction);
  setupNavigation();
  setupUI();
  setupForms();
  setupFilters();
  setupSettings();
  setupImportExport();
  populateCategories();
  applyTheme(state.theme);
  setTodayDefaults();
  renderAll();
}

window.editTransaction=editTransaction;
window.deleteTransaction=deleteTransaction;
window.deleteBudget=deleteBudget;
window.deleteGoal=deleteGoal;
window.addToGoal=addToGoal;
