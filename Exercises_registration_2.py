from __future__ import print_function, absolute_import
import elastix
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
import SimpleITK as sitk

# IMPORTANT: these paths may differ on your system, depending on where
# Elastix has been installed. Please set accordingly.
ELASTIX_PATH = os.path.join(r'C:\Users\tesse\OneDrive\Universiteit\000-Generate\Universiteit\Capita selecta on medical image analysis\elastix-5.0.0-win64\elastix.exe')
TRANSFORMIX_PATH = os.path.join(r'C:\Users\tesse\OneDrive\Universiteit\000-Generate\Universiteit\Capita selecta on medical image analysis\elastix-5.0.0-win64\transformix.exe')

if not os.path.exists(ELASTIX_PATH):
    raise IOError('Elastix cannot be found, please set the correct ELASTIX_PATH.')
if not os.path.exists(TRANSFORMIX_PATH):
    raise IOError('Transformix cannot be found, please set the correct TRANSFORMIX_PATH.')

# Make a results directory if non exists
if os.path.exists('results') is False:
    os.mkdir('results')

itk_image = sitk.ReadImage('example_data/chest_ct.mhd')
image_array =sitk.GetArrayFromImage(itk_image)

raw_path = os.path.join('example_data', 'chest_ct.raw')
width = 112
height = 256
depth = 256  # For 2D images, set depth to 1
pixel_type = sitk.sitkUInt32  # Adjust pixel type based on your image
image = sitk.ReadImage(raw_path, (width, height, depth), pixel_type)
image_array_2 = sitk.GetArrayFromImage(image)

print(np.shape(image_array_2))

fixed_image = image_array[:,100,:]
moving_image = image_array[:,110,:]

# Show the resulting image side by side with the fixed and moving image
fig, ax = plt.subplots(1, 4, figsize=(20, 5))
ax[0].imshow(fixed_image, cmap='gray')
ax[0].set_title('Fixed image')
ax[1].imshow(moving_image, cmap='gray')
ax[1].set_title('Moving image')

plt.show()