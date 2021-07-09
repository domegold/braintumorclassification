import h5py
import numpy as np
import glob

from PIL import Image

def convert_mat_file(filename):
	arrays = {}
	f = h5py.File(filename)
	for k, v in f.items():
	    arrays[k] = np.array(v)
	    #print(list(f.keys()))
	    #print(f['cjdata']['image'])
	    image = np.array(f['cjdata'].get('image')).astype(np.float64)
	    hi = np.max(image)
	    lo = np.min(image)
	    image = (((image - lo)/(hi-lo))*255).astype(np.uint8)
	    im = Image.fromarray(image)
	    #print(f['cjdata']['label'][0][0])
	    folder = str(f['cjdata']['label'][0][0]) + "/"
	    im.save(folder+filename[0:-4]+".jpg")
	    print(filename+" converted successfully")

for file in glob.glob("*.mat"):
#	print(file)
	convert_mat_file(file)

