# import cv2
# import numpy as np


# async def colour_analyzer(filepath):
#     # Load the image
#     image = cv2.imread(filepath)

#     # Check if the image was loaded successfully
#     if image is None:
#         print("Error: Unable to load image.")
#         return None

#     temp_image = image[50:1000, 150:175]

#     # Get the height and width of the image
#     height, width, _ = temp_image.shape

#     temp_image = cv2.resize(temp_image, dsize=(width*2, height))
#     image = temp_image

#     xpos = width//2
#     ypos = 20

#     segment_height = 90

#     mean_colour_list = []
#     rgb_values = {}

#     for i in range(10):
#         segment = image[ypos:ypos+10, xpos-10:xpos+10]
#         mean_colour = np.mean(segment, axis=(0, 1)).astype(int)
#         mean_colour_list.append(mean_colour)
#         ypos += segment_height

#     value_list = ['URO', 'BIL', 'KET', 'BLD',
#                   'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

#     for i, colour_value in enumerate(mean_colour_list):
#         rgb_values[value_list[i]] = colour_value.tolist()[::-1]

#     return rgb_values

import cv2
import numpy as np


async def colour_analyzer(filepath):
    # Load the image
    image = cv2.imread(filepath)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return None
    
    # Resize the image as in the original code
    temp_image = image[50:1000, 150:175]
    height, width, _ = temp_image.shape
    temp_image = cv2.resize(temp_image, dsize=(width*2, height))

    segment_height = 90
    # Define the list of labels
    value_list = ['URO', 'BIL', 'KET', 'BLD',
                  'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

    rgb_values = {}

    for i in range(10):
        ypos = i * segment_height
        xpos = width // 2  # Center of the left half of the image
        segment = temp_image[ypos:ypos+10, xpos:xpos+10]
        mean_colour = np.mean(segment, axis=(0, 1)).astype(int)
        label = value_list[i]
        rgb_values[label] = mean_colour.tolist()[::-1]


    return rgb_values
