// Select all <button> elements
const buttons = document.querySelectorAll('button');

// Loop through each button and add a click event listener
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function () {
    // Log the text of the clicked button
    console.log(this.textContent);
  });
}
