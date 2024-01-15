import json
import zipfile
import os

api_token= {"username":"miguelngelmerabarco","key":"26c356252225969ad268666e5a7d1cdd"} ##Contenido de archivo kaggle.json

##Conectar a kaggle

with open("C:/Users/migue/.kaggle/kaggle.json", "w") as file:
    json.dump(api_token, file)

##Poner la ruta de la carpeta dataset que se ha creado previamente
    
location = "C:/Users/migue/OneDrive/Documentos/trabajo_final2/dataset"

##validar que la carpeta existe

if not os.path.exists(location):
    ##si no existe la carpeta dataset entonces la creo
    os.mkdir(location)
else:
    ##si la carpeta si existe, entonces voy a borrar su contenido
    for root, dirs, files in os.walk (location, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name)) ##elimino todos los archivos
            for name in dirs:
                os.rmdir(os.path.join(root,name))##elimino todas las carpetas

##descargar dataset de kaggle
os.system("kaggle datasets download -d hummaamqaasim/jobs-in-data -p C:/Users/migue/OneDrive/Documentos/trabajo_final2/dataset")

##Descomprimir el archivo
os.chdir(location)

for file in os.listdir():
    zip_ref= zipfile.ZipFile(file,"r") ##lee archivo zip
    zip_ref.extractall() ##extrae contenido de archivo zip
    zip_ref.close() ##Cierra archivo
