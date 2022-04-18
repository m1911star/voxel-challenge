from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=10)
scene.set_floor(-3, (1.0, 1.0, 1.0))
scene.set_background_color((0.165, .165, .165))
scene.set_directional_light((1, 1, 1), 0.0, (.165, .165, .165))


@ti.kernel
def initialize_voxels():
    black_button_color = vec3(0.125, 0.125, 0.125)
    normal = vec3(0.769, 0.753, 0.82)
    for i in range(0, 10):
        for j in range(0, 15):
            for k in range(0, 3):
                color = vec3(1, 0, 0)
                if i == 1 and j == 4 and k == 2:
                    color = black_button_color
                    # scene.set_voxel(vec3(i, j, k), 2, black_button_color)
                elif i == 2 and 3 <= j <= 5 and k == 2:
                    color = black_button_color
                    # scene.set_voxel(vec3(i, j, k), 2, black_button_color)
                elif i == 3 and j == 4 and k == 2:
                    color = black_button_color
                    # scene.set_voxel(vec3(i, j, k), 2, black_button_color)
                elif 1 <= i <= 8 & 8 <= j <= 12:
                    if 2 <= i <= 7 and 9 <= j <= 11:
                        color = vec3(0.357, 0.349, 0.188)
                    else:
                        color = vec3(0.439, 0.435, 0.467)
                else:
                    color = normal
                    # scene.set_voxel(vec3(i, j, k), 2, normal)
                scene.set_voxel(vec3(i, j, k), 1, color)
    # red button
    scene.set_voxel(vec3(6, 4, 2), 1, vec3(0.573, 0, 0.167))
    scene.set_voxel(vec3(8, 5, 2), 1, vec3(0.573, 0, 0.167))

    scene.set_voxel(vec3(4, 1, 2), 1, vec3(0.3176470588235294, 0.3137254901960784, .33333333))
    scene.set_voxel(vec3(6, 1, 2), 1, vec3(0.3176470588235294, 0.3137254901960784, .33333333))

    for i in range(2, 9):
        scene.set_voxel(vec3(i, 14, 0), 1, vec3(1, 0, 0))

initialize_voxels()

scene.finish()
