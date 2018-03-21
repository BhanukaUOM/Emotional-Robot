import RPi.GPIO as GPIO
import time
import speech_recognition as sr
import picamera, subprocess, os, sys
import threading

C_DATA = 23
C_STORE = 24
C_SHIFT = 25
R_DATA = 14
R_STORE = 15
R_SHIFT = 18

#Happy
h1= "happy"
h2= "like"
h3= "good"
h4= "nice"

#Sad
s1= "hate"
s2= "cry"
s3= "crying"
s4= "sad"

#Angry
a1= "hit"
a2= "kick"
a3= "kill"
a4= "angry"
a5= "goaway"
a6= "runaway"

#Love
l1= "love"
l2= "like"
l3= "sweety"

#Eye
e1= "lie"
e2= "joke"
e3= "nothing"

#Trunk
t1= "tasty"
t2= "sweet "
t3= "ice cream"
t4= "delicious"

#ohh
o1= "ohh"
o2= "wow"
o3= "beatufull"

def PinInit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(C_DATA, GPIO.OUT)
    GPIO.setup(C_STORE, GPIO.OUT)
    GPIO.setup(C_SHIFT, GPIO.OUT)
    GPIO.setup(R_DATA, GPIO.OUT)
    GPIO.setup(R_STORE, GPIO.OUT)
    GPIO.setup(R_SHIFT, GPIO.OUT)

def SendDataC(S_DATA):
    for num in range(0, 8):
        if(S_DATA & 0b10000000):
            GPIO.output(C_DATA, GPIO.HIGH)
        else:
            GPIO.output(C_DATA, GPIO.LOW)
            
        GPIO.output(C_SHIFT, GPIO.HIGH)
        GPIO.output(C_SHIFT, GPIO.LOW)
        S_DATA = S_DATA << 1
    StorePulseC()

def SendDataR(S_DATA):
    for num in range(0, 8):
        if(S_DATA & 0b10000000):
            GPIO.output(R_DATA, GPIO.LOW)
        else:
            GPIO.output(R_DATA, GPIO.HIGH)
            
        GPIO.output(R_SHIFT, GPIO.HIGH)
        GPIO.output(R_SHIFT, GPIO.LOW)
        S_DATA = S_DATA << 1
    StorePulseR()
    
def StorePulseC():
    GPIO.output(C_STORE, GPIO.HIGH)
    GPIO.output(C_STORE, GPIO.LOW)

def StorePulseR():
    GPIO.output(R_STORE, GPIO.HIGH)
    GPIO.output(R_STORE, GPIO.LOW)

def Send(row, column):
    SendDataC(0b00000000)
    if(row==1):
        SendDataR(0b00000001)
    elif(row==2):
        SendDataR(0b00000010)
    elif(row==3):
        SendDataR(0b00000100)
    elif(row==4):
        SendDataR(0b00001000)
    elif(row==5):
        SendDataR(0b00010000)
    elif(row==6):
        SendDataR(0b00100000)
    elif(row==7):
        SendDataR(0b01000000)
    elif(row==8):
        SendDataR(0b10000000)

    if(column==1):
        SendDataC(0b00000001)
    elif(column==2):
        SendDataC(0b00000010)
    elif(column==3):
        SendDataC(0b00000100)
    elif(column==4):
        SendDataC(0b00001000)
    elif(column==5):
        SendDataC(0b00010000)
    elif(column==6):
        SendDataC(0b00100000)
    elif(column==7):
        SendDataC(0b01000000)
    elif(column==8):
        SendDataC(0b10000000)
    time.sleep(0.0005)

def Happy():
    for i in range (0,300):
        Send(3,2)
        Send(4,2)
        Send(5,2)
        Send(6,2)
        Send(2,3)
        Send(7,3)
        Send(1,4)
        Send(8,4)
        Send(2,6)
        Send(3,6)
        Send(6,6)
        Send(7,6)
        Send(2,7)
        Send(3,7)
        Send(6,7)
        Send(7,7)
    
def Sad():
    for i in range (0,300):
        Send(1,1)
        Send(8,1)
        Send(7,2)
        Send(2,2)
        Send(3,3)
        Send(4,3)
        Send(5,3)
        Send(6,3)
        Send(2,6)
        Send(3,6)
        Send(6,6)
        Send(7,6)
        Send(2,7)
        Send(3,7)
        Send(6,7)
        Send(7,7)
    
def Nor():
    for i in range (0,200):
        Send(4,2)
        Send(5,2)   
        Send(2,3)
        Send(7,3)
        Send(3,3)
        Send(4,3)
        Send(5,3)
        Send(6,3)
        Send(2,6)
        Send(3,6)
        Send(6,6)
        Send(7,6)
        Send(2,7)
        Send(3,7)
        Send(6,7)
        Send(7,7)
    
