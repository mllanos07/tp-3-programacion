from PIL import Image
import os

direct = input("pegue la direccion de la imagen:")

img = Image.open(direct)

if img.mode != 'RGB':
    img = img.convert('RGB')

imagen = Image.new("RGB", img.size)

pixelesOriginales = img.load()
pixeles = imagen.load()

for y in range(img.height):
  for x in range(img.width):
    r, g, b = pixelesOriginales[x, y]
    gris = int((r + g + b) / 3)
    pixeles[x, y] = (gris, gris, gris)

if not os.path.exists('ImagenesFiltradas') :
    os.makedirs('ImagenesFiltradas')

nombre, extension = os.path.splitext(os.path.basename(direct))
print(nombre)
print(extension)

nuevoNombre = 'ImagenesFiltradas/' + nombre + 'BN' + extension
print(nuevoNombre)


imagen.save(nuevoNombre)

pixeles.show