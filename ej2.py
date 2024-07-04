from PIL import Image
import os

img_route = input('Ingresa la ruta de la imagen: ')

imagen = Image.open(img_route)

imagen.show()

for i in range(1, 100):        
    if(os.path.exists(f'mate{i}.jpg')):
        imagen.save(f'mate{i+1}.jpg')
        break
    else:
        imagen.save('mate1.jpg')