import requests
import os
from dotenv import load_dotenv
#Load .env variables.
load_dotenv()
api_token=os.getenv('API_TOKEN')
api_ig_id=os.getenv('API_IG_ID')
#Create stactic URL variable
url_graph= 'https://graph.facebook.com/'
version_graph = 'v14.0/'
media = '/media?image_url=https://upload.wikimedia.org/wikipedia/commons/a/a3/June_odd-eyed-cat.jpg'
media_publish='/media_publish?creation_id='
caption = '&caption= This cat is awesome %23Pythonrules'
#Create Container
# REF: https://developers.facebook.com/docs/instagram-api/guides/content-publishing/
# Endpoint
# Using method POST https://graph.facebook.com/v14.0/{ig-user-id}/media?image_url=http.urlimage.jpg&caption={caption hashtag simbol = %23}&access_token=user_token_from_api


#Url base & Url container
urlbase = url_graph+version_graph+api_ig_id   #https://graph.facebook.com/v14.0/{ig-user-id}/
url_container = urlbase+media+caption+api_token #https://graph.facebook.com/v14.0/{ig-user-id}/media?image_url=http.urlimage.jpg&caption={caption hashtag simbol = %23}&access_token=user_token_from_api
url_permalink = url_graph+version_graph

# Methods / funtions section:
def get_permalink(permalink): # This get the permalink of the publish.
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

def create_container_id(): # This get and set the Containter ID
    print('Obteniendo ID de contenedor... espere un momento:')
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

#Publish container media
# Use the POST /{ig-user-id}/media_publish endpoint to publish the container ID
# POST https://graph.facebook.com/v14.0/{ig-user-id}/media_publish?creation_id={ig-container-id}&access_token={user_token}

def publish_container(): # This publish the container create before and push using POST method
        try:
            ig_container_id = create_container_id()
            url = urlbase+media_publish+ig_container_id+api_token
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
            return 