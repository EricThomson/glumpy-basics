# -*- coding: utf-8 -*-
"""
Homogeneous coordinates in Python
Eric Thomson accompanying Chapter 4 of Rougier's book
http://www.labri.fr/perso/nrougier/python-opengl/

Also taking a heavy dose from the excellent:
https://blogs.mathworks.com/graphics/2015/09/28/homogeneous-coordinates/
"""

import numpy as np
import matplotlib.pyplot as plt #plt.plot(x, y)
plt.style.use('classic')

#%% Note I set the zorder so grid lines show up behind points
pts = np.array([ [1,  -1, -1,  1,],
                 [1,   1, -1, -1,],
                 [1,  1,  1,  1] ], dtype = np.float32)
x_cart = pts[0,:]/pts[2,:]
y_cart = pts[1,:]/pts[2,:]
plt.close('all')
fig, ax = plt.subplots()
ax.fill(x_cart, y_cart, 'b', alpha = 0.3, zorder = 3)
ax.plot(x_cart, y_cart, c = 'b', alpha = 0.8, zorder = 3)
plt.grid(linestyle = '-', color ="#E9E9E9", zorder = 0)
plt.xlabel('x')
plt.ylabel('y');
ax.axis('square')
ax.axis((-2.5, 2.5, -2.5, 2.5))


#%% Rotation counterclockwise
rot_angle = np.pi/4;  #
rot_mat = np.array([[np.cos(rot_angle), -np.sin(rot_angle), 0],
                    [np.sin(rot_angle), np.cos(rot_angle), 0],
                    [   0,                 0,         1]]);

pts_rotated = rot_mat.dot(pts);
rot_x_cart = pts_rotated[0,:]/pts_rotated[2,:]
rot_y_cart = pts_rotated[1,:]/pts_rotated[2,:]
ax.fill(rot_x_cart, rot_y_cart, 'y', alpha = 0.3, zorder = 3)
ax.plot(rot_x_cart, rot_y_cart, c = 'y', alpha = 0.8, zorder = 3)

#%% Scale
scale_factor = 0.5;
scale_mat = np.array([[scale_factor,  0,         0],
             [0         , scale_factor, 0],
             [0         ,    0,         1]]);
pts_scaled = scale_mat.dot(pts);
scale_x_cart = pts_scaled[0,:]/pts_scaled[2,:]
scale_y_cart = pts_scaled[1,:]/pts_scaled[2,:]
ax.fill(scale_x_cart, scale_y_cart, 'r', alpha = 0.3, zorder = 3)
ax.plot(scale_x_cart, scale_y_cart, c = 'r', alpha = 0.8, zorder = 3)

#%% Translate
x_trans = 1;
y_trans = -2;
translation_mat = np.array([[1,  0, x_trans],
                            [0,  1, y_trans],
                            [0,  0,    1]]);
pts_translated = translation_mat.dot(pts);
translated_x_cart = pts_translated[0,:]/pts_scaled[2,:]
translated_y_cart = pts_translated[1,:]/pts_scaled[2,:]
ax.fill(translated_x_cart, translated_y_cart, 'g', alpha = 0.3, zorder = 3)
ax.plot(scale_x_cart, scale_y_cart, c = 'g', alpha = 0.8, zorder = 3)


#%% Arbitrary combinations of stuff
sc_ro_tr = translation_mat.dot(scale_mat.dot(rot_mat))
pts_sc_ro_tr = sc_ro_tr.dot(pts)
sc_ro_tr_x_cart = pts_sc_ro_tr[0,:]/pts_sc_ro_tr[2,:]
sc_ro_tr_y_cart = pts_sc_ro_tr[1,:]/pts_sc_ro_tr[2,:]
ax.fill(sc_ro_tr_x_cart, sc_ro_tr_y_cart, 'g', alpha = 0.3, zorder = 3)
ax.plot(sc_ro_tr_x_cart, sc_ro_tr_y_cart,  c = 'g', alpha = 0.8, zorder = 3)





# :)
