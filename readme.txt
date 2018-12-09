Learning glumpy using the tutorial from its author:
http://www.labri.fr/perso/nrougier/python-opengl/#python-opengl-for-scientific-visualization

Installation instructions
Based mostly on https://glumpy.readthedocs.io/en/latest/installation.html

1. If you don't already have it, install MS build tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/
I installed MS Visual Studio community edition 2017 with no additional bells or whistles.

2. At the anaconda prompt create the glumpy environment (or whatever you want to call it). 
  conda create --name glumpy
  conda install python=3.6 numpy cython pyopengl freetype freeglut spyder -y
  pip install triangle glumpy

3. Put the GLFW binaries in the right place.
Go to http://www.glfw.org/download.html, get the binaries that are right for your system, and put glf3.dll (from lib-ming2-w64)
in the folder returned by the `where python` command in your anaconda prompt.

5. Run spyder from your environment, and glumpy should just work.
I would try one of the glut examples (glut_quad_solid.py), and one of the glumpy examples (glumpy_quad_solid.py). Obviously you don't have to use Spyder. You can run scripts from the conda prompt too.

6. In case of emergency, break glass
If you mess up and need to start over:
conda remove --name glumpy --all

