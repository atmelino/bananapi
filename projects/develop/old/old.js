
			// part1 = new Date().toLocaleString() + ' ';
			part1 = sprintf('%3d %22s ', id,date);
			part2 = sprintf('%7.2f ', parseFloat(lV1));
			part3 = sprintf('%6.2f ', parseFloat(cmA1));
			part4 = sprintf('%8.2f ', parseFloat(pw1));
			part5 = sprintf('%7.2f ', parseFloat(lV3));
			part6 = sprintf('%6.2f ', parseFloat(cmA3));
			part7 = sprintf('%8.2f ', parseFloat(pw3));
			part8 = sprintf('%7.2f ', parseFloat(lV3));
			part9 = sprintf('%6.2f ', parseFloat(cmA3));
			part10 = sprintf('%8.2f ', parseFloat(pw3));
			var printstring = part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9 + part10;
			// printlnMessage('messages', printstring);
			data += printstring + '<br>';

	var oTable;
	// 	$(document).ready(function() {
	// 		$('#example').DataTable({
	// 			data : dataSet,
	// 			columns : [ {
	// 				title : "Name"
	// 			}, {
	// 				title : "Position"
	// 			}, {
	// 				title : "Office"
	// 			}, {
	// 				title : "Extn."
	// 			}, {
	// 				title : "Start date"
	// 			}, {
	// 				title : "Salary"
	// 			} ]
	// 		});
	// 	});

	// 	$(document).ready(function() {
	// 		$('#example').DataTable();
	// 	});

	// 	$(document).ready(function() {
	// 		var oTable = $('#example').dataTable({
	// 			"bProcessing" : true,
	// 			"bServerSide" : true,
	// 			"sAjaxSource" : "server_processing04.php",

	// 			fnRowCallback : function(nRow, aData, iDisplayIndex, iDisplayIndexFull) {
	// 				// Row click
	// 				$(nRow).on('click', function() {
	// 					console.log('Row Clicked', this, aData, iDisplayIndex, iDisplayIndexFull);
	// 				});

	// 				// Cell click
	// 				$('td', nRow).on('click', function() {
	// 					console.log('Col Clicked.', this, aData, iDisplayIndex, iDisplayIndexFull);
	// 				});
	// 			}

	// 		});

	// 		var table = $('#example').DataTable();

	// 		var columns = table.columns();
	// 		//alert(columns);

	// 		//table.column('2').visible(false);

	// 	});

// 	$(document).ready(function() {
// 		$('#example').dataTable({
// 			'bSort' : false,
// 			'aoColumns' : [ {
// 				sWidth : "45%",
// 				bSearchable : false,
// 				bSortable : false
// 			}, {
// 				sWidth : "45%",
// 				bSearchable : false,
// 				bSortable : false
// 			}, {
// 				sWidth : "10%",
// 				bSearchable : false,
// 				bSortable : false
// 			} ],
// 			"scrollY" : "200px",
// 			"scrollCollapse" : true,
// 			"info" : true,
// 			"paging" : true
// 		});
// 	});



$("#loadValues").click(function() {
			myParams = {
				fs : 'loadValues',
				param2 : 2
			};
			//printlnMessage('messages', "load values clicked");
			ajax_loadValues(myParams);
		});
		function ajax_saveValues(myParams) {
			// printlnMessage('messages', "ajax_saveValues() called");
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
			var requeststring;
			requeststring = "DBFunctions.php?json=" + JSON.stringify(myParams);
			// printlnMessage('messages', requeststring);
			ajaxsaveValuesRequest.open("POST", encodeURI(requeststring), true);
			ajaxsaveValuesRequest.send(null);
		}

		// Create a function that will receive data sent from the server
		function ajaxCalled_saveValues() {
			if (ajaxsaveValuesRequest.readyState == 4) {

				// printlnMessage('messages',"ajaxCalled_saveValues called");
				ValuesAjax = ajaxsaveValuesRequest.responseText;
				// printlnMessage('messages', ValuesAjax);

			}
		}






// 		$('.vertical input').spinner({
		// 			min : -10,
		// 			max : 10,
		// 			alignment : 'vertical'
		// 		}).val(0);


			//var spinner = $("#frontLeft").spinner();
			//printlnMessage('messages', $("#frontLeft").spinner("value"));
			//printlnMessage('messages', this);
			//printlnMessage('messages', spinner.spinner("value"));
			// 			ajax_setSpeed(ajaxCalled_setSpeed, "fl", 3);
			// 			ajax_setSpeed(ajaxCalled_setSpeed, "fr", 3);
			// 			ajax_setSpeed(ajaxCalled_setSpeed, "rl", 3);
			// 			ajax_setSpeed(ajaxCalled_setSpeed, "rr", 3);

			// 			wheel = "fl";
			// 			speed = spinnerfl.spinner("value");
			// 			ajax_setSpeed(ajaxCalled_setSpeed, wheel, speed);
			// 			wheel = "rl";
			// 			speed = spinnerrl.spinner("value");
			// 			ajax_setSpeed(ajaxCalled_setSpeed, wheel, speed);
			// 			wheel = "fr";
			// 			speed = spinnerfr.spinner("value");

			// 			ajax_setSpeed(ajaxCalled_setSpeed, wheel, speed);
			// 			wheel = "rr";
			// 			speed = spinnerrr.spinner("value");
			// 			ajax_setSpeed(ajaxCalled_setSpeed, wheel, speed);
			$("#prompt_example").click(function() {
				jPrompt("Enter your name", function(e, value) {
					jAlert("You name :" + value + ":");

				});
			});

			
			$("#buttonDatabasetmp").click(function() {
				jPrompt('Type something:', 'Prefilled value', 'Prompt Dialog', function(r) {
					if (r)
						alert('You entered ' + r);
				});
			});
			// 						if (getCookie('hostname') == "localhost")
			// 							sim = 1;
			// 						else
			// 							sim = 0;

			// 						hostname = "localhost";
			$("#saveValues").click(function() {
				myParams = {
					fs : 'saveValues',
					lV3 : 2,
					cmA3 : 3,
					pw3 : 6,
				};
				//printlnMessage('messages', JSON.stringify(myParams));
				//printlnMessage('messages', "save values clicked");
				ajax_saveValues(myParams);
			});

			function getValues() {
				//printlnMessage('messages', "get values");

				if (document.getElementById('simulation').checked)
					simulation = 1;
				else
					simulation = 0;

				myParams = {
					simulation : simulation,
					param2 : 2
				};
				//printlnMessage('messages', JSON.stringify(myParams));
				ajax_getValues(myParams);
			}
			$("#getValues").click(function() {
				printlnMessage('messages', header);
				getValues();
			});