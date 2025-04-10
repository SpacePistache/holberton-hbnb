document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();

          const email = document.getElementById('email').value;
          const password = document.getElementById('password').value;

          try {
              const response = await fetch('https://your-api-url/login', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({ email, password })
              });

              if (response.ok) {
                  const data = await response.json();
                  
                  // Set cookie (secure, path=/, expires in 1 day)
                  document.cookie = `token=${data.access_token}; path=/; max-age=86400`;

                  // Redirect to main page
                  window.location.href = 'index.html';
              } else {
                  const errorData = await response.json();
                  displayError(`Login failed: ${errorData.message || response.statusText}`);
              }
          } catch (error) {
              displayError('An error occurred. Please try again later.');
              console.error('Login Error:', error);
          }
      });
  }
});


function displayError(message) {
  let errorContainer = document.getElementById('error-message');
  if (!errorContainer) {
      errorContainer = document.createElement('div');
      errorContainer.id = 'error-message';
      errorContainer.style.color = 'red';
      loginForm.appendChild(errorContainer);
  }
  errorContainer.textContent = message;
}
