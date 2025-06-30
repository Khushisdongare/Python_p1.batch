const button = document.getElementById('countBtn');
const counterSpan = document.getElementById('clickCount');
let count = 0;

// First listener: Increase the visible counter
button.addEventListener('click', function () {
  count++;
  counterSpan.textContent = count;
});

// Second listener: Log event details
button.addEventListener('click', function (event) {
  console.log('Event Type:', event.type);
  console.log('Time Stamp:', event.timeStamp);
  console.log('Element Tag Name:', this.tagName); // 'BUTTON'
});
