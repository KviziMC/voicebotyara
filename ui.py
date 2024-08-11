import customtkinter
from PIL import Image
def button_callback():
    print("шо")

app = customtkinter.CTk()
app.geometry("500x400")

textbox = customtkinter.CTkTextbox(app)
textbox.insert('0.0', '')
textbox.pack(padx=20, pady=20)

button_image = customtkinter.CTkImage(Image.open("microphone.png"), size=(26, 26))
button = customtkinter.CTkButton(app, text="шо", command=button_callback, image=button_image)
button.pack(padx=20, pady=20)



app.mainloop()                                                             

