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
