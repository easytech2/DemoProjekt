#if __name__ = '__main__':
import contours
import cv2
#import shapely.speedups

# Öffnen der Kammera
cam = cv2.VideoCapture(0)
while cam.isOpened():
# Lesend er Kammera!
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
# Differenzen zwischen beiden Frame erstellen
# Aufnehmen Zwei Instanzen
    diff = cv2.absdiff(frame1, frame2)
# Bewegungen von der Cam in Grauer Farbe erstellen
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)                                                # Blur effekt
    thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)                             # Schärfere Cam Aufnahme
    dilated = cv2.dilate(thresh, None, iterations=3)
    countours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)        # Konturen erstellen
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)                                  # Kontur Zeichnen und verfolgen
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if cv2.waitKey(10) == ord('q'):                                                         # Schliesen des Videos
        break
    cv2.imshow('Ai Cam', frame1)

