import cv2
import face_recognition as fr



#cargar imagenes
foto_1 = fr.load_image_file(r"C:\Users\lomel\Desktop\Biometria facial\imagenes\Miguel.jpg")
foto_2 = fr.load_image_file(r"C:\Users\lomel\Desktop\Biometria facial\imagenes\santiago_lomeli.jpg")

#pasar imagenes a rgb
foto_1 = cv2.cvtColor(foto_1, cv2.COLOR_BGR2RGB)
foto_2 = cv2.cvtColor(foto_2, cv2.COLOR_BGR2RGB)

#localizar cara control
lugar_cara_A = fr.face_locations(foto_1)[0]
cara_codificada_A = fr.face_encodings(foto_1)[0]

lugar_cara_B = fr.face_locations(foto_2)[0]
cara_codificada_B = fr.face_encodings(foto_2)[0]

# mostrar rectangulo
cv2.rectangle(foto_1,
            (lugar_cara_A[3], lugar_cara_A[0]),
            (lugar_cara_A[1], lugar_cara_A[2]),
            (0, 255, 0),
            2)

cv2.rectangle(foto_2,
            (lugar_cara_B[3], lugar_cara_B[0]),
            (lugar_cara_B[1], lugar_cara_B[2]),
            (0, 255, 0),
            2)


# realizar comparacion 
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)


# medida de distancia
# se puede agregar tolerancia al final                              ! aqui 
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B, )

# mostrar resultado
cv2.putText(foto_2,
            f'{resultado}{distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0,
            2))


# mostrar imagen
cv2.imshow('Foto control', foto_1)
cv2.imshow('Foto prueba', foto_2)


# mantener programa abierto
cv2.waitKey(0)