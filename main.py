#bibliotecas para utilizar a camera(periférico):
from picamera import PiCamera
from time import sleep

camera = PiCamera() #a função Picamera foi definida como "camera" e os comandos dela podem ser utilizados

camera.start_preview() #inicia a visualização da camera
camera.annotate_text = "Carol_11801081_Vitor_11800782" #anota o texto na imagem capturada
sleep(5) #mantem a visualização por 5 segundos
camera.capture('/home/sel/Desktop/pratica6_cavi/foto_modificada2.jpg') #faz a captura d aimagem e guarda na pasta selecionada
camera.stop_preview()#para a visualização

camera.start_recording('/home/sel/Desktop/pratica6_cavi/video.h264') # inicia a gravação de um vídeo
sleep(7) #mantem por 7 segundos
camera.stop_recording() #finaliza a gravação


#módulos para usar com os APIs de clima:
from requests import get
import json
from pprint import pprint

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations' #URL da API com todas as estações do planeta
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/' #URL da API com últimos dados do clima da estação escolhida

closest_stn = 966583 #pegando dados da estação da UFSC

weather = weather + str(closest_stn) #colocando o valor da ID da estação escolhida ao fim do link para API weather para pegar os dados somente dessa estação

my_weather = get(weather).json()['items'] #pegar o clima da estação escolhida e por nessa variável em modo de lista dos itens
pprint(my_weather) # printar os dados