#DATA FORMAT
#
# Accelerometer   Gyrometer
# Ax  Ay  Az      Gx  Gy  Gz

ax,ay,az = 0, 0, 16348 # @ 2g - acccel
gx,gy,gz = 0, 0, 0

with open('data', 'w') as f:
  for i in range(10000):
    f.write(f'{ax} {ay} {az} {gx} {gy} {gz}\n')
    print('ax ay az gx gy gz')
    print(f'{ax} {ay} {az} {gx} {gy} {gz}\n')
    gy = 100
    gx = -25
