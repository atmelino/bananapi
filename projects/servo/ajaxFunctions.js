// ------------------- LED ---------------------------
function ajax_setPosition(callback, angle) {
	printlnMessage('messages', "ajax_setPosition() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxServoPositionRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxServoPositionRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxServoPositionRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxServoPositionRequest.onreadystatechange = callback;
	var requeststring;
		requeststring = "servoFunctions.php?led=2&angle="+angle;

	printlnMessage('messages', requeststring);
	ajaxServoPositionRequest.open("GET", encodeURI(requeststring), true);
	ajaxServoPositionRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_setPosition() {
	if (ajaxServoPositionRequest.readyState == 4) {
		servoPositionAjax = ajaxServoPositionRequest.responseText;
		printlnMessage('messages', servoPositionAjax);
		// servoPositionJSON = JSON.parse(servoPositionAjax);
		// printlnMessage('messages',servoPositionJSON.username);
	}
}
