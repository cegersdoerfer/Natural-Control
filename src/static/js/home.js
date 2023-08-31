function toggleLightSwitch(element) {
    const isChecked = element.checked;
    fetch('/switch', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        lightSwitch: isChecked
      })
    })
      .then(response => response.json())
      .then(data => {
        val = data.success;
        if (val == true) {
            console.log('Success:', data);
            }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

function submitBrightnessVal() {
    const brightnessVal = document.getElementById("brightness").value;
    fetch('/brightness', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        brightness: brightnessVal
      })
    })
      .then(response => response.json())
      .then(data => {
        val = data.success;
        if (val == true) {
            console.log('Success:', data);
            }
      })
      .catch(error => {
        console.error('Error:', error);
      });
      /* set slider value to brightnessVal */
      document.getElementById("brightness").innerHTML = brightnessVal;
  }

