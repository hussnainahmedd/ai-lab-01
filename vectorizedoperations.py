import numpy as np

battery_readings = np.array([100 , 92 , 84 , 76 , 68 ,60])

print("Drop per step: ", np.diff(battery_readings))
print("Below 80 : " , battery_readings[battery_readings < 80])
print ("mean:" , np.mean(battery_readings))
