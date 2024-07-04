from PIL import Image
from tabulate import tabulate
import os

img_route = input('Ingresa la ruta de la imagen: ')

imagen = Image.open(img_route)

nombre = os.path.basename(img_route)
extension = imagen.format
res = imagen.size
pixeles = res[0] * res[1]

imagen.show()

data = [
    ["Nombre", nombre],
    ["Extensión", extension],
    ["Resolución", res],
    ["Cantidad de píxeles", pixeles],
    ["Ruta", img_route]
]

print(tabulate(data))