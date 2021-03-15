## Pasos para configurar y probar tu camera si funciona:

### 1. Listar todos los dispositivos que tenemos conectados a la placa:

__$ !ls -ltrh /dev/video*__

### 2. Crear el objeto camera importando de la libreria:

```python

from jetcam.csi_camera import CSICamera

camera = CSICamera(width=224, height=224, capture_device=0) # confirm the capture_device number

```

#### Una vez capturado el objeto camera podemos capturar y leer un frame de la camara con el siguente script de python:

```python

image = camera.read()

print(image.shape)

```

La salida de este print devuelve los pixeles de height, los pixeles de weidth y el numero de colores channels.

### 3. Crear un widget para ver el frame capturado:

```python

import ipywidgets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg

image_widget = ipywidgets.Image(format='jpeg')

image_widget.value = bgr8_to_jpeg(image)

display(image_widget)

```

### 4. Ejecutar el metodo update_image que es una callback function que se subscribe al valor cambiante de las imagenes enseñandolas por pantalla:

```python

camera.running = True

def update_image(change):
    image = change['new']
    image_widget.value = bgr8_to_jpeg(image)
    
camera.observe(update_image, names='value')

```

En el caso en que se quiera apagar la transmision hay que ejecutar un unsubscribe:

```python

camera.unobserve(update_image, names='value')

```

### 5. Se puede transmitir el video de la camara atraves de otro metodo __dlink__:

```python

import traitlets

camera_link = traitlets.dlink((camera, 'value'), (image_widget, 'value'), transform=bgr8_to_jpeg)

```

Al igual que anteriormente se puede eliminar con el metodo __unlink()__:

```python

camera_link.unlink()

```

y reconectar again:

```python

camera_link.link()

```

### 6. Por ultimo es necesario apagar los recursos de la camera cuando no se estan usando:

```python

# Attention!  Execute this cell before moving to another notebook
# The USB camera application only requires that the notebook be reset
# The CSI camera application requires that the 'camera' object be specifically released

camera.running = False
camera.cap.release()

```
