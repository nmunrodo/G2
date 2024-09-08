import time
import numpy as np
import PIL
from PIL import Image

current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
n = (generated_number)

im = Image.open('chapter1.jpg')
r, g, b = np.array(im).T
r = r + n
g = g + n
b = b + n
im = Image.fromarray(np.dstack([item.T for item in (r,g,b)]))
im.save('chapter1out.png')

im2 = Image.open('chapter1out.png')
red, green, blue = im2.split()
red_img = Image.merge('RGB', (red, Image.new('L', im2.size), Image.new('L', im2.size)))
red_img.save('red_image.png')
rpix=list(red_img.getdata())
rpixrange=[x for sets in rpix for x in sets] 
sum_rpixrange=sum(rpixrange)
print(sum_rpixrange)