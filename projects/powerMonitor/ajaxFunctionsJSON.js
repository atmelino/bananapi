
function ajax_getValues(myParams) {
	// printlnMessage('messages', "ajax_getValues() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxGetValuesRequestJSON = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxGetValuesRequestJSON = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxGetValuesRequestJSON = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxGetValuesRequestJSON.onreadystatechange = ajaxCalled_getValues;
	// printlnMessage('messages', JSON.stringify(myParams));
	var requeststring;
	requeststring = "getValuesJSON.php?json=" + JSON.stringify(myParams);
	//printlnMessage('messages', requeststring);
	ajaxGetValuesRequestJSON.open("GET", encodeURI(requeststring), true);
	ajaxGetValuesRequestJSON.send(null);

}

// Create a function that will receive data sent from the server
function ajaxCalled_getValues() {
	if (ajaxGetValuesRequestJSON.readyState == 4) {
		//printlnMessage('messages', "ajaxCalled_getValues()");
		getValuesAjaxJSON = ajaxGetValuesRequestJSON.responseText;
		//printlnMessage('messages', "response from PHP and python:");
		printlnMessage('messages', getValuesAjaxJSON);
	}
}
