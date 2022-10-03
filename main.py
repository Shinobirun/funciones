
def anioBisiesto(anio):
    if anio == 0 and (anio % 400) == 0:
        print('es bisiesto')
    elif (anio % 4) == 0:
        print("es bisiesto")
    else:
        print('no es bisiesto')

fecha =  input('ingrese un año ')
fecha= int(fecha)
anioBisiesto(fecha)