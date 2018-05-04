from PIL import Image
import os


size = (1024)
filelocation = 'images/'

for f in os.listdir(filelocation):
    f = f.lower()
    if f.endswith('.jpeg'):
        print(f)
        image = Image.open(filelocation + f)
        fn, fext = os.path.splitext(f)
        image.thumbnail(size, size)
        image.save('{}/{}.jpg'.format(size, fn))

    elif f.endswith('.png'):
        print(f)
        image = Image.open(filelocation + f)
        fn, fext = os.path.splitext(f)
        rgb = image.convert('RGB')
        rgb.thumbnail(size, size)
        rgb.save('{}/{}.jpg'.format(size, fn))
