from ursina import *

app = Ursina()

rocket = Entity(model='rocket.obj', collider='mesh')

rocket.x -= 60
rocket.z += 500

def update():
  ax,ay,az,gx,gy,gz = data.readline().strip().split()
  rocket.rotation_x = float(gx)
  rocket.rotation_y = float(gy)
  rocket.rotation_z = float(gz)
  print(ax,ay,az,gx,gy,gz)

data = open('data', 'r')
app.run()
data.close()
