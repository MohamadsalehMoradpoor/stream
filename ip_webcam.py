import cv2

url = "http://22.122.251.149:8080/video"

stream = cv2.VideoCapture(url)

while True:
          r , frame = stream.read()
          if frame is not None:
                    cv2.imshow("stream", frame)
          b = cv2.waitKey(1)
          if b==ord("b"):
                    beak
stream.release()