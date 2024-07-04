from PIL import Image
import os

img_ruta = input('Ingresa la ruta de la carpeta: ')
alto = int(input('Ingresa la resolución deseada en alto: '))
ancho = int(input('Ingresa la resolución deseada en ancho: '))

 
img_lista = []

for img in img_lista:
    img = Image.open(img_ruta + img)

def resize():
    if width > height:kk
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

    # Resize the image.
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))
