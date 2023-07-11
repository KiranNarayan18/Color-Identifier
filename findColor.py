import cv2


def find_color(pixelValue):

    if pixelValue < 10:
        return 'red'
    
    elif pixelValue > 10 and pixelValue <= 25:
        return 'orange'
    
    elif pixelValue > 25 and pixelValue <= 40:
        return 'yellow'

    elif pixelValue > 40 and pixelValue <= 75:
        return 'green'
    
    elif pixelValue > 75 and pixelValue <= 130:
        return 'blue'
    
    elif pixelValue > 130 and pixelValue <= 160:
        return 'purple'
    
    elif pixelValue > 160 and pixelValue <=169:
        return 'pink'
    
    

cap = cv2.VideoCapture(0)


while cap:
    try:
        _, frame = cap.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        height, width, _ = frame.shape
        # print("height", height, "width", width)

        center = (width//2, height//2)

        center_pixel = hsv_frame[width//2, height//2]
        

        result = find_color(center_pixel[0])
        if result is None:
            continue
        color_map = {
                'red': (0, 0, 255),
                'orange': (0, 165, 255),
                'yellow': (0, 255, 255),
                'green': (0, 255, 0),
                'blue': (255, 0, 0),
                'purple': (128, 0, 128),
                'pink': (203, 192, 255)
            }
        # print(color_map[result])
        cv2.circle(frame, center, 15, (0,0,0), 2)
        cv2.putText(frame, result.capitalize(), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0 ,color_map[result], 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    except Exception as e:
        print(e)


cap.release()     
cv2.destroyAllWindows()


