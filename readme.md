## Learning Glumpy  
Following along the glumpy tutorial of its author, Nicolas Rougier (http://www.labri.fr/perso/nrougier/python-opengl/#python-opengl-for-scientific-visualization). Each chapter has its own more detailed `readme` that includes an annotated list of the programs it contains.


### Installation instructions (Anaconda/Windows 10)
Getting things to work in Linux is probably easier, so I would do that. But if you must work in Windows (which I do sometimes), here is how I got it working. This based mostly on https://glumpy.readthedocs.io/en/latest/installation.html

1. Install MS build tools:    
Get it here: https://visualstudio.microsoft.com/visual-cpp-build-tools/    
I installed MS Visual Studio community edition 2017 with no additional bells or whistles.

2. At the Conda prompt create the glumpy environment.    
```
conda create --name glumpy           
conda install python=3.6 numpy cython pyopengl freetype freeglut spyder -y    
pip install triangle glumpy```

3. Put GLFW binaries in the right place.    
Go to http://www.glfw.org/download.html, get the binaries that are right for your system, and put `glf3.dll` (from `lib-ming2-w64`)
in the folder returned by the `where python` command in your anaconda prompt.

4. Run spyder from your environment, and glumpy should just work.    
I would try one of the glut examples (`glut_quad_solid.py`), and one of the glumpy examples (`glumpy_quad_solid.py`). Obviously you don't have to use Spyder. Just do your thing.
