### Pasos iniciales para setear un entorno jupyter en Ubuntu

### 1.

Instalar en caso de no tener los siguentes paquetes instalados:
- python3
- python3-pip
- python3-dev

__$ sudo apt update__

__$ sudo apt install python3-pip python3-dev__

### 2.

Actualizar pip e instalar virtualenv:
__$ sudo -H pip3 install --upgrade pip__

__$ sudo -H pip3 install virtualenv__

### 3.

Con el virtualenv ya instalado podemos definir nuestro directorio donde guardaremos nuestros proyectos.

__$ mkdir directorio__

__$ cd directorio__

__$ virtualenv virtualEnvironmentName__

Antes de instalar jupyter es necesario iniciar el virtualenv:

__$ source virtualEnvironmentName/bin/activate__

### 4. Instalar jupyter:

Una vez activado el virtualenv estariamos dentro de este entorno creado donde podemos instalar el paquete jupyter e iniciarlo via comandos:

__$ pip install jupyter__

Para ejecutar jupyter:

__$ jupyter notebook__