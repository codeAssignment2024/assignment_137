import time
current_time = int(time.time())
genetated_number = (current_time % 100) + 50
if genetated_number % 2 == 0:
    genetated_number += 10

from PIL import Image
img = Image.open('chapter1.jpg')
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (min(255, r + genetated_number), min(255, g + genetated_number), min(255, b + genetated_number))

img.save('chapter1out.png')

red_sum = 0

for i in range(img.width):
    for j in range(img.height):
        r, _, _ = pixels[i, j]
        red_sum += r
print(red_sum)

