import picamera
from time import sleep
import tkinter

def quit():
    camera.stop_preview()
    global tkTop
    tkTop.destroy()

def setBrightness(ev=None):
    global camera
    global tkScale
    camera.brightness = tkScale.get()

def setContrast(ev=None):
    global camera
    global tkScale
    camera.contrast = tkScale.get()

camera = picamera.PiCamera()
camera.start_preview()
camera.brightness = 50
camera.contrast = 0

#Rahmen_Einstellungen
tkTop = tkinter.Tk()
tkTop.wm_title("Settings")
tkTop.geometry('400x300')

#Button_EXIT
tkButtonQuit = tkinter.Button(
    tkTop, text="EXIT", command=quit)
tkButtonQuit.pack()

#Schieberegler_Helligkeit
tkScale = tkinter.Scale(
    tkTop,
    from_=0, to=100,
    length=100,
    orient=tkinter.HORIZONTAL,
    command=setBrightness)
tkScale
tkScale.set(50)
tkScale.pack(anchor=tkinter.CENTER)


#Schieberegler_Kontrast
tkScale = tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=200,
    orient=tkinter.HORIZONTAL,
    command=setContrast)
tkScale
tkScale.set(0)
tkScale.pack(anchor=tkinter.CENTER)



tkinter.mainloop()
