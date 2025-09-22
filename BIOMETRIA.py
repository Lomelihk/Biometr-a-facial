import cv2
import face_recognition as fr
import os
import numpy


# creamos base de datos
ruta = 'imagenes'
mis_imagenes = []
nombres_personas = []
lista_personas = os.listdir(ruta)

for nombre in lista_personas:
    imagen_actual = cv2.imread(f'{ruta}\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_personas.append(os.path.splitext(nombre)[0])

print(nombres_personas)

# codificar imagenes

def codificar(imagenes):

    # crear lista nueva
    lista_codificada = []
    #pasar todas las imagenes en rgb

    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar 
        codificado = fr.face_encodings(imagen)
        if len(codificado) > 0:
        #agregar a la lista

            lista_codificada.append(codificado[0])
    # devolver lista codificada

    return lista_codificada


lista_personas_codificada = codificar(mis_imagenes)

# tomar imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('No se a podido tomar la captura')
else:
    # reconocer cara captura
    cara_captura = fr.face_locations(imagen)

    # codificar cara
    cara_capturada_codificada = fr.face_encodings(imagen, cara_captura)

    #buscar conincidencias
    for caracodif, caraubic in zip(cara_capturada_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_personas_codificada, caracodif)
        distancias = fr.face_distance(lista_personas_codificada, caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguna persona")
        else:
            #buscar el nombre de la persona encontrada

            nombre = nombres_personas[indice_coincidencia]

            y1, x1, y2, x2 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

            #mostrar coincidencias

            cv2.imshow('Imagen web', imagen)

            #mantener ventana abierta
            cv2.waitKey(0)