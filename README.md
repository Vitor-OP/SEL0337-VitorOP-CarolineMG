# SEL0337-VitorOP-CarolineMG
> SEL0337 - Applications of Microprocessors II
> 
> Caroline Meireles Grupe, n° USP: 11801081     
> Vitor Odorissio Pereira, n° USP: 11800782


Repository created to utilise and understand the functions of Git and GitHub for the practice 6 in the SEL0337 course given by  Prof. Pedro de Oliveira Conceição Junior.



---

## Practice 6
> Computational vision, version control system (Git) and public APIs

This practice is intended for:
- familiarize with raspberryPi accessories -such as the camera module
- understand the utilisation of public APIs.
- learn how to use Git and GitHub

### Camera module
> Simple code that just access the camera, takes a picuture and record a video.

Utilizing the function `PiCamera()` from the library `picamera` its able to define the class `picamera` as `camera`. Along that, the methods `start_preview()`, `annotate_text`, `capture()`, and `stop_preview` were utilized to enhance the functionality of the module.

Also were utilized the function `sleep` from lib `time` to make the camera humanly manageble.

```py
camera = PiCamera()

camera.start_preview()
camera.annotate_text = "Carol_11801081_Vitor_11800782"
sleep(5)
camera.capture('/home/sel/Desktop/pratica6_cavi/foto_modificada2.jpg')
camera.stop_preview()
```
This code opens a preview for 5 seconds of the camera, marks the image with the text given, takes the picture and then closes the preview. Very straght foward, giving the following result:

<img src="https://raw.githubusercontent.com/Vitor-OP/SEL0337-VitorOP-CarolineMG/main/photo.jpg" width=70% height=70%>

Then, it records a video for 7 seconds, utilizing the `start_recording()` methode and the `stop_recording` methode:

```py
camera.start_recording('/home/sel/Desktop/pratica6_cavi/video.h264')
sleep(7)
camera.stop_recording()
```
Which created the video.h264 file of the following recording ~~converted and compacted externaly to be presented in this document~~:

<img src="https://github.com/Vitor-OP/SEL0337-VitorOP-CarolineMG/blob/main/gif_compacted.gif?raw=true" width=70% height=70%>

### Weather API
> Basic code for dealing with json files from a public API:

Utilizing the function `get` from the library `request`, expecialized in reatriving information from the internet, and the `json` library, used to manipulate the scrapped data; the code to collect and show the data from a weather station was very short and simple:

```py
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/' #API from the weather data and selecting its last transmission

closest_stn = 966583 #selecting the weather station

weather = weather + str(closest_stn) #unifying both strings of the API address

my_weather = get(weather).json()['items'] #function to scrap the data
pprint(my_weather) #function to print it on the screen
```

This simple code would return the following data:
```
{'air_pressure': 1010.51,
 'air_quality': 48.8,
 'ambient_temp': 29.93,
 'created_by': 'UFSC',
 'created_on': '2018-09-27T16:10:21Z',
 'ground_temp': 23.06,
 'humidity': 46.42,
 'id': 13228613,
 'rainfall': 0,
 'reading_timestamp': '2018-09-27T16:10:21Z',
 'updated_by': 'UFSC',
 'updated_on': '2018-10-04T15:35:19.899Z',
 'weather_stn_id': 966583,
 'wind_direction': 90,
 'wind_gust_speed': 0,
 'wind_speed': 0}
<class 'dict'>
```

