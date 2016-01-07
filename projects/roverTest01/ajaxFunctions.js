// ------------------- LED ---------------------------
function ajax_setSpeed(callback, speed) {
	//printlnMessage('messages', "ajax_setSpeed() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxStepperPositionRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxStepperPositionRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxStepperPositionRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxStepperPositionRequest.onreadystatechange = callback;
	var requeststring;
		requeststring = "stepperFunctions.php?wheel=lf&speed="+speed;

	printlnMessage('messages', requeststring);
	ajaxStepperPositionRequest.open("GET", encodeURI(requeststring), true);
	ajaxStepperPositionRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_setPosition() {
	if (ajaxStepperPositionRequest.readyState == 4) {
		stepperPositionAjax = ajaxStepperPositionRequest.responseText;
		printlnMessage('messages', stepperPositionAjax);
		// stepperPositionJSON = JSON.parse(stepperPositionAjax);
		// printlnMessage('messages',stepperPositionJSON.username);
	}
}
