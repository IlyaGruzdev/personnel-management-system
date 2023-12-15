
var j = jQuery.noConflict();

// Получаем ссылки на формы и кнопки
var signedInForm = document.querySelector('#myform-signin');
var signedUpForm = document.querySelector('#myform-signup');
var signedInButton = document.querySelector('.signedin-active');
var signedUpButton = document.querySelector('.signedup-inactive');

signedUpForm.style.display = 'none'; 
signedInButton.addEventListener('click', function() {
  signedUpForm.style.display = 'none';  // Скрываем форму входа
  signedInForm.style.display = "block"// Показываем форму входа
});

signedUpButton.addEventListener('click', function() {
  signedInForm.style.display = "none"// Показываем форму входа
  signedUpForm.style.display = "block"; // Показываем форму регистрации
});

$(function() {
	$(".btn").click(function() {
		$(".form-signin").toggleClass("form-signin-left");
    $(".form-signup").toggleClass("form-signup-left");
    $(".signup-inactive").toggleClass("signup-active");
    $(".signin-active").toggleClass("signin-inactive");
    $(".forgot").toggleClass("forgot-left");   
    $(this).removeClass("idle").addClass("active");
	});
});

$(function() {
	$(".btn-signedin").click(function() {
  $(".btn-animate").toggleClass("btn-animate-grow");
  $(".welcome").toggleClass("welcome-left");
  $(".cover-photo").toggleClass("cover-photo-down");
  $(".profile-photo").toggleClass("profile-photo-down");
  $(".btn-goback").toggleClass("btn-goback-up");
  $(".forgot").toggleClass("forgot-fade");
	});
});
document.getElementById('myform-signup').addEventListener('submit', function(event) {
 
  var formData = new FormData(this);

  fetch('/', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    var messagesContainer = document.querySelector('.regmessages');
    messagesContainer.innerHTML = ''; // Очистка контейнера от предыдущих сообщений

    if (data.hasOwnProperty('error')) {
      messagesContainer.style.display="block";
      localStorage.setItem('username', document.getElementById('id_username').value);
      localStorage.setItem('email', document.getElementById('id_email').value);
      localStorage.setItem('password', document.getElementById('id_password').value);
      localStorage.setItem('confirm_password', document.getElementById('id_confirm_password').value);
      var error = data.error+'\n';
      var errorElement = document.createElement('li'); // Создаем новый элемент для каждой ошибки
      errorElement.style="color: black; font-size: 15px";
      errorElement.textContent = error; 
      messagesContainer.appendChild(errorElement);
    }
    if(data.hasOwnProperty('errors'))
    {
    messagesContainer.style.display="block";
    console.log(data);
    for (var i = 0; i < data.errors.__all__.length; i++) {
      var error = data.errors.__all__[i]+'\n';
      var errorElement = document.createElement('li'); // Создаем новый элемент для каждой ошибки
      errorElement.style="color: black; font-size: 15px";
      errorElement.textContent = error; // Устанавливаем текст ошибки в элемент
      messagesContainer.appendChild(errorElement); // Добавляем элемент с ошибкой в контейнер
    }
  }
     else if(data.hasOwnProperty('message')){
      localStorage.removeItem('username');
      localStorage.removeItem('email');
      localStorage.removeItem('password');
      localStorage.removeItem('confirm_password')
      history.go();
    }
  })
  .catch(function(error) {
    console.log('Произошла ошибка: ' + error.message);
  });

  event.preventDefault();
});
document.getElementById('myform-signin').addEventListener('submit', function(event) {
  var loginElement = document.querySelector('#id_login');
  var passwordElement = document.querySelector('#logpassword');
  var checkboxElement = document.querySelector('#checkbox');

  var formData = new FormData(this);

  fetch('/', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    var messagesContainer = document.querySelector('.logmessages');
    messagesContainer.innerHTML = ''; // Очистка контейнера от предыдущих сообщений
    if (data.hasOwnProperty('error')) {
      messagesContainer.style.display="block";
      localStorage.setItem('login', loginElement.value);
      localStorage.setItem('logpassword', passwordElement.value);
      localStorage.setItem('remember', checkboxElement.value);
      var error = data.error+'\n';
      var errorElement = document.createElement('li'); // оздаем новый элемент для каждой ошибки
      errorElement.style="color: black; font-size: 15px";
      errorElement.textContent = error; 
      messagesContainer.appendChild(errorElement);
    }
    if(data.hasOwnProperty('errors'))
    {
      messagesContainer.style.display="block";
      console.log(data);
      for (var i = 0; i < data.errors.__all__.length; i++) {
        var error = data.errors.__all__[i]+'\n';
        var errorElement = document.createElement('li'); // Создаем новый элемент для каждой ошибки
        errorElement.style="color: black; font-size: 15px";
        errorElement.textContent = error; // Устанавливаем текст ошибки в элемент
        messagesContainer.appendChild(errorElement); // Добавляем элемент с ошибкой в контейнер
      }
    }
   
     else if(data.hasOwnProperty('message')){
      // Очищаем данные из localStorage
      localStorage.removeItem('login');
      localStorage.removeItem('logpassword');
      localStorage.removeItem('remember')
      history.go();
    }
  })
  .catch(function(error) {
    console.log('Произошла ошибка: ' + error.message);
  });

  // Отменяем стандартное поведение отправки формы
  event.preventDefault();
});