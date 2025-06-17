import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Loader")
        self.image_paths = []

        self.load_button = tk.Button(root, text="Load Images", command=self.load_images)
        self.load_button.pack(pady=10)

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(padx=10, pady=10)

    def load_images(self):
        filetypes = [
            ("Image files", "*.jpeg *.jpg *.png"),
            ("JPEG files", "*.jpeg *.jpg"),
            ("PNG files", "*.png"),
            ("All files", "*.*"),
        ]
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=filetypes
        )
        if files:
            self.image_paths = list(files)
            self.listbox.delete(0, tk.END)
            for path in self.image_paths:
                self.listbox.insert(tk.END, path)
        else:
            messagebox.showinfo("No Selection", "No images were selected.")

def load_images(file_paths):
    images = []
    for file_path in file_paths:
        try:
            img = Image.open(file_path)
            images.append(img)
        except Exception as e:
            print(f"Error loading image {file_path}: {e}")
    return images

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()