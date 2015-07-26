// ------------------- LED ---------------------------
function ajax_getLEDChange(callback, onOff) {
	printlnMessage('messages', "ajax_getLEDChange() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxLEDChangeRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxLEDChangeRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxLEDChangeRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxLEDChangeRequest.onreadystatechange = callback;
	var requeststring;
	if (onOff == "0")
		requeststring = "ledChanger.php?led=2&onOff=0";
	else
		requeststring = "ledChanger.php?led=2&onOff=1";

	printlnMessage('messages', requeststring);
	ajaxLEDChangeRequest.open("GET", encodeURI(requeststring), true);
	ajaxLEDChangeRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_getLEDChange() {
	if (ajaxLEDChangeRequest.readyState == 4) {
		LEDChangeAjax = ajaxLEDChangeRequest.responseText;
		printlnMessage('messages', LEDChangeAjax);
		// LEDChangeJSON = JSON.parse(LEDChangeAjax);
		// printlnMessage('messages',LEDChangeJSON.username);
	}
}
