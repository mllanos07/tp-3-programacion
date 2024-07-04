from PIL import Image

rutaImg = input('ingrese la ruta de la imagen:')
rutataMarca = input('ingrese la ruta de  la marca de agua: ')

img = Image.open(rutaImg)
marca = Image.open(rutataMarca)

anchoImg, altoImg = img.size
width, hight = marca.size

margen = 50

print(f'el ancho es: {anchoImg} y el alto es: {altoImg}')

print(f'1: Superior izquierda, 2: Superior derecha, 3: Inferior izquierda, 4: Inferior derecha')
ubicacion = input('eliga ubicacion marca de agua:')

if ubicacion == '1' :
  img.paste(marca, (margen, margen))
elif ubicacion == '2' :
  img.paste(marca, (anchoImg - width - margen, margen))
elif ubicacion == '3' :
  img.paste(marca, (margen, altoImg - hight - margen))
elif ubicacion == '4' :
  img.paste(marca, (anchoImg - width - margen, altoImg - hight - margen))
else :
  print('error')

img.save('pasted.png')
img.show