from PIL import Image,ImageEnhance,ImageFilter
import os
path = r'C:\Users\aniru\OneDrive\Code\PYTHON\Games\Image'
pathOut = r'C:\Users\aniru\OneDrive\Code\PYTHON\Games\ImageOut'

# for filename in os.listdir(path):
#     img = Image.open(f"{path}\{filename}")
#     print(img.format, img.size, img.mode)

#     edit = img.filter(ImageFilter.SHARPEN).convert('L')
#     factor = 1.5
#     enhancer = ImageEnhance.Contrast(edit)
#     edit = enhancer.enhance(factor)
#     clean_name = os.path.splitext(filename)[0]
#     edit.save(f'{pathOut}/{clean_name}_edited.png')
#     # edit.show()


# for filename in os.listdir(path):
#   size = (128,328)
#   img = Image.open(f'{path}\{filename}')
#   edit = img.filter(ImageFilter.SHARPEN).convert('L').copy()
#   edit.thumbnail(size)
#   clean_name = os.path.splitext(filename)[0]
#   # edit.save(f'{pathOut}/{clean_name}_edited.png')
#   edit.save(f'{pathOut}/{clean_name}_edited.png')

for filename in os.listdir(path):
    img = Image.open(f"{path}\{filename}")
    box = (0 , 0 , 2000 , 3000)
    region = img.crop(box)
    clean = os.path.splitext(filename)[0]
    region.save(f'{pathOut}/{clean}_edited.jpg')
