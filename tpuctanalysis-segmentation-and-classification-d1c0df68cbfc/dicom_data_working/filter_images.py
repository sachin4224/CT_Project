import numpy as np 
import scipy.ndimage
from skimage import feature
from scipy.misc.pilutil import Image
import scipy.misc
import cv2



image_path="/Users/sachin/Desktop/CT_Project/masked_dicom_images/026.png"
a=Image.open(image_path)
a=scipy.misc.fromimage(a)
b=cv2.Canny(a,1000,1100)

b=scipy.misc.toimage(b)
b.save("/Users/sachin/Desktop/CT_Project/masked_images_after_filter/026_1.png")
