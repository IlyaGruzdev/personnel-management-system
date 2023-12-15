  var selectField = document.getElementsByClassName("selector");
  var dropdown_items = document.getElementsByClassName("dropdown-cont-item");
  var dropdown_content = document.getElementById("dropdown-content"); 
  selectField[0].onclick = function()
  {
    document.getElementById("dropdown-content_1").classList.toggle("hide");
  }
  selectField[1].onclick = function()
  {
    document.getElementById("dropdown-content_2").classList.toggle("hide");
  }
  selectField[2].onclick = function()
  {
    document.getElementById("dropdown-content_3").classList.toggle("hide");
  }
  for (item of dropdown_items)
  {
    item.onclick = function()
    { 
      this.parentNode.parentNode.querySelector(".selector > div").innerText = this.innerText;
    } 
   
  }

  function showRegisterForm() {
    var elementsToHide = document.querySelectorAll("body > *:not(#navbar_navbar_inverse):not(#register_form)");
    elementsToHide.forEach(function(element) {
        element.style.display = "none";
    });

    var navbar = document.getElementById("navbar_navbar_inverse");
    if(navbar) {
        navbar.style = navbar.style.display +"block";
    } else {
        // В случае, если элемент не найден, вы можете попробовать обратиться к нему через класс или другой способ и отобразить его
        console.log("Элемент с id 'navbar_navbar-inverse' не найден.");
    }
    document.querySelector("header").style.display="block";
    document.getElementById("register_form").style.display = "block";
    document.body.style="background-color: black";
    var savedUsername = localStorage.getItem('username');
    var savedEmail = localStorage.getItem('email');
    var savedPassword = localStorage.getItem('password');
    var savedConfirmPassword = localStorage.getItem('confirm_password');
    var savedLogin = localStorage.getItem('login');
    var savedLogPassword = localStorage.getItem('logpassword');
    var remember = localStorage.getItem('remember');
  
  // Устанавливаем значения в поля форм
  signedUpForm.querySelector('#id_username').value = savedUsername||"";
  signedUpForm.querySelector('#id_email').value = savedEmail||"";
  signedUpForm.querySelector('#id_password').value = savedPassword||"";
  signedUpForm.querySelector('#id_confirm_password').value = savedConfirmPassword||"";
  signedInForm.querySelector('#id_login').value = savedLogin||"";
  signedInForm.querySelector('#id_password').value = savedLogPassword||"";
  signedInForm.querySelector('#checkbox').checked = remember||false;
}