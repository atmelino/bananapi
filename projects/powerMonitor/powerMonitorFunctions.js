function getValuesTimerFunc() {
	printMessage('messages', sprintf("timer event %02d ", (counter++)));
	getValues();
	getValuesTimer = setTimeout('getValuesTimerFunc()', 1000); // refresh every
																// x secs
}

function killAllTimers() {
	// clear all scheduled future function calls
	clearTimeout(getValuesTimer);
	// clearTimeout(primeTimer);

}
