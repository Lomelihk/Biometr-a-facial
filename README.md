# Biometría Facial

Sistema de reconocimiento facial en tiempo real usando Python, OpenCV y `face_recognition`. Compara el rostro capturado por la webcam contra una base de datos de imágenes de referencia e identifica a la persona.

## Características

- Reconocimiento facial en tiempo real desde la webcam
- Codificación y comparación de rostros con tolerancia configurable
- Dos versiones: Windows (`BIOMETRIA.py`) y macOS (`biometriaMac.py`)
- La versión macOS crea automáticamente la carpeta `imagenes/` si no existe
- Muestra el nombre de la persona reconocida sobre el recuadro del rostro

## Tecnologías

| Librería | Uso |
|---|---|
| `opencv-python` | Captura de video y procesamiento de imagen |
| `face_recognition` | Codificación y comparación de rostros |
| `numpy` | Operaciones vectoriales |

## Instalación

```bash
# Instalar dependencias
pip install opencv-python face_recognition numpy

# En macOS puede requerir cmake y dlib primero
brew install cmake
pip install cmake dlib
pip install face_recognition
```

## Uso

1. Agrega fotos de referencia en la carpeta `imagenes/` (una foto por persona, nombre del archivo = nombre de la persona)

```
imagenes/
├── Juan.jpg
├── Maria.png
└── Pedro.jpg
```

2. Ejecuta el script según tu sistema operativo:

```bash
# macOS
python biometriaMac.py

# Windows
python BIOMETRIA.py
```

3. Apunta la webcam hacia un rostro. Si coincide con alguna imagen de referencia, aparecerá el nombre sobre el recuadro.

## Estructura del proyecto

```
Biometr-a-facial/
├── BIOMETRIA.py        # Versión Windows
├── biometriaMac.py     # Versión macOS (recomendada)
├── main.py             # Punto de entrada alternativo
├── imagenes/           # Carpeta de imágenes de referencia (ignorada en git)
└── .gitignore
```

## Notas

- La carpeta `imagenes/` está excluida del repositorio por privacidad. Créala localmente y agrega tus propias imágenes de referencia.
- El reconocimiento funciona mejor con fotos de buena iluminación y el rostro de frente.
- En macOS, si la webcam no abre, asegúrate de dar permisos de cámara a la terminal.
