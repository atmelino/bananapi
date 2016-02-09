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