import tkinter as tk
from tkinter import colorchooser
from tkinter import Image, PhotoImage
from PIL import Image, ImageTk

class ColorSelector:
    def __init__(self, master):
        self.master = master
        master.title("Color Selector")
        master.geometry('325x500')
        master.resizable(False, False)
        master.configure(bg='#abdbe3') #background

        # Set the icon for the window
        master.iconbitmap("icon.ico")   
            
        self.color = "white"

        # Load the logo image and create a label to display it
        logo_img = tk.PhotoImage(file="logo.png")
        logo_label = tk.Label(master, image=logo_img, bg='#abdbe3')
        logo_label.image = logo_img  # keep a reference to the image to prevent garbage collection
        logo_label.pack(pady=10)

        self.color_label = tk.Label(master, text="Selected Color:", font=("Exo", 12), bg='#abdbe3')
        self.color_label.pack(pady=10)
        
        self.color_button = tk.Button(master, text="Select Color", command=self.get_color, font=("Exo", 12))
        self.color_button.pack(pady=10)
        
        self.rgb_label = tk.Label(master, text="RGB: (255, 255, 255)", font=("Exo", 12), bg='#abdbe3')
        self.rgb_label.pack(pady=10)
        
        self.canvas = tk.Canvas(master, bg=self.color, width=200, height=200)
        self.canvas.pack(pady=10)



    def get_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.color_label.config(text="Selected Color: " + self.color, bg='#abdbe3')
            self.canvas.config(bg=self.color)
            rgb = self.get_rgb(self.color)
            self.rgb_label.config(text="RGB: " + rgb)
    
    def get_rgb(self, color):
        # Convert hex color string to RGB tuple
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        # Format RGB tuple as string
        rgb_str = "({}, {}, {})".format(rgb[0], rgb[1], rgb[2])
        return rgb_str

root = tk.Tk()
app = ColorSelector(root)
root.mainloop()
