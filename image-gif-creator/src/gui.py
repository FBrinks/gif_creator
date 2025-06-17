import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.simpledialog
import os

from image_sorter import move_up, move_down
from gif_creator import create_gif

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Creator")
        self.image_paths = []

        # Ladda bilder-knapp
        self.load_button = tk.Button(root, text="Ladda bilder", command=self.load_images)
        self.load_button.pack(pady=10)

        # Lista för bildsökvägar
        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(padx=10, pady=10)

        # Ram för upp/ned-knappar
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.up_button = tk.Button(self.button_frame, text="Flytta upp", command=self.move_up)
        self.up_button.grid(row=0, column=0, padx=5)

        self.down_button = tk.Button(self.button_frame, text="Flytta ned", command=self.move_down)
        self.down_button.grid(row=0, column=1, padx=5)

        # Skapa GIF-knapp
        self.gif_button = tk.Button(root, text="Skapa och spara GIF", command=self.create_and_save_gif)
        self.gif_button.pack(pady=10)

    def load_images(self):
        filetypes = [
            ("Image files", "*.jpeg *.jpg *.png"),
            ("JPEG files", "*.jpeg *.jpg"),
            ("PNG files", "*.png"),
            ("All files", "*.*"),
        ]
        files = filedialog.askopenfilenames(
            title="Välj bilder",
            filetypes=filetypes
        )
        if files:
            self.image_paths = list(files)
            self.update_listbox()
        else:
            messagebox.showinfo("Ingen bild vald", "Inga bilder valdes.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for path in self.image_paths:
            self.listbox.insert(tk.END, os.path.basename(path))

    def move_up(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        idx = selected[0]
        new_idx = move_up(self.image_paths, idx)
        self.update_listbox()
        self.listbox.select_set(new_idx)

    def move_down(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        idx = selected[0]
        new_idx = move_down(self.image_paths, idx)
        self.update_listbox()
        self.listbox.select_set(new_idx)

    def create_and_save_gif(self):
        if not self.image_paths:
            messagebox.showwarning("Inga bilder", "Ladda in bilder först.")
            return

        filename = tk.simpledialog.askstring("GIF-namn", "Ange namn på GIF-filen (utan .gif):")
        if not filename:
            return

        # Spara i samma mapp som första bilden
        first_image_dir = os.path.dirname(self.image_paths[0])
        gif_path = os.path.join(first_image_dir, f"{filename}.gif")

        # Standardtid per bild (ms)
        duration = 500

        try:
            create_gif(self.image_paths, duration, gif_path)
            messagebox.showinfo("GIF skapad", f"GIF sparad som:\n{gif_path}")
        except Exception as e:
            messagebox.showerror("Fel vid GIF-skapande", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()