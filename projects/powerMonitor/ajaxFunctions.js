function ajax_sendMessage(myParams) {
	// printlnMessage('messages', "ajax_sendMessage() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxsendMessageRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxsendMessageRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxsendMessageRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxsendMessageRequest.onreadystatechange = ajaxCalled_sendMessage;
	// printlnMessage('messages', JSON.stringify(myParams));
	var requeststring;
	requeststring = "powerMonitor.php?json=" + JSON.stringify(myParams);
	// printlnMessage('messages', requeststring);
	ajaxsendMessageRequest.open("GET", encodeURI(requeststring), true);
	ajaxsendMessageRequest.send(null);

}

// Create a function that will receive data sent from the server
function ajaxCalled_sendMessage() {
	if (ajaxsendMessageRequest.readyState == 4) {
		// printlnMessage('messages', "ajaxCalled_sendMessage()");
		sendMessageAjax = ajaxsendMessageRequest.responseText;
		// printlnMessage('messages', "response from PHP and python:");
		printMessage('messages', sendMessageAjax);
		// sendMessageAjaxJSON = JSON.parse(sendMessageAjax);
		// printMessage('messages', sendMessageAjaxJSON.bv3);
		// part1 = sprintf('%s ',sendMessageAjaxJSON.date);

	}
}

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
				ajaxGetValuesRequest = new ActiveXObject("Microsoft.XMLHTTP");
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
		// printMessage('messages', getValuesAjax);
		getValuesAjaxJSON = JSON.parse(getValuesAjax);
		// printMessage('messages', getValuesAjaxJSON.bv3);
		// part1 = sprintf('%s ',getValuesAjaxJSON.date);

		lV3 = getValuesAjaxJSON.lV3;
		cmA3 = getValuesAjaxJSON.cmA3;
		pw3 = getValuesAjaxJSON.pw3;
		part1 = new Date().toLocaleString() + ' ';
		part2 = sprintf('%7.2f ', parseFloat(lV3));
		part3 = sprintf('%6.2f ', parseFloat(cmA3));
		part4 = sprintf('%8.2f ', parseFloat(pw3));
		var printstring = part1 + part2 + part3 + part4;
		printlnMessage('messages', printstring);

		if (document.getElementById('saveSQL').checked) {
			// printlnMessage('messages', "save to database");

			myParams = {
				fs : 'saveValues',
				lV3 : lV3,
				cmA3 : cmA3,
				pw3 : pw3,
			};
			// printlnMessage('messages', JSON.stringify(myParams));
			// printlnMessage('messages', "save values clicked");
			ajax_saveValues(myParams);

		}

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

