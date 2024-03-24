import cv2  # Imports the OpenCV library
import tkinter as tk  # Imports the Tkinter library
from tkinter import filedialog  # Imports the file dialog from Tkinter
from PIL import Image, ImageTk  # Imports Image and ImageTk modules from PIL library

# Function to open a file
def open_file():
    # Opens the file selection dialog and gets the selected file path
    file_path = filedialog.askopenfilename()
    
    # Continues if a file path is selected
    if file_path:
        # Loads the selected image using OpenCV
        img= cv2.imread(file_path)
        
        # Converts the image to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        
        # Detects faces using the face recognition classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30,30))

        # Encloses each face in a frame and adds a label
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)  # Encloses the face in a frame
            cv2.putText(img,"human",(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)  # Adds a label below the face
            
        # Converts the image to RGB format
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        # Converts the image to an Image object using the PIL library
        img = Image.fromarray(img)
        
        # Resizes the image to a specific dimension
        img = img.resize((600,400), Image.LANCZOS)
        
        # Converts the image to a format suitable for tkinter using the ImageTk module
        img = ImageTk.PhotoImage(img)

        # Updates the current image on the canvas
        canvas.img = img
        
        # Adds the new image to the canvas
        canvas.create_image(0,0, anchor = tk.NW, image=img)

# Loads the face recognition classifier
face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Creates a Tkinter window
root = tk.Tk()
root.title("Face Recognition")

# Creates a canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Creates an "Open File" button and associates it with the open file function
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

# Starts the Tkinter window
root.mainloop()
