function ajax_getValues(myParams) {
	// printlnMessage('messages', "ajax_getValues() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxGetValuesRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxGetValuesRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxGetValuesRequest = new ActiveXObject(
						"Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxGetValuesRequest.onreadystatechange = ajaxCalled_getValues;
	// printlnMessage('messages', JSON.stringify(myParams));
	var requeststring;
	requeststring = "getValues.php?json=" + JSON.stringify(myParams);
	// printlnMessage('messages', requeststring);
	ajaxGetValuesRequest.open("GET", encodeURI(requeststring), true);
	ajaxGetValuesRequest.send(null);

}

// Create a function that will receive data sent from the server
function ajaxCalled_getValues() {
	if (ajaxGetValuesRequest.readyState == 4) {
		// printlnMessage('messages', "ajaxCalled_getValues()");
		getValuesAjax = ajaxGetValuesRequest.responseText;
		// printlnMessage('messages', "response from PHP and python:");
		//printMessage('messages', getValuesAjax);
		getValuesAjaxJSON = JSON.parse(getValuesAjax);
		//printMessage('messages', getValuesAjaxJSON.bv3);
		//part1 = sprintf('%s ',getValuesAjaxJSON.date);


		part1=new Date().toLocaleString()+' ';
		part2 = sprintf('%7.2f ',parseFloat(getValuesAjaxJSON.bv3));
		part3 = sprintf('%6.2f ',parseFloat(getValuesAjaxJSON.cmA3));
		part4 = sprintf('%8.2f ',parseFloat(getValuesAjaxJSON.pw3));
		var printstring = part1+part2+part3+part4;
		printlnMessage('messages', printstring);

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
