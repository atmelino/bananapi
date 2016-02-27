function printMessage(target, message) {
	elementId = document.getElementById(target);
	if (elementId != null) {
		elementId.innerHTML += message;
		elementId.scrollTop = elementId.scrollHeight;
	}
}

function printlnMessage(target, message) {
	elementId = document.getElementById(target);
	if (elementId != null) {
		printMessage(target, message);
		elementId.innerHTML += '\n';
	}

}

function clearMessage(target) {
	document.getElementById(target).innerHTML = '';
}

function getCookie(c_name) {
	var i, x, y, ARRcookies = document.cookie.split(";");
	for (i = 0; i < ARRcookies.length; i++) {
		x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
		y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
		x = x.replace(/^\s+|\s+$/g, "");
		if (x == c_name) {
			return unescape(y);
		}
	}
}

function existCookie(c_name) {
	var myBoolean = new Boolean(false);
	var i, x, y, ARRcookies = document.cookie.split(";");
	for (i = 0; i < ARRcookies.length; i++) {
		x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
		y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
		x = x.replace(/^\s+|\s+$/g, "");
		if (x == c_name) {
			myBoolean = true;
		}
	}
	return myBoolean;
}

function setCookie(c_name, value, exdays) {
	var exdate = new Date();
	exdate.setDate(exdate.getDate() + exdays);
	var c_value = escape(value)
			+ ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
	document.cookie = c_name + "=" + c_value;
	// printlnMessage('messages', "cookie "+c_name+" set to "+ value);
}

function AddItem(Element, Text, Value) {
	// Create an Option object
	var opt = document.createElement("option");

	// Add an Option object to Drop Down/List Box
	document.getElementById(Element).options.add(opt);

	// Assign text and value to Option object
	opt.text = Text;
	opt.value = Value;
}

function getSelectedText(elementId) {

	// printMessage('messages',"elementId:");
	// printlnMessage('messages',elementId);

	var elt = document.getElementById(elementId);

	if (elt.selectedIndex == -1)
		return null;

	return elt.options[elt.selectedIndex].text;
}

function createTableFromData(data) {
	// usage:
	// var textToAppend = createTableFromData(data);
	// $('#example').append(textToAppend);

	var tableHtml = '';
	var currentRowHtml;
	for ( var i = 0, length = data.length; i < length; i++) {
		currentRowHtml = '	<tr>		<td>' + data[i].join('</td>		<td>')
				+ '</td>	</tr>';
		tableHtml += currentRowHtml;
	}
	return tableHtml;
}
