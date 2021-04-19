from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def open_image():
    global image_file
    filename = filedialog.askopenfilename(
        initialdir='/',
        title="Upload Main Image",
        filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png"))
    )

    if filename != "":
        Label(window, text=f"Image {filename} uploaded").grid(row=4, column=0)
        image_file = filename


image_file = None


def save_image(image_file):
    if image_file is not None:
        main = Image.open(image_file)
        width, height = main.size

        draw = ImageDraw.Draw(main)

        text = watermark_entry.get()
        font = ImageFont.truetype('arial.ttf', 40)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 15
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 35))
        main.show()


# --------------- UI --------------- #
window = Tk()
window.title("Image watermark")
window.config(padx=100, pady=100)

title_label = Label(window, text="Image watermark desktop app", font="Arial")
title_label.grid(row=0, column=1, pady=20)

canvas = Canvas(height=250, width=250)
canvas.grid(row=1, column=1)


upload_btn_main = Button(window, text="Select Image", command=open_image)
upload_btn_main.grid(row=3, column=0, pady=10)

add_watermark_btn = Button(window, text="Add Watermark", width=15, command=lambda: save_image(image_file=image_file))
add_watermark_btn.grid(row=5, column=2, pady=20)

watermark_entry = Entry(window, bd=0.5, width=35, insertwidth=1)
watermark_entry.grid(row=5, column=1,  pady=20)

window.mainloop()