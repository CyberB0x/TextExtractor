import pytesseract
from tkinter import Tk, Label, Button, filedialog, Text
from PIL import Image, ImageTk

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧾 OCR-программа (pytesseract)")
        self.root.geometry("800x600")

        self.label = Label(root, text="Выберите изображение для распознавания текста", font=("Arial", 14))
        self.label.pack(pady=10)

        self.image_label = Label(root)
        self.image_label.pack()

        self.select_button = Button(root, text="📂 Выбрать изображение", command=self.select_image)
        self.select_button.pack(pady=5)

        self.text_box = Text(root, wrap="word", font=("Courier", 12))
        self.text_box.pack(expand=True, fill="both", padx=10, pady=10)

        self.save_button = Button(root, text="💾 Сохранить текст", command=self.save_text)
        self.save_button.pack(pady=5)


    def select_image(self):
        path = filedialog.askopenfilename(filetypes=[("Изображения", "*.png *.jpg *.jpeg *.bmp *.tiff")])
        if path:
            img = Image.open(path)
            img.thumbnail((500, 500))
            self.imgtk = ImageTk.PhotoImage(img)
            self.image_label.configure(image=self.imgtk)

            text = pytesseract.image_to_string(img, lang="rus+eng")
            self.text_box.delete(1.0, "end")
            self.text_box.insert("end", text.strip())


    def save_text(self):
        text = self.text_box.get("1.0", "end").strip()
        if text:
            file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text)


if __name__ == "__main__":
    root = Tk()
    app = OCRApp(root)
    root.mainloop()