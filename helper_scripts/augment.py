import os
import glob
from scipy import ndarray
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io

def rotation(image_to_rotate, rotation_degree):
    return sk.transform.rotate(image_to_rotate, rotation_degree)

for file in glob.glob("*.jpg"):
	print(file)
	input_image = sk.io.imread(file)
	image_rot_l = rotation(input_image, -25)
	image_rot_r = rotation(input_image, 25)
	sk.io.imsave(file.split(".")[0] + "_rot_l.jpg", image_rot_l)
	sk.io.imsave(file.split(".")[0] + "_rot_r.jpg", image_rot_r)