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