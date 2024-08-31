# -*- coding: utf-8 -*-
"""perspective_transform.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ir8cZNrTE4A_c3F_j3NVCqKUeSYx6Pun
"""

"""from google.colab import drive
drive.mount("/content/gdrive")"""
"""from google.colab.patches import cv2_imshow"""
import cv2
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
import torch
import torchvision.transforms as T
from PIL import Image
from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np
# %matplotlib inline

orig_img = cv2.imread('/content/drive/MyDrive/Py/1.Data_augmentation_for_image_registration/input/before.jpg')
print("read")
orig_img = np.asarray(orig_img)
orig_img = Image.fromarray(orig_img)

perspective_transformer = T.RandomPerspective(distortion_scale=0.6, p=1.0)
x=0

while(True):
  perspective_imgs = perspective_transformer(orig_img)
  plt.imshow(np.squeeze(perspective_imgs))
  plt.show()
  y=str(x)
  cv2.imwrite('/content/drive/MyDrive/Py/1.Data_augmentation_for_image_registration/output/test'+y+'.jpg',np.squeeze(perspective_imgs))
  x=x+1
  if(x>=5):
    break