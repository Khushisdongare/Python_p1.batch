const buttons = document.querySelectorAll('button');

buttons.forEach((button) => {
  button.addEventListener('click', (event) => {
    console.log(this); // Logs the value of `this` inside the arrow function
  });
});
