from picamera2 import Picamera2
import cv2 as cv
import numpy as np
import time

#Initialisierung und Konfiguration der Kamera
cam = Picamera2()
camera_config = cam.create_still_configuration()
cam.configure(camera_config)
cam.start()

#Kurze Verzögerung, um die Kamera zu stabilisieren
time.sleep(3)
try:
    while True:
        #Bild aufnehmen und convertieren
        pil_image = cam.capture_image()
        image_np = np.array(pil_image)
        image_bgr = cv.cvtColor(image_np, cv.COLOR_RGB2BGR)

        #Bild anzeigen
        cv.imshow('Bild', image_bgr)

        #Warte und Prüfe ob Taste gedrückt wurde
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print('Programm wurde vom Benutzer unterbrochen')

finally:
    #Beenden der Schleife und freigeben von Ressourcen
    cam.stop()
    cv.destroyAllWindows()