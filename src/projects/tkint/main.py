import matplotlib
matplotlib.use("TkAgg")  # <-- key on macOS when using tkinter dialogs

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter import Tk, filedialog
import matplotlib.image as mpimg

# Create ONE Tk root for the whole app (don’t recreate per click)
root = Tk()
root.withdraw()
root.update()  # helps ensure Tk is initialized

def pick_file(_event=None):
    path = filedialog.askopenfilename(
        parent=root,
        title="Open image",
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg *.tif *.tiff *.bmp"),
            ("All files", "*.*"),
        ],
    )
    if not path:
        return

    try:
        img = mpimg.imread(path)
    except Exception as e:
        print(f"Failed to open {path}: {e}")
        return

    ax_img.clear()
    ax_img.imshow(img, cmap="gray")
    ax_img.set_title(path)
    ax_img.axis("off")
    fig.canvas.draw_idle()

fig = plt.figure(figsize=(8, 5))
ax_img = fig.add_axes([0.05, 0.12, 0.9, 0.83])
ax_img.set_title("Click 'Open…' to load an image")
ax_img.axis("off")

ax_btn = fig.add_axes([0.05, 0.02, 0.15, 0.07])
btn = Button(ax_btn, "Open…")
btn.on_clicked(pick_file)

plt.show()
root.destroy()
