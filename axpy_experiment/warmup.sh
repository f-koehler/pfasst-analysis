#!/bin/bash
function fulload() { dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null & };
fulload
echo "Press enter when warm enough!"
read
killall dd
