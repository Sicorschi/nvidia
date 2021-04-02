from jetcam.csi_camera import CSICamera
import ipywidgets
from IPython.display import bgr8_to_jpeg


camera = CSICamera(width=224, height=224, capture_device=0)

image = camera.read()

print(image.shape)

image_widget = ipywidgets.Image(format='jpeg')

image_widget.value = bgr8_to_jpeg(image)

display(image_widget)

camera.running = True

def update_image(change):
    image = change['new']
    image_widget.value = bgr8_to_jpeg(image)
    
camera.observe(update_image, names='value')