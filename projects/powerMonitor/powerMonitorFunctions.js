function getValuesTimerFunc() {
	//printMessage('messages', sprintf("timer event %02d ", (counter++)));
	getValues();
	period_ms=period*1000;
	//printlnMessage('messages', "period_ma " + period_ms);

	
	getValuesTimer = setTimeout('getValuesTimerFunc()', period*1000); // refresh every
																// x secs
}

function killAllTimers() {
	// clear all scheduled future function calls
	clearTimeout(getValuesTimer);
	// clearTimeout(primeTimer);

}
