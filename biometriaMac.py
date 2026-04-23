import cv2
import face_recognition as fr
import os
import numpy

# 1. Configuración de base de datos
ruta = 'imagenes'
mis_imagenes = []
nombres_personas = []

if not os.path.exists(ruta):
    os.makedirs(ruta)
    print(f"Creada la carpeta '{ruta}'. Agrega fotos ahí y reinicia.")

lista_personas = [f for f in os.listdir(ruta) if not f.startswith('.')]

for nombre in lista_personas:
    imagen_actual = cv2.imread(os.path.join(ruta, nombre))
    if imagen_actual is not None:
        mis_imagenes.append(imagen_actual)
        nombres_personas.append(os.path.splitext(nombre)[0])

print(f'Personas cargadas: {nombres_personas}')

# 2. Función para codificar
def codificar(imagenes):
    lista_codificada = []
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen)
        if len(codificado) > 0:
            lista_codificada.append(codificado[0])
    return lista_codificada

print("Codificando fotos... espera un momento.")
lista_personas_codificada = codificar(mis_imagenes)
print("Codificación finalizada.")

# 3. Captura de video en tiempo real
captura = cv2.VideoCapture(0)

while True:
    exito, imagen = captura.read()

    if not exito:
        print('No se ha podido acceder a la cámara.')
        break

    # Reconocer caras en el frame actual
    caras_ubicaciones = fr.face_locations(imagen)
    caras_codificadas = fr.face_encodings(imagen, caras_ubicaciones)

    for caracodif, caraubic in zip(caras_codificadas, caras_ubicaciones):
        distancias = fr.face_distance(lista_personas_codificada, caracodif)
        
        if len(distancias) > 0:
            indice_coincidencia = numpy.argmin(distancias)

            if distancias[indice_coincidencia] < 0.6:
                nombre = nombres_personas[indice_coincidencia]
                color = (0, 255, 0) # Verde si lo conoce
            else:
                nombre = "Desconocido"
                color = (0, 0, 255) # Rojo si no

            # Dibujar rectángulo y nombre
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), color, 2)
            cv2.putText(imagen, nombre, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)

    # Mostrar imagen
    cv2.imshow('Reconocimiento Facial (Presiona ESC para salir)', imagen)

    # Frenar el bucle con la tecla ESC
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# Limpieza
captura.release()
cv2.destroyAllWindows()