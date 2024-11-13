'''For Linux (Pydroid 3):

1. `psutil` library

Install: `pip install psutil`'''

import psutil

battery = psutil.sensors_battery()
if battery is not None:
    print(f"Battery percentage: {battery.percent}%")
    print(f"Power plugged: {battery.power_plugged}")
else:
    print("Battery information not available")

'''For Android :

1. `android-battery` library (not recommended, as it's outdated)

import android

android.batteryStartMonitoring()

print(f"Battery level: {android.getBatteryLevel()}")
print(f"Battery status: {android.getBatteryStatus()}")

android.batteryStopMonitoring()'''

'''
For Windows:

Code remains the same as for Linux.


Cross-platform solution:

Install: `pip install pybattery`

import pybattery

print(f"Battery percentage: {pybattery.get_battery_percentage()}%")
print(f"Battery status: {pybattery.get_battery_status()}")
'''