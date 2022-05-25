#DATA FORMAT
#
# Accelerometer   Gyrometer
# Ax  Ay  Az      Gx  Gy  Gz

ax,ay,az = 0, 0, 16348 # @ 2g - acccel
gx,gy,gz = 0, 100, 0

with open('data', 'w') as f:
  hit = 1
  for i in range(10000):
    f.write(f'{ax} {ay} {az} {gx} {gy} {gz}\n')
    print('ax ay az gx gy gz')
    print(f'{ax} {ay} {az} {gx} {gy} {gz}\n')
    gx += 1
    gy += 1
    gz += 1