def Ohh():
    for i in range (0,300):
        Send(6,1)
        Send(5,1)
        Send(3,1)
        Send(4,1)
        Send(6,2)
        Send(3,2)
        Send(4,3)
        Send(3,3)
        Send(5,3)
        Send(6,3)
        Send(2,6)
        Send(3,6)
        Send(6,6)
        Send(7,6)
        Send(2,7)
        Send(3,7)
        Send(6,7)
        Send(7,7)

def Trunk():
    for i in range (0,300):
        Send(3,1)
        Send(4,1)
        Send(3,2)
        Send(4,2)
        Send(2,3)
        Send(3,3)
        Send(4,3)
        Send(5,3)
        Send(6,3)
        Send(7,3)
        Send(2,6)
        Send(3,6)
        Send(6,6)
        Send(7,6)
        Send(2,7)
        Send(3,7)
        Send(6,7)
        Send(7,7)

def Love():
    for i in range (0,300):
        Send(4,2)
        Send(5,2)
        Send(3,3)
        Send(4,3)
        Send(5,3)
        Send(6,3)
        Send(2,4)
        Send(3,4)
        Send(4,4)
        Send(5,4)
        Send(6,4)
        Send(7,4)
        Send(1,5)
        Send(2,5)
        Send(3,5)
        Send(4,5)
        Send(5,5)
        Send(6,5)
        Send(7,5)
        Send(8,5)
        Send(1,6)
        Send(2,6)
        Send(3,6)
        Send(4,6)
        Send(5,6)
        Send(6,6)
        Send(7,6)
        Send(8,6)
        Send(3,7)
        Send(2,7)
        Send(7,7)
        Send(6,7)

def Eye():
    for i in range (0,300):
        Send(3,2)
        Send(4,2)
        Send(5,2)
        Send(6,2)
        Send(7,2)
        Send(2,3)

        Send(6,6)
        Send(7,6)
        Send(2,6)
        Send(3,6)
        Send(6,7)
        Send(7,7)

def Angry():
    for i in range (0,300):
        Send(1,1)
        Send(8,1)
        Send(7,2)
        Send(2,2)
        Send(3,3)
        Send(4,3)
        Send(5,3)
        Send(6,3)
        Send(2,6)
        Send(3,6)
        Send(6,6)
        Send(7,6)
        Send(1,7)
        Send(2,7)
        Send(7,7)
        Send(8,7)
        Send(3,2)
        Send(3,2)
        Send(4,2)
        Send(5,2)
        Send(6,2)
       

        
def my_process():
    a1 = "arecord /home/pi/Documents/a.wav -D sysdefault:CARD=1 -d 3"
    subprocess.call(a1,shell= True)
    
def audioReconize():
    print("Reconizing...")
    AUDIO_FILE = ("a.wav")
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        output = str.lower(r.recognize_google(audio))
    try:
        print("You said: " + output)
        if ((output.find(h1) >= 0) or (output.find(h2) >= 0) or (output.find(h3) >= 0) or (output.find(h4) >= 0)):
            Happy()

        elif ((output.find(s1) >= 0) or (output.find(s2) >= 0) or (output.find(s3) >= 0) or (output.find(s4) >= 0)):
            Sad()
        elif ((output.find(a1) >= 0) or (output.find(a2) >= 0) or (output.find(a3) >= 0) or (output.find(a4) >= 0) or (output.find(a5) >= 0) or (output.find(a6) >= 0)):
            Angry()
        elif ((output.find(l1) >= 0) or (output.find(l2) >= 0) or (output.find(l3) >= 0)):
            Love()
        elif ((output.find(e1) >= 0) or (output.find(e2) >= 0) or (output.find(e3) >= 0)):
            Eye()
        elif ((output.find(t1) >= 0) or (output.find(t2) >= 0) or (output.find(t3) >= 0) or (output.find(t4) >= 0)):
            Trunk()
        elif ((output.find(o1) >= 0) or (output.find(o2) >= 0) or (output.find(o3) >= 0)):
            Ohh()
        else:
            Nor()
     
    except sr.UnknownValueError:
        print("Can't Reconize. Please try again")
     
    except sr.RequestError as e:
        print("Could not request results from Recognition service; {0}".format(e))


PinInit()

while(1):
    print("Speak Now...")
    print("Recording for 3 Sec..")
    thread = threading.Thread(target=my_process)
    thread.start()
    Nor()
    audioReconize()