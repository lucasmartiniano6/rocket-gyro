# Avalanche noise random number generator
# 3D Rocket gyroscope simulation
Based on the MPU6050 motion tracking device. This aims to recreate in-flight rocket experience based solely in the output data from the MPU6050 gyroscope and accelerometer.

[Inertial rocket](screenshot.png)

[Moving rocket](move.png)

Nice TODO
-----
  * Implement accelerator effects (+-2g)

Usage
-----

```
 pip3 install ursina 
 # then...
 ./simu.py
```

Implementation
-----
The data file is read and each line is interpreted as: [accel-x accel-y accel-z gyro-x gyro-y gyro-z].
Then, the ursina engine rotates the 3d rocket model accordingly. For simulation purposes, the data file was artificially generated, see generate_data.py for how.

Check for more information:
  * https://product.tdk.com/system/files/dam/doc/product/sensor/mortion-inertial/imu/data_sheet/mpu-6000-datasheet1.pdf
  * https://mjwhite8119.github.io/Robots/mpu6050
