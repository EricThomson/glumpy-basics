'''
Minimal example with OpenGL, the 'hard' way from Rougier's online book:
http://www.labri.fr/perso/nrougier/python-opengl/#the-hard-way

Shows how to use glut to open a GL context and draw an empty window.
'''

import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    glut.glutSwapBuffers()

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == b'\x1b':
        sys.exit( )

glut.glutInit()  #create a gl context -- you won't have access to any GL commands before this
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)  #initial display mode double buffer/rgba color model
glut.glutCreateWindow(b'Hello world!')  #b because https://stackoverflow.com/a/27154196/1886357
glut.glutReshapeWindow(512,512)
glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)  #callback -> esc will close window
glut.glutMainLoop()