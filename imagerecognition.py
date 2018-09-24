# 64 bit with pillow:
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
i = Image.open('images/dot.png')
iar = np.asarray(i)
print(iar)
plt.imshow(iar)
plt.show()
''' Here is a 3-dimensional array of the data. All of the data is the image, each matrix block is a row of data,
and each element within that is the pixel values in RGB-A (Red Green Blue Alpha).
So each pixel is measured in RBGA, so an example row is [255, 255, 255, 255], what does that mean?
This means we're looking at a 256-color image, since programming starts with a 0 rather than a 1.
This color means 255 red, 255 green, 255 blue, and then 255 Alpha.
Alpha is a measure of how opaque an image is.
The higher the number, the more solid the color is, the lower the number, the more transparent it is.'''
i1 = Image.open('images/dotndot.png')
iar1 = np.asarray(i1)
print(iar1)
plt.imshow(iar1)
plt.show()
#The idea of thresholding is to simplify the image. Some people particularly like the visual effect as well,
#  but we're interested in the simplifying aspect. An issue arises when we're trying to identify characters,
# shapes, objects, whatever, because there is a massive list of colors. Anything complex, to be analyzed, needs
#  to be broken down to the most basic parts.With thresholding, we can look at an image, analyze the "average" color,
# and turn that "average" into the threshold between white or black. Some thresholding wont go all of the way
# to either full black or white, there will be some gradient, but, for our basic purposes, we want to go all of the way!
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.asarray(i3)
plt.imshow(iar3)
print(iar3)
plt.show()
