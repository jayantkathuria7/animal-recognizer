#Importing necessary libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

#Loading the Model
model = tf.keras.models.load_model('Animal_Recognizer.keras')

#Initializing the GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Animal Recognizer')
top.configure(background='#CDCDCD')

#Initializing the labels (one for age and another for gender)
label1 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
label2 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
label3 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

#Defining Detect function which detects the age and gender of the person in image using the model
def detect(file_path):
    try:
        global label1, label2, label3
        image = Image.open(file_path)
        image = image.resize((256, 256))  # Resize image to 48x48
        image = np.array(image)  # Convert to numpy array
        image = np.expand_dims(image, axis=0)  # Expand dimensions to (1, 48, 48, 3)
        image = image / 255.0  # Normalize image data

        pred = model.predict(image)

        diet = np.argmax(pred[0])
        name = np.argmax(pred[1])
        age_group = np.argmax(pred[2])

        diet_f = ['carnivore', 'herbivore', 'omnivore']
        name_f = ['bear', 'chimpanzee', 'cow', 'crocodile', 'crow', 'deer', 'eagle', 'elephant',
                  'giraffe', 'lion', 'pig', 'raccoon', 'tiger', 'wolf', 'zebra']
        age_group_f = ['adult', 'child']

        print("Predicted Die:", diet_f[diet])
        print("Predicted Name:", name_f[name])
        print("Predicted Age Group:", age_group_f[age_group])


        label1.configure(foreground="#011638", text=f"Diet: {diet_f[diet]}")
        label2.configure(foreground="#011638", text=f"Name: {name_f[name]}")
        label3.configure(foreground="#011638", text=f"Age Group: {age_group_f[age_group]}")
    except Exception as e:
        print("Error:", e)

#Defining show_detect button
def show_detect_button(file_path):
    try:
        detect_b = Button(top, text='Detect', command=lambda: detect(file_path))
        detect_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
        detect_b.place(relx=0.79, rely=0.46)
    except Exception as e:
        print("Error:", e)

#Defining function for button to upload image
def upload_image_button():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text='')
        label2.configure(text='')
        label3.configure(text='')
        show_detect_button(file_path)
    except Exception as e:
        print("Error:", e)

upload = Button(top, text='Upload an Image', command=upload_image_button, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side='bottom', pady=50)
sign_image.pack(side='bottom', expand=True)
label1.pack(side='bottom', expand=True)
label2.pack(side='bottom', expand=True)
label3.pack(side='bottom', expand=True)
heading = Label(top, text='Animal Recognizer', pady=20, font=('arial', 15, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
