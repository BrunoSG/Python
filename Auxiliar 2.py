from pyprocessing import *
def setup():
  global vx, vy
  size(200,200)
  vx = width/2
  vy = height/2
def draw():
  global vx,vy
  background(200)
  ellipse(vx,vy,10,10) #circle at location (vx,vy) and radius 10
def keyPressed():
  global vx,vy
  if key.code == 65362: vy = vy - 5 #decrases vy if the key was up arrow
  if key.code == 65361: vx = vx - 5 #decrases vx if the key was left arrow
  if key.code == 65364: vy = vy + 5 #increases vy if the key was down arrow
  if key.code == 65363: vx = vx + 5 #increases vx if the key was right arrow
run()