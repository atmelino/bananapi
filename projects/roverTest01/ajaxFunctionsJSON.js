
function ajax_setSpeedJSON(myParams) {
	// printlnMessage('messages', "ajax_setSpeedJSON() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxStepperSpeedRequestJSON = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxStepperSpeedRequestJSON = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxStepperSpeedRequestJSON = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxStepperSpeedRequestJSON.onreadystatechange = ajaxCalled_setSpeedJSON;
	// printlnMessage('messages', JSON.stringify(myParams));
	var requeststring;
	requeststring = "stepperFunctionsJSON.php?json=" + JSON.stringify(myParams);
	printlnMessage('messages', requeststring);
	ajaxStepperSpeedRequestJSON.open("GET", encodeURI(requeststring), true);
	ajaxStepperSpeedRequestJSON.send(null);

}

// Create a function that will receive data sent from the server
function ajaxCalled_setSpeedJSON() {
	if (ajaxStepperSpeedRequestJSON.readyState == 4) {
		//printlnMessage('messages', "ajaxCalled_setSpeedJSON()");
		stepperSpeedAjaxJSON = ajaxStepperSpeedRequestJSON.responseText;
		printlnMessage('messages', "response from PHP and python:");
		printlnMessage('messages', stepperSpeedAjaxJSON);
	}
}
