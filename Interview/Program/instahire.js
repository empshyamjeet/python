const button = document.querySelector('.btn.btn-lg.btn-primary.new-btn');

// Function to click the button if it is not disabled
function clickButton() {
    if (!button.hasAttribute('disabled')) {
        button.click();
        console.log('Button clicked');
    } else {
        console.log('Button is disabled');
    }
}

// Run the function every 500 milliseconds (0.5 seconds)
const intervalId = setInterval(clickButton, 500);

// Stop the interval after 100 clicks
let clickCount = 0;
const maxClicks = 500;

const stopInterval = setInterval(() => {
    clickCount++;
    if (clickCount >= maxClicks) {
        clearInterval(intervalId);
        clearInterval(stopInterval);
        console.log('Stopped clicking after 100 times');
    }
}, 1000);
