# -----------------------------------------------------------------------------
# Python, OpenGL & Scientific Visualization
# www.labri.fr/perso/nrougier/python+opengl
# Copyright (c) 2017, Nicolas P. Rougier
# Distributed under the 2-Clause BSD License.
# -----------------------------------------------------------------------------
import math
from glumpy import app, gloo, gl

vertex =  """
  uniform float theta;
  attribute vec2 position;
  attribute vec4 color;
  varying vec4 v_color;
  void main()
  {
    gl_Position.x = cos(theta)*position.x - sin(theta)*position.y;
    gl_Position.y = sin(theta)*position.x + cos(theta)*position.y;
    gl_Position.z = 0.0;
    gl_Position.w = 1.0;
    v_color = color;
  } """

fragment = """
  varying vec4 v_color;
  void main()
  {
      gl_FragColor = v_color;
  } """

# Build the program and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)

# Upload data into GPU
corn_val = 1/math.sqrt(2)
quad['color'] = [ (1,0,0,1), (0,1,0,1), (0,0,1,1), (1,1,0,1) ]
quad['position'] = [ (-corn_val,-corn_val),   (-corn_val,+corn_val),\
                      (+corn_val,-corn_val),   (+corn_val,+corn_val)   ]
quad['theta'] = 0.0  #initialize to 0: this will be changed in on_draw() below

# Create a window with a valid GL context
window = app.Window(color=(0,0,0,1))

time = 0.0

# Tell glumpy what needs to be done at each redraw
@window.event
def on_draw(dt):
    #Rougier did it differently:  quad['theta'] += dt  
    print(dt)     
    global time
    time += 0.025
    window.clear()
    quad['theta'] = time
    quad.draw(gl.GL_TRIANGLE_STRIP)

# We set the framecount to 360 in order to record a movie that can
# loop indefinetly. Run this program with:
# python quad-scale.py --record quad-scale.mp4
app.run() #(framecount=360)
