# aqui ponemos los funciones de gdal que estabamos usando en el notebook...

import numpy as np
import gdal
# y las demas que necesitamos para hacer el ndvi, evi, savi, etc...

def classifyImage(image):
    zona_urbana = np.where((image>=-1)&(image<=1),arr,0) # hay que cambiar el 1 y -1 por el rango de las zonas urbanas
    zona_natural = np.where((image>=-1)&(image<=1),arr,0) # hay que cambiar el 1 y -1 por el rango de las zonas naturales
    return zona_urbana, zona_natural

def compareImages(image1, image2):
    # pasa los dos imagenes para obtener la diferencia entre los dos, pixel por pixel
    img1 = gdal.Open(image1)
    img2 = gdal.Open(image2)
    i1 = img1.GetRasterBand(1).ReadAsArray(0, 0, img1.RasterXSize, img1.RasterYSize)
    i2 = img2.GetRasterBand(1).ReadAsArray(0, 0, img2.RasterXSize, img2.RasterYSize)
    diff = i1 - i2
    return diff

def compareArrays(arr1, arr2):
    # si tiene los resultos como arrays, usa este funcion
    diff = arr1 - arr2
    return diff