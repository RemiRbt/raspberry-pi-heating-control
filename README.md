# Raspberry PI heating control project

This is a small project to turn on the heater automatically 1h before waking up.
Integrating shutdown button and reset motor position button.

You'll need:
- Raspberry Pi (any model)
- 2 push button
- 1 servo motor
- wires

## Wiring

Here is a simple diagram to wire all your components:
![Wire diagram](https://raw.githubusercontent.com/RemiRbt/raspberry-pi-heating-control/master/diagram.png "Wire diagram")

## Python files

Just add the 3 python files to your home directory (*/home/pi*).

## Run files when Rpi boots

In order to run files when Rpi boots, you have to modify this file :
*/etc/rc.local*
And add these lines:
```
python /home/pi/shutdown.py &
python /home/pi/clearSpinButton.py &
```

# Trigger the motor 1 hour before you wake up

For this step, you have to modify the [crontab](http://github.com).
Just add this line:
```
30 6 * * * python /home/pi/spinForward.py
```
Edit the crontab as you wish so that the heating is triggered before your alarm :smile: