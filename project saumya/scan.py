import cv2
import pyzbar.pyzbar as pyzbar

# Start webcam
cap = cv2.VideoCapture(0)
names = set()

# Function for attendance file
attendance_file = 'attendance.txt'
fob = open(attendance_file, 'a+')

def enterData(z):
    if z in names:
        pass
    else:
        names.add(z)
        fob.write(z + '\n')
        print(f'{z} is present')

print('Reading code..................')

# Function to check data
def checkData(data):
    data = str(data)
    if data in names:
        print(f'{data} is already present')
    else:
        enterData(data)

while True:
    _, frame = cap.read()
    decodeObjects = pyzbar.decode(frame)

    for obj in decodeObjects:
        try:
            decoded_data = obj.data.decode('utf-8')
            checkData(decoded_data)
        except UnicodeDecodeError:
            print(f'Error decoding data from QR code: {obj.data}')

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Close the attendance file
fob.close()
cap.release()
cv2.destroyAllWindows()
