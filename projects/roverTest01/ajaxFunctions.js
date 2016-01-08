function ajax_setSpeed(callback, wheel, speed) {
	// printlnMessage('messages', "ajax_setSpeed() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxStepperSpeedRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxStepperSpeedRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxStepperSpeedRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxStepperSpeedRequest.onreadystatechange = callback;
	var requeststring;
	requeststring = "stepperFunctions.php?wheel=" + wheel + "&speed=" + speed;

	printlnMessage('messages', requeststring);
	ajaxStepperSpeedRequest.open("GET", encodeURI(requeststring), true);
	ajaxStepperSpeedRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_setSpeed() {
	if (ajaxStepperSpeedRequest.readyState == 4) {
		//printlnMessage('messages', "ajaxCalled_setSpeed()");
		stepperSpeedAjax = ajaxStepperSpeedRequest.responseText;
		printlnMessage('messages', "response from python:");
		printlnMessage('messages', stepperSpeedAjax);
	}
}
