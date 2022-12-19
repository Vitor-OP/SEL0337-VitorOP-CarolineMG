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
> very simple code that just access the camera, takes a picuture and record a video.

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

<img src="https://i.imgur.com/wZosJHb.jpg" width=70% height=70%>

Then, it records a video for 7 seconds, utilizing the `start_recording()` methode and the `stop_recording` methode:

```py
camera.start_recording('/home/sel/Desktop/pratica6_cavi/video.h264')
sleep(7)
camera.stop_recording()
```
Which created the video.h264 file of the following recording ~~converted and compacted externaly to .gif to be presented in this document~~:

<img src="https://github.com/Vitor-OP/SEL0337-VitorOP-CarolineMG/blob/main/video_3.gif?raw=true" width=50% height=50%>

### Weather API
> basic code for importing json files from a public API:

