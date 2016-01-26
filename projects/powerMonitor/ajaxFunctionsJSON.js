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
				ajaxGetValuesRequestJSON = new ActiveXObject(
						"Microsoft.XMLHTTP");
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
	// printlnMessage('messages', requeststring);
	ajaxGetValuesRequestJSON.open("GET", encodeURI(requeststring), true);
	ajaxGetValuesRequestJSON.send(null);

}

// Create a function that will receive data sent from the server
function ajaxCalled_getValues() {
	if (ajaxGetValuesRequestJSON.readyState == 4) {
		// printlnMessage('messages', "ajaxCalled_getValues()");
		getValuesAjaxJSON = ajaxGetValuesRequestJSON.responseText;
		// printlnMessage('messages', "response from PHP and python:");
		printMessage('messages', getValuesAjaxJSON);
	}
}

function ajax_createDB() {
	// printlnMessage('messages','ajax_createDB() called');
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxDBRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxDBRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxDBRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxDBRequest.onreadystatechange = ajaxCalled_createDB;
	myParams = {
		login : loginDB
	};
	var requeststring;
	requeststring = "DBCreate.php?&json=" + JSON.stringify(myParams);
	ajaxDBRequest.open("POST", encodeURI(requeststring), true);
	// printlnMessage('messages',requeststring);
	ajaxDBRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_createDB() {
	if (ajaxDBRequest.readyState == 4) {
		DBAjax = ajaxDBRequest.responseText;
		printlnMessage('messages', DBAjax);
	}
}

function ajax_saveValues() {
	printlnMessage('messages', "ajax_saveValues() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxsaveValuesRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxsaveValuesRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxsaveValuesRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxsaveValuesRequest.onreadystatechange = ajaxCalled_saveValues;
	myParams = {
		testparam : 'abc'
	};
	var requeststring;
	requeststring = "DBFunctions.php?json=" + JSON.stringify(myParams);
	printlnMessage('messages', requeststring);
	ajaxsaveValuesRequest.open("POST", encodeURI(requeststring), true);
	ajaxsaveValuesRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_saveValues() {
	if (ajaxsaveValuesRequest.readyState == 4) {

		// printlnMessage('messages',"ajaxCalled_saveValues called");
		ValuesAjax = ajaxsaveValuesRequest.responseText;
		printlnMessage('messages', ValuesAjax);

	}
}
