# 🧾 TextExtractor — OCR-программа на Python

**TextExtractor** — это простое приложение для извлечения текста с изображений с помощью `pytesseract` (Tesseract OCR) и `tkinter` для графического интерфейса.

---

## 🚀 Возможности

- Распознавание текста на русском и английском языках
- Поддержка изображений форматов: PNG, JPG, JPEG, BMP
- Графический интерфейс для выбора файла и отображения результата
- Предобработка изображения для повышения точности (опционально)

---

## 🛠️ Установка

1. **Установи Python** (3.8+)
2. **Установи зависимости:**

```bash
   pip install pytesseract pillow
```

**Скачивайте и установите Tesseract OCR**

Рекомендуемая сборка для Windows: UB Mannheim

```commandline
   Путь к tesseract.exe в коде, если он не в системной переменной PATH:
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## 📷 Как использовать
1. **Запусти файл main.py**
2. **Нажми кнопку "Выбрать изображение"**
3. **Программа распознает текст и выведет результат в окне**

## 📁 Структура проекта
```commandline
   TextExtractor/
├── main.py
├── README.md
└── requirements.txt
```

## 📌 Зависимости
1. pytesseract
2. Pillow
3. tkinter (обычно входит в стандартную библиотеку Python)
4. Tesseract OCR



