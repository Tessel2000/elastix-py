from __future__ import print_function, absolute_import
import elastix
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
import SimpleITK as sitk

fixed_image_path = 'example_data/patient1.jpg'
moving_image_path = 'example_data/patient2.jpg'

im1 = imageio.imread(fixed_image_path)
im2 = imageio.imread(moving_image_path)


ELASTIX_PATH = os.path.join(r'C:\Users\tesse\OneDrive\Universiteit\000-Generate\Universiteit\Capita selecta on medical image analysis\elastix-5.0.0-win64\elastix.exe')
TRANSFORMIX_PATH = os.path.join(r'C:\Users\tesse\OneDrive\Universiteit\000-Generate\Universiteit\Capita selecta on medical image analysis\elastix-5.0.0-win64\transformix.exe')

if os.path.exists('results') is False:
    os.mkdir('results')

el = elastix.ElastixInterface(elastix_path=ELASTIX_PATH)
el.register(
    fixed_image=fixed_image_path,
    moving_image=moving_image_path,
    parameters=[os.path.join('example_data', 'parameters_samplespace2_MR.txt')],
    output_dir='results')

# fig, ax = plt.subplots(1, 3, figsize=(20, 5))
# ax[0].imshow(im1)
# ax[0].set_title('Fixed image')
# ax[1].imshow(im2)
# ax[1].set_title('Moving image')
#
# Iteration_file_path = os.path.join('results', 'IterationInfo.0.R0.txt')
# log = elastix.logfile(Iteration_file_path)
#
# ax[2].plot(log['itnr'], log['metric'])
# ax[2].set_title('Cost function over iterations')
# ax[2].set_xlabel('Iteration')
# ax[2].set_ylabel('Cost metric')
# plt.show()

# Find the results
transform_path = os.path.join('results', 'TransformParameters.0.txt')
result_path = os.path.join('results', 'result.0.tiff')

# Open the logfile into the dictionary log
for i in range(5):
    log_path = os.path.join('results', 'IterationInfo.0.R{}.txt'.format(i))
    log = elastix.logfile(log_path)
    # Plot the 'metric' against the iteration number 'itnr'
    plt.plot(log['itnr'], log['metric'])
plt.legend(['Resolution {}'.format(i) for i in range(5)])

# Load the fixed, moving, and result images
fixed_image = imageio.imread(fixed_image_path)[:, :, 0]
moving_image = imageio.imread(moving_image_path)[:, :, 0]
transformed_moving_image = imageio.imread(result_path)

# Show the resulting image side by side with the fixed and moving image
fig, ax = plt.subplots(1, 4, figsize=(20, 5))
ax[0].imshow(fixed_image, cmap='gray')
ax[0].set_title('Fixed image')
ax[1].imshow(moving_image, cmap='gray')
ax[1].set_title('Moving image')
ax[2].imshow(transformed_moving_image, cmap='gray')
ax[2].set_title('Transformed\nmoving image')

plt.show()