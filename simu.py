from ursina import *

app = Ursina()

rocket = Entity(model='rocket.obj', collider='mesh')

rocket.z += 500
rocket.x -= 60

def controls():
  speed = 40
  rocket.rotation_y += 0.4
  rocket.rotation_x += 0.2
  
  camera.y += held_keys['w'] * time.dt * speed
  camera.y -= held_keys['s'] * time.dt * speed
  camera.x += held_keys['d'] * time.dt * speed
  camera.x -= held_keys['a'] * time.dt * speed
  camera.z += held_keys['e'] * time.dt * speed * 3
  camera.z -= held_keys['q'] * time.dt * speed * 3

  rocket.rotation_x -= held_keys['w'] * time.dt *speed
  rocket.rotation_x += held_keys['s'] * time.dt *speed
  rocket.rotation_y -= held_keys['d'] * time.dt *speed
  rocket.rotation_y += held_keys['a'] * time.dt *speed

def update():
  #controls()
  ax,ay,az,gx,gy,gz = data.readline().strip().split()
  rocket.rotation_x = float(gx)
  rocket.rotation_y = float(gy)
  rocket.rotation_z = float(gz)
  print(ax,ay,az,gx,gy,gz)

data = open('data', 'r')
app.run()
data.close()