function ajax_showTables(myParams) {
	// printlnMessage('messages', "ajax_showTables() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxshowTablesRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxshowTablesRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxshowTablesRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxshowTablesRequest.onreadystatechange = ajaxCalled_showTables;
	var requeststring;
	requeststring = "DBFunctions.php?json=" + JSON.stringify(myParams);
	// printlnMessage('messages', requeststring);
	ajaxshowTablesRequest.open("POST", encodeURI(requeststring), true);
	ajaxshowTablesRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_showTables() {
	if (ajaxshowTablesRequest.readyState == 4) {

		// printlnMessage('messages',"ajaxCalled_showTables called");
		ValuesAjax = ajaxshowTablesRequest.responseText;
		// printlnMessage('messages', ValuesAjax);

		ValuesAjaxJSON = JSON.parse(ValuesAjax);
		// printlnMessage('messages', 'Tables:');
		elementId = document.getElementById("dayComboBox");
		elementId.options.length = 0;

		// for ( var i = 0; i < items.length; i++) {
		// }
		// //printlnMessage('messages', ValuesAjaxJSON.lV3.length);
		AddItem("dayComboBox", "select a date", 1);
		length = ValuesAjaxJSON.table.length;
		for (i = 0; i < length; i++) {
			day = ValuesAjaxJSON.table[i];
			// printlnMessage('messages', day);
			AddItem("dayComboBox", day, day);
		}

		date = ValuesAjaxJSON.table[length - 1];
		printlnMessage('messages', ValuesAjaxJSON.table[length - 1]);
		document.getElementById("dayComboBox").value = date;

		dayComboSelect();

	}
}

function ajax_loadValues(myParams) {
	// printlnMessage('messages', "ajax_loadValues() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxloadValuesRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxloadValuesRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxloadValuesRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxloadValuesRequest.onreadystatechange = ajaxCalled_loadValues;
	var requeststring;
	requeststring = "DBFunctions.php?json=" + JSON.stringify(myParams);
	// printlnMessage('messages', requeststring);
	ajaxloadValuesRequest.open("POST", encodeURI(requeststring), true);
	ajaxloadValuesRequest.send(null);
}

// Create a function that will receive data sent from the server
function ajaxCalled_loadValues() {
	if (ajaxloadValuesRequest.readyState == 4) {

		// printlnMessage('messages',"ajaxCalled_loadValues called");
		ValuesAjax = ajaxloadValuesRequest.responseText;
		// printlnMessage('messages', ValuesAjax);

		ValuesAjaxJSON = JSON.parse(ValuesAjax);
		// printlnMessage('messages', ValuesAjaxJSON.message);

		document.getElementById('of').innerText = ValuesAjaxJSON.count;

		// var data;
		// header = sprintf('%22s %7s %6s %8s %7s %6s %8s %7s %6s %8s', 'date ',
		// 'Volt ', 'mA ', 'mW ', 'Volt ', 'mA ', 'mW ', 'Volt ', 'mA ',
		// 'mW ');
		// printlnMessage('messages', header);
		// var data = header + '<br>';
		// printlnMessage('messages', ValuesAjaxJSON.lV3.length);
		mytable = new Array();
		header = [ 'id', 'date', 'Volt', 'mA', 'mW', 'Volt', 'mA', 'mW',
				'Volt', 'mA', 'mW' ]
		mytable.push(header);
		for (i = 0; i < ValuesAjaxJSON.lV3.length; i++) {
			// printlnMessage('messages', ValuesAjaxJSON.lV3[i]);
			id = ValuesAjaxJSON.id[i];
			date = ValuesAjaxJSON.date[i];
			lV1 = ValuesAjaxJSON.lV1[i];
			cmA1 = ValuesAjaxJSON.cmA1[i];
			pw1 = ValuesAjaxJSON.pw1[i];
			lV2 = ValuesAjaxJSON.lV2[i];
			cmA2 = ValuesAjaxJSON.cmA2[i];
			pw2 = ValuesAjaxJSON.pw2[i];
			lV3 = ValuesAjaxJSON.lV3[i];
			cmA3 = ValuesAjaxJSON.cmA3[i];
			pw3 = ValuesAjaxJSON.pw3[i];
			// part1 = new Date().toLocaleString() + ' ';
			cell = new Array();
			cell.push(sprintf('%3d', id));
			cell.push(sprintf('%22s ', date));
			cell.push(sprintf('%7.2f ', parseFloat(lV1)));
			cell.push(sprintf('%6.2f ', parseFloat(cmA1)));
			cell.push(sprintf('%8.2f ', parseFloat(pw1)));
			cell.push(sprintf('%7.2f ', parseFloat(lV2)));
			cell.push(sprintf('%6.2f ', parseFloat(cmA2)));
			cell.push(sprintf('%8.2f ', parseFloat(pw2)));
			cell.push(sprintf('%7.2f ', parseFloat(lV3)));
			cell.push(sprintf('%6.2f ', parseFloat(cmA3)));
			cell.push(sprintf('%8.2f ', parseFloat(pw3)));

			// printlnMessage('messages', cell);
			mytable.push(cell);
			// var printstring = part1 + part2 + part3 + part4 + part5 + part6 +
			// part7 + part8 + part9 + part10;
			// printlnMessage('messages', printstring);
			// data += printstring + '<br>';
		}
		// $('#data').html(data);
		// printlnMessage('messages', ValuesAjaxJSON.pw3);

		// d = new Array(ValuesAjaxJSON.pw3);
		// printlnMessage('messages', d);

		// mytable = new Array(cell);

		var textToAppend = createTableFromData(mytable);

		// printlnMessage('messages', textToAppend);

		// $('#dataTable').append(textToAppend);
		$('#dataTable').html(textToAppend);
	}
}

function ajax_saveToExcel(myParams) {
	// printlnMessage('messages',"ajax_saveToExcel() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxsaveToExcelRequest = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxsaveToExcelRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxsaveToExcelRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxsaveToExcelRequest.onreadystatechange = ajaxCalled_saveToExcel;
	var requeststring;
	requeststring = "DBfunctions.php?json=" + JSON.stringify(myParams);
	// printlnMessage('messages',requeststring);
	ajaxsaveToExcelRequest.open("GET", encodeURI(requeststring), true);
	ajaxsaveToExcelRequest.send(null);
}

function ajaxCalled_saveToExcel() {
	if (ajaxsaveToExcelRequest.readyState == 4) {
		// printlnMessage('messages',"ajaxCalled_retrieveLastPlate() state 4");
		saveToExcelAjax = ajaxsaveToExcelRequest.responseText;
		printlnMessage('messages', saveToExcelAjax);
	}
}
