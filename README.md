# How use Instagram API Graph version 14 in Python
Little code related to Instagram API writing in Python. 

Limitaciones de la API.
Instagram API Graph de momento no soporta subir archivos locales --por lo que-- las imagenes deben estar alojadas en la red y ser de acceso público.
No se admiten las cuentas de creador de Instagram.
Las cuentas pueden realizar un máximo de 25 publicaciones a través de la API en un período de 24 horas.
Las publicaciones por secuencia (reels) cuentan como una única publicación.
JPEG es el único formato de imagen admitido. Los formatos de JPEG extendido, como MPO y JPS, no son compatibles.
No se admiten las historias.
No se admiten las etiquetas de compra.
No se admiten las etiquetas de contenido de marca.
No se admiten los filtros.
El símbolo de hashtag (#) debe tener codificación URL HTML como %23 en la leyenda.
No se admiten publicaciones en Instagram TV.
Primeros pasos:
Cómo buena práctica en Python se recomienda utilizar entornos virtuales como workspace, estos te permitirán, trabajar en entornos separados entre sí, con librerias especificas para cada proyecto.

Crearemos el entorno virtual de trabajo.
```
python -m venv API-Instagram 
#Nos movemos a la carpeta creada.
cd .\API-Instagram\ 
#Activamos en entorno
.\Scripts\Activate.ps1
```
shell python
En este caso, estoy trabajando en entorno Windows, si necesitas saber como crear entornos virtuales en otros sistemas operativos te dejo en enlace a la documentación.
Una vez activado, crearemos una carpeta de recursos llamado src.
```
 mkdir src
 ```
 

También instalaremos los paquetes necesarios, en este caso requests y python-dotenv
```
pip install requests
pip install python-dotenv
```
Con esto ya tenemos los más básico, utilizaremos la librería request para utilizar los métodos HTTP; Get y Post.

Generalidades
El proceso de publicación cuenta con dos pasos, el primero es crear un contenedor media que nos devolverá una ID. Este contenedor almacenará la url de la imagen que hemos seleccionado y finalmente publicaremos ese contenedor.

En la carpeta src, crearemos un archivo al que llamaremos app.py
```
#app.py

def main():
    #Publish a new instagram post - Max post per day is 25!-
    fn.publish_container()


if __name__ == '__main__':
    print('Iniciando proceso espere un momento ...')
    main()
```
También crearemos el archivo .env que almacenará las variables de entorno, en este caso los datos del Instagram Bussiness ID y el token. Procura, almacenarlo fuera de la ruta raíz. Si utilizas Git/Git-hub/Gitlab, evitaras que puedas compartir esta información en tus repositorios públicos.

```
# environment variables defined inside a .env file
API_TOKEN='&access_token=EAAKYuskeIxcBAFj9zJrtB...'
API_IG_ID='17382764539239043'
		   
```
Si quieres saber qué otros usos puedes darle a esta librería revisa su documentación oficial.
```
python-dotenv
Read key-value pairs from a .env file and set them as environment variables
```

Para terminar crearemos el archivo que contendrá las funciones y librerías necesarias, en este caso lo he llamado functions.py

Importando librerías y las variables de entorno.
En esta primera parte, importaremos las librerías previamente instaladas; Requests y OS que nos servirá para instanciar en método de clase load_dotenv().
```
#funtions.py
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_token=os.getenv('API_TOKEN')
api_ig_id=os.getenv('API_IG_ID')
```
Como se indicó anteriormente, este proceso consta de dos pasos, crear el ID del contenedor y crear el ID de la publicación.

Definimos las constantes.
```
#funtions.py
#API endpoints
url_graph= 'https://graph.facebook.com/'
version_graph = 'v14.0/'
media = '/media?image_url=https://webpage.com/my.jpg'
caption = '&caption= This picture is awesome %23Pythonrules'
```
Ten en cuenta que la estructura del endpoint para crear la id del contenedor es de la siguiente forma:

💡
ig-user-id es la ID de instagram, y user_token_from_api es el token de acceso.
```
# API endpoints
# Using method POST https://graph.facebook.com/v14.0/{ig-user-id}/media?image_url=http.urlimage.jpg&caption={caption hashtag simbol = %23}&access_token=user_token_from_api
```

Métodos o funciones

La función get_container_id() creará el contenedor, y retornará la id.
```
#funtions.py

def get_container_id(): # This get and set the Containter ID
    print('Obteniendo ID de contenedor... espere un momento:')
    #url = create_container()
    res = requests.post(url_container)
    ig_container_id = res.json()
    print(ig_container_id)
    status = res.status_code
    if status == 200:
            print('processing status ok! ...')
            print(url_container)
            container_id = ig_container_id['id']
    else:
            print('Error: ',res)
        
    return container_id
```
La función publish_container(), publicará el contenedor media.
```
#funtions.py

def publish_container(): # Publish the container created before using POST method.
        try:
            ig_container_id = create_container_id()
            url = base_url+media_publish+ig_container_id+token
            print(f'Url del publish {url}')
            res = requests.post(url)
            print(f' res del publish {res}')
            #verify resquest if status is 200 is Ok!
            status = res.status_code
            if status == 200 : 
                ig_publish_id = res.json()
                ig_publish_id = str(ig_publish_id['id'])
                permalink_url = get_permalink(ig_publish_id)
                print (f'Publicación exitosa! {status}')
            else:
                print(f'Error: {status} : {ig_publish_id}')

        except:
        		print(f'Error: {status} : {res}')
            return 
```
La función get_permalink() permite obtener el permalink de la publicación. El permalink es la url definitiva, visible a los usuarios de Instagram : https://www.instagram.com/p/ChSCjDQsaYQ/
```
#funtions.py

def get_permalink(permalink): # Get the permalink of the publish.
    permalink = permalink
    res = requests.get(url_permalink+permalink+'?fields=permalink'+api_token)
    status = res.status_code
    permalink_url = res.json()
    if status == 200:
        print ('Obteniendo Permalink')
        permalink_url = permalink_url['permalink']
        print (permalink_url)
    else:
        print('Error', res) 
    return permalink_url
```
Si todo sale bien, cuando ejecutes la aplicación deberás visualizar algo como esto.
```
Obteniendo ID de contenedor... espere un momento:
{'id': '17937773603175978'} #<--------ID Contenedor
processing status ok! ...
https://graph.facebook.com/v14.0/17382764539239043/media?image_url=https://upload.wikimedia.org/wikipedia/commons/a/a3/June_odd-eyed-cat.jpg&caption= This cat is awesome %23Pythonrules&access_token=EAA...lB

Url de la publicación (https://graph.facebook.com/v14.0/17382764539239043/media_publish?creation_id=1738276453923908&access_token=EAAKo...B)

Estado de la públicación <Response [200]>
Obteniendo Permalink
https://www.instagram.com/p/HKRyskzNbu_/
Publicación exitosa! 200
```
Códigos de respuesta:
Estado 200 indica que la solicitud fue procesada con éxito. Mientras el estado 400 indica que algo falló.  Puedes conocer los detalles que se almacenan en la variable res.

Ten siempre en cuenta que solo tienes un máximo de 25 publicaciones cada 24 horas.
