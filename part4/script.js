document.addEventListener('DOMContentLoaded', () => {
    const pathname = window.location.pathname;

  if (pathname.endsWith('/index.html') || pathname.endsWith('/')) {
    getListPlaces();
  }

  const priceFilter= document.getElementById('price-filter');
  if (priceFilter){
    priceFilter.addEventListener('change', filter);
  }

  const loginForm = document.getElementById('login-form');

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();

          const email = document.getElementById('email').value;
          const password = document.getElementById('password').value;

          try {
              const response = await fetch('http://localhost:5000/api/v1/auth/login', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({ email, password })
              });

              if (response.ok) {
                  const data = await response.json();

                  document.cookie = `token=${data.access_token}; path=/`;

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
      //loginForm.appendChild(errorContainer);
  }
  errorContainer.textContent = message;
}

async function getListPlaces() {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data);
            displayPlaces(data);
        } else {
            const errorData = await response.json();
            displayError(`No places found: ${errorData.message || response.statusText}`);
        }
    } catch (error) {
        displayError('An error occurred. Please try again later.');
    }
}

function displayPlaces(places) {
    for (const place of places.places) {
        console.log(place);
        const placecard = document.createElement('div');
        placecard.className='place-card';
        placecard.setAttribute('data-price', place.price);
        document.getElementById('places-list').appendChild(placecard);

        const logementName=document.createElement('h1');
        const logementNameText=document.createTextNode(place.title);
        logementName.appendChild(logementNameText);
        placecard.appendChild(logementName);

        const logementPrice=document.createElement('p');
        const logementPriceText=document.createTextNode('Price per night $' + place.price);
        logementPrice.appendChild(logementPriceText);
        placecard.appendChild(logementPrice);

        const logementButton=document.createElement('button');
        const logementButtonText=document.createTextNode('View Details');
        logementButton.appendChild(logementButtonText);
        logementButton.setAttribute('type', 'button');
        logementButton.setAttribute('class', 'button');
        const url= 'place.html?placeid=' + place.id;
        logementButton.setAttribute('onclick', `window.location.href=${url}`);
        placecard.appendChild(logementButton);


    }   
}

function filter() {
    let maxPrice = document.getElementById('price-filter').value;

    if (maxPrice !== 'all') {
        maxPrice = Number(maxPrice);
    }

 const places = document.getElementsByClassName('place-card');
 for (const place of places) {
    const price = Number(place.getAttribute('data-price'));
    if (maxPrice === 'all') {
        place.style.display = 'block';
    } else {
        if (price <= maxPrice) {
            place.style.display = 'block';
        } else {
            place.style.display = 'none';
        }
    }
 }
}
