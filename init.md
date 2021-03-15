## Pasos para configurar el setup de la placa jetson nano.

### 1. Descargar la imagen del software de la placa de la pagina oficial. Es recomendable descargar una imagen que tenga el set de herramientas de Jetpack, para este documento es la version 4.5.1.


### 2. Quemar la imagen en una micro SD de 64 GB minimo, para garantizar un espacio suficiente para las aplicaciones como para los datos.

### 3. Introducir la micro SD en la placa. Conectar un monitor un teclado y raton. Seguir los pasos iniciales como aceptar la politica y setear el teclado y la region. 

### 4. Una vez el SO este iniciado abrimos una terminal y agregamos el siguente comando:

__$ free -m__

Nos permitira conocer el estado de memoria de mis archivos, alli localizamos un archivo especial llamado swap.
Si este archivo no tiene una memoria de 4GB habra que setearla manualemte, mediante los siguentes pasos:

#### Disable ZRAM:

__$ sudo systemctl disable nvzramconfig__

#### Create 4GB swap file

__$ sudo fallocate -l 4G /mnt/4GB.swap__

__$ sudo chmod 600 /mnt/4GB.swap__

__$ sudo mkswap /mnt/4GB.swap__

#### Append the following line to /etc/fstab

__$ sudo echo "/mnt/4GB.swap swap swap defaults 0 0" >> /etc/fstab__

#### If you have problems with the permission in the last step execute first the sudo comando and then execute the specific command:

__$ sudo su__

__$ sudo echo "/mnt/4GB.swap swap swap defaults 0 0" >> /etc/fstab__

Como paso final reinicia la placa mediante:

__$ sudo reboot now__

### 5. Accede a la placa de manera remota mediante el protocolo _SSH_ conectando un cable microusb del ordenador a la placa, de esta manera se podra conectar mediante el comando _ssh_ a la direccion especifica __192.168.55.1__ sin necesidad de que la placa este conectada a internet y tenga que tener una direccion IP.

__$ ssh user@192.168.55.1__

#### Creamos un directorio para despues cuando ejecutemos _docker_ hagamos un link a este directorio:

__$ mkdir -p ~/nvdli-data__

#### Ahora ya estamos listos para ejecutar una imagen de docker. En este caso es importante estar conectado a internet porque si no encuentra la imagen la va a tener que descargar, todos los paquetes la primera vez, despues da igual estar conectado a la red.

```
sudo docker run --runtime nvidia -it --rm --network host \
    --volume ~/nvdli-data:/nvdli-nano/data \
    --device /dev/video0 \
    nvcr.io/nvidia/dli/dli-nano-ai:<tag>
```

En este caso la palabra tag se refiere a una version del codigo compatible con el sistema operativo JetPack L4T instalado. Muy importante enconetrar la version compatible, si no no ejecutara el contenedor.

#### Ejemplo de ejecucion de docker a un conetendor con la placa conectada a una camara mediante CSI:

```

echo "sudo docker run --runtime nvidia -it --rm --network host \
    --volume ~/nvdli-data:/nvdli-nano/data \
    --volume /tmp/argus_socket:/tmp/argus_socket \
    --device /dev/video0 \
    nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0" > docker_dli_run.sh

```

#### Le concedemos privilegios de ejecucion:

__$ chmod +x docker_dli_run.sh__

#### Ejecutamos el conetendor mediante la shell creada:

__$ ./docker_dli_run.sh__

### Abrimos un navegador y accedemos a la direccion de __192.168.55.1:8888__ donde nos pedira una contraseña _dlinano_

Se ejecutara _JupiterLab_ y podremos acceder al proyecto.

