import os
import time
import uuid
import cv2
from matplotlib import pyplot as plt

IMAGES_PATH = os.path.join('data', 'images')
number_images = 30

# Ensure the directory exists
os.makedirs(IMAGES_PATH, exist_ok=True)

# Try to find the working camera index
camera_index = -1
for index in range(5):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        camera_index = index
        cap.release()
        break

if camera_index == -1:
    print("Error: Unable to access any camera.")
    exit()

print(f"Using camera index {camera_index}")

# Initialize the camera with the found index
cap = cv2.VideoCapture(camera_index)

for imgnum in range(number_images):
    print(f'Collecting image {imgnum}')
    ret, frame = cap.read()

    if not ret:
        print(f"Error: Failed to capture image {imgnum}")
        continue

    imgname = os.path.join(IMAGES_PATH, f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)

    # Display the image using matplotlib
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title(f'Image {imgnum}')
    plt.show(block=False)
    plt.pause(0.5)  # Display for 0.5 seconds
    plt.close()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
