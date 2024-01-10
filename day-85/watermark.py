import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.image_path = ""
        self.image = None

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        '''Creating the canvas with Buttons and Entries for inputs'''
        # Load Image Button
        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        # Watermark Entry
        self.watermark_entry = tk.Entry(self.root, width=30)
        self.watermark_entry.insert(0, "Your Watermark Text")
        self.watermark_entry.pack(pady=5)

        # Add Watermark Button
        self.watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack(pady=10)

        # Canvas for displaying image
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

    def load_image(self):
        '''Opens explorer on a GUI where you can select your image from'''
        file_types = [("JPEG files", "*.jpg;*.jpeg"), ("PNG files", "*.png"), ("All files", "*.*")]
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=file_types)
    
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.display_image()

    def display_image(self):
        '''Displays the Image that has been selected'''
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.config(width=self.photo.width(), height=self.photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def add_watermark(self):
        '''Adds a water mark at co-ordinates to be specified'''
        if self.image:
            watermark_text = self.watermark_entry.get()

            if watermark_text:
                draw = ImageDraw.Draw(self.image)
                font = ImageFont.load_default()

                text_width = draw.textlength(watermark_text, font=font)
                image_width, image_height = self.image.size

                x = (image_width - text_width) // 2
                y = image_height - font.getsize(watermark_text)[1] - 20

                draw.text((x, y), watermark_text, font=font, fill="white")

                self.display_image()

if __name__ == "__main__":
    window = tk.Tk()
    app = WatermarkApp(window)
    window.mainloop()
