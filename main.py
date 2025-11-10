import numpy as np
import scipy
import matplotlib
import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

directory = os.fsencode('dataset-resized/cardboard')

#dataframe with each image's category, image file, and filename. May or may not actually get used
image_frame = pd.DataFrame(columns=('category', 'image', 'filename'))

#a big array of filenames
filename_array = []
#a big array of images (our "X")
image_array = []
#a big array of categories (our "y")
category_array = []

i = 0

#we basically just run the for loop below six times, once for each category, filling out the arrays and dataframe.
category = 'cardboard'

for filename in os.listdir('dataset-resized/' + category):
    current_path = 'dataset-resized/' + category + '/' + filename
    current_image = Image.open(current_path)
    image_frame.loc[i] = {"category" : category, "image" : current_image, "filename" : filename}
    category_array.append(category)
    image_array.append(current_image)
    filename_array.append(filename)
    i += 1
    #filename = os.fsdecode(file)
 #   print(filename)

category = 'glass'

for filename in os.listdir('dataset-resized/' + category):
    current_path = 'dataset-resized/' + category + '/' + filename
    current_image = Image.open(current_path)
    image_frame.loc[i] = {"category" : category, "image" : current_image, "filename" : filename}
    category_array.append(category)
    image_array.append(current_image)
    filename_array.append(filename)
    i += 1

category = 'metal'

for filename in os.listdir('dataset-resized/' + category):
    current_path = 'dataset-resized/' + category + '/' + filename
    current_image = Image.open(current_path)
    image_frame.loc[i] = {"category" : category, "image" : current_image, "filename" : filename}
    category_array.append(category)
    image_array.append(current_image)
    filename_array.append(filename)
    i += 1

category = 'paper'

for filename in os.listdir('dataset-resized/' + category):
    current_path = 'dataset-resized/' + category + '/' + filename
    current_image = Image.open(current_path)
    image_frame.loc[i] = {"category" : category, "image" : current_image, "filename" : filename}
    category_array.append(category)
    image_array.append(current_image)
    filename_array.append(filename)
    i += 1

category = 'plastic'

for filename in os.listdir('dataset-resized/' + category):
    current_path = 'dataset-resized/' + category + '/' + filename
    current_image = Image.open(current_path)
    image_frame.loc[i] = {"category" : category, "image" : current_image, "filename" : filename}
    category_array.append(category)
    image_array.append(current_image)
    filename_array.append(filename)
    i += 1

category = 'trash'

for filename in os.listdir('dataset-resized/' + category):
    current_path = 'dataset-resized/' + category + '/' + filename
    current_image = Image.open(current_path)
    image_frame.loc[i] = {"category" : category, "image" : current_image, "filename" : filename}
    category_array.append(category)
    image_array.append(current_image)
    filename_array.append(filename)
    i += 1

#test display
print(image_frame.head(5))
print(filename_array[1392])
plt.imshow(image_array[1392])
plt.show()