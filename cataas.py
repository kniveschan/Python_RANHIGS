from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO


def load_image():
    response = requests.get(url)
    print(response)
#    print(response.content)
    image_data=BytesIO(response.content)
    print(image_data)
    img=Image.open(image_data)
    img.thumbnail((500,500))#подгоняем картинку под размер
    print(img)
    img=ImageTk.PhotoImage(img)
    label.image = img
    label.config(image=img)


window=Tk()
window.geometry("500x550")

label=Label(width=500, height=500)
label.pack()


url="https://cataas.com/cat"

mainmenu=Menu(window)
window.config(menu=mainmenu)

file_menu=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузка изображения", command=load_image)
file_menu.add_command(label="Выход", command=window.destroy)


load_image()

window.mainloop()
