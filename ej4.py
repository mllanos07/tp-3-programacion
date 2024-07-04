from PIL import Image
import os

rutaImg = input('Ingresa la ruta de la imagen: ')
x = int(input('Ingresa la coordenada X inicial: '))
y = int(input('Ingresa la coordenada y inicial: '))
ancho = int(input('Ingresa el ancho: '))
altura = int(input('Ingresa la altura: '))

imagen = Image.open(rutaImg)

nombre = 'Recortes'
path = '\\Users\Public\Documents\matias-llanos\programacion\programacion2\guia3'
rutaCompleta = os.path.join(path, nombre)

os.makedirs(rutaCompleta, exist_ok=True)

recorte = imagen.crop((x, y, ancho, altura))

for i in range(1, 100):        
    if(os.path.exists(f'recorte{i}.png')):
        recorte.save(f'recorte{i+1}.png')
        break
    else:
        recorte.save('recorte1.png')