document.addEventListener("DOMContentLoaded", function () {
    // Store the original content of the main section
    var originalMainContent = document.getElementById("mainSection").innerHTML;
  
    // Get references to the buttons and content sections
    const homeButton = document.querySelector('.homeButton');
    const chatButton = document.getElementById('chatButton');
    const calendarButton = document.getElementById('calendarButton');
    const journalButton = document.getElementById('journalButton');
    const musicButton = document.getElementById('musicButton');
    const musicClassicalButton = document.getElementById('musicClassicalButton');

    const mainSection = document.getElementById('mainSection');
    const chatSection = document.getElementById('chatSection');
    const calendarSection = document.getElementById('calendarSection');
    const journalSection = document.getElementById('journalSection');
    const musicSection = document.getElementById('musicSection');
    const musicClassicalSection = document.getElementById('musicClassicalSection');
  
    // Add click event listeners to the buttons
    homeButton.addEventListener('click', function () {
      resetState();
      mainSection.classList.add('home');
      mainSection.style.display = 'block'; // Make sure to show the home section
    });
  
    chatButton.addEventListener('click', function () {
      resetState();
      mainSection.classList.add('chat');
      chatSection.style.display = 'block';
    });
  
    calendarButton.addEventListener('click', function () {
      resetState();
      mainSection.classList.add('calendar');
      calendarSection.style.display = 'block';
    });
  
    journalButton.addEventListener('click', function () {
      resetState();
      mainSection.style.display = 'none';
      journalSection.style.display = 'block';
    });

    musicButton.addEventListener('click', function () {
      resetState();
      mainSection.style.display = 'none';
      musicSection.style.display = 'block';
    });

    musicClassicalButton.addEventListener('click', function () {
      resetState();
      mainSection.style.display = 'none';
      musicClassicalSection.style.display = 'block';
    });
  
    // Function to reset the state
    function resetState() {
      mainSection.style.display = 'none';
      chatSection.style.display = 'none';
      calendarSection.style.display = 'none';
      journalSection.style.display = 'none';
      musicSection.style.display = 'none';
      musicClassicalSection.style.display = 'none';
  
      mainSection.classList.remove('home', 'chat', 'calendar');
    }
  });
  