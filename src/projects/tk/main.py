import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib
matplotlib.use("TkAgg")  # important on macOS when embedding in Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.image as mpimg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matplotlib inside Tk")
        self.geometry("900x600")

        # --- Top controls ---
        top = tk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.X)

        tk.Button(top, text="Open…", command=self.open_file).pack(side=tk.LEFT, padx=6, pady=6)

        # --- Matplotlib figure/canvas ---
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("No image loaded")
        self.ax.axis("off")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Optional: Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()

    def open_file(self):
        path = filedialog.askopenfilename(
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
            messagebox.showerror("Open failed", f"Could not open:\n{path}\n\n{e}")
            return

        self.ax.clear()
        self.ax.imshow(img, cmap="gray")
        self.ax.set_title(path)
        self.ax.axis("off")
        self.canvas.draw_idle()


if __name__ == "__main__":
    App().mainloop()
