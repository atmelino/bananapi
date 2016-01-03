<?php

shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr0/brightness');
shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr1/brightness');
shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr2/brightness');
shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr3/brightness');
?>
