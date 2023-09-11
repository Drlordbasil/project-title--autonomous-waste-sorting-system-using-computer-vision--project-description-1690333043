import cv2
Here's the optimized Python script:

```python


class WasteSortingSystem:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def capture_image(self):
        """Capture an image using the camera and save it to disk."""
        ret, frame = self.camera.read()
        if ret:
            try:
                cv2.imwrite('waste_image.jpg', frame)
                print("Image captured successfully!")
            except Exception as e:
                print("Failed to save image:", str(e))
        else:
            print("Failed to capture image.")

    def image_processing(self, image_path):
        """Apply advanced computer vision algorithms to process the captured image."""
        try:
            image = cv2.imread(image_path)
            # Apply advanced computer vision algorithms to identify and classify waste materials

            # Example: Convert image to grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Grayscale Image', grayscale_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print("Failed to process image:", str(e))

    def run(self):
        self.capture_image()
        self.image_processing('waste_image.jpg')

    def close(self):
        self.camera.release()


if __name__ == '__main__':
    waste_sorting_system = WasteSortingSystem()
    waste_sorting_system.run()
    waste_sorting_system.close()
```

The code is optimized as per the suggestions mentioned earlier.
