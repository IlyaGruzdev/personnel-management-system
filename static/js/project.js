window.addEventListener('load', function() {
  var messages = document.querySelector('.messages-content');
  var d, m, i = 0;

  function scrollToBottom() {
    messages.scrollTo(0, messages.scrollHeight);
  }

  function setDate() {
    d = new Date();
    if (m !== d.getMinutes()) {
      m = d.getMinutes();
      var timestamp = document.createElement('div');
      timestamp.className = 'timestamp';
      timestamp.textContent = d.getHours() + ':' + m;
      messages.appendChild(timestamp);
    }
  }

  function insertMessage(msg) {
    if (msg.trim() === '') {
      return false;
    }
    var newMessage = document.createElement('div');
    newMessage.className = 'message message-personal new';
    newMessage.textContent = msg;
    messages.appendChild(newMessage);
    setDate();
    document.querySelector('.message-input').value = '';
    scrollToBottom();
    setTimeout(function() {
      fakeMessage();
    }, 1000 + (Math.random() * 20) * 100);
  }

  document.querySelector('.message-submit').addEventListener('click', function() {
    insertMessage(document.querySelector('.message-input').value);
  });

  window.addEventListener('keydown', function(e) {
    if (e.which === 13) {
      insertMessage(document.querySelector('.message-input').value);
      return false;
    }
  });

  var Fake = [
    'Hi there, I\'m Fabio and you?',
    'Nice to meet you',
    'How are you?',
    'Not too bad, thanks',
    'What do you do?',
    'That\'s awesome',
    'Codepen is a nice place to stay',
    'I think you\'re a nice person',
    'Why do you think that?',
    'Can you explain?',
    'Anyway I\'ve gotta go now',
    'It was a pleasure to chat with you',
    'Time to make a new codepen',
    'Bye',
    ':)'
  ];

  function fakeMessage() {
    var messageInput = document.querySelector('.message-input').value;
    if (messageInput !== '') {
      return false;
    }
    var loadingMessage = document.createElement('div');
    loadingMessage.className = 'message loading new';
    loadingMessage.innerHTML = '<figure class="avatar"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80.jpg" /></figure><span></span>';
    messages.appendChild(loadingMessage);
    scrollToBottom();

    setTimeout(function() {
      var loading = document.querySelector('.message.loading');
      if (loading) {
        loading.remove();
      }
      var newMessage = document.createElement('div');
      newMessage.className = 'message new';
      newMessage.innerHTML = '<figure class="avatar"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80.jpg" /></figure>' + Fake[i];
      messages.appendChild(newMessage).classList.add('new');
      setDate();
      scrollToBottom();
      i++;
    }, 1000 + (Math.random() * 20) * 100);
  }

  scrollToBottom();
  setTimeout(function() {
    fakeMessage();
  }, 100);
});