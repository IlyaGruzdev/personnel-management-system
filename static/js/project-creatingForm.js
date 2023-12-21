var closeButton = document.getElementById('closebutton').onclick = function(){
  document.getElementById('creating_form').style.visibility="hidden";
}
var addBtn = document.getElementById('add-btn').onclick = function(){
  document.getElementById('creating_form').style.visibility="visible";
  document.getElementById('success-list').innerHTML = '';
  document.getElementById('error-list').innerHTML = '';
}
var selectSet = new Set(); // Переменная должна быть объявлена глобально, чтобы сохранить состояние множества между кликами

document.getElementById("id_personal_list").addEventListener("click", function(event) {
  const clickField = event.target;
  event.preventDefault();
  event.stopImmediatePropagation();
  if (clickField.classList.contains("changedField")) {
    clickField.classList.remove("changedField");
    selectSet.delete(clickField.textContent);
  } else {
    clickField.classList.add("changedField");
    selectSet.add(clickField.textContent);
  }
});

document.addEventListener("click", function(event) {
  const dropdown = document.getElementById("id_personal_list");
  if (!dropdown.contains(event.target)) {
    dropdown.blur(); // закрыть выпадающий список при клике вне его
  }
});
