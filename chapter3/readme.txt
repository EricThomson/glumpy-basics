Chapter 3 notes
http://www.labri.fr/perso/nrougier/python-opengl/

This includes all the examples from Ch 3 of Rougier's book. It does things in glut to show the low level OpenGL details (The Hard Way section), and in glumpy to show how much easier it is when you use an abstraction layer in glumpy (The Easy Way). 

Programs:
Glut:
glut_open_gl_context.py: shows how to open an opengl context

Glut/glumpy
*_quad_solid.py : simplest case of how to draw a square with color hard-coded into fragment shader, position fed in from progam.
*_quad_uniform_color.py: slightly more complex case where color is fed into fragment shader as a uniform variable.
*_quad_varying_color.py: vertices are colored, and fragment interpolates with varying color.

Glumpy only
glumpy_quad_scale.py: takes rainbow square and scales it with time so it shrinks down to zero area and back up to 1.
glumpy_quad_rotation_eric.py: solution to problem of rotating the cube in time (there is a Rougier version online that is different: http://www.labri.fr/perso/nrougier/python-opengl/code/chapter-03/quad-rotation.py).



