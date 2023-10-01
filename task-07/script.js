var button = document.querySelector('.button');
var inputb = document.querySelector('.inputb');
var description = document.querySelector('.description');
var temperature = document.querySelector('.temperature');

button.addEventListener('click', function () {
  if (inputb.value.trim() !== '') {
    fetch('http://api.openweathermap.org/data/2.5/weather?q=' + inputb.value + '&appid=6c2cada2d128866e70a0f496a3191aa4')
      .then(response => response.json())
      .then(data => {
        var descriptionValue = data['weather'][0]['description'];
        var temperatureValue = data['main']['temp'];

        temperature.innerHTML = (temperatureValue - 273).toFixed(2);
        description.innerHTML = descriptionValue;
      })
      .catch(error => alert("Error! Unable to check weather data"));
  } else {
    description.innerHTML = "Please enter a location.";
  }
});
