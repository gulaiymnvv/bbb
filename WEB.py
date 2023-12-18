<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Простой рисовальщик</title>
</head>
<body>
    <canvas id="drawingCanvas" width="800" height="600" style="border:1px solid #000;"></canvas>

<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.2/brython.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.2/brython_stdlib.js"></script>
<script type="text/python">
    # Вставьте ваш Python-код рисовальщика сюда
    import tkinter as tk
from tkinter import colorchooser

class SimpleDrawer:
    def _init_(self, root):
        self.root = root
        self.root.title("Простой рисовальщик")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.color = "black"
        self.line_width = 2
        self.tool = "pencil"
        self.last_x = 0
        self.last_y = 0

        self.setup_menu()
        self.setup_toolbar()
        self.setup_canvas()

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Выход", command=self.root.destroy)

    def setup_toolbar(self):
        tool_bar = tk.Frame(self.root, bg="gray")
        tool_bar.pack(side=tk.TOP, fill=tk.X)

        pencil_button = tk.Button(tool_bar, text="Карандаш", command=self.choose_pencil)
        pencil_button.grid(row=0, column=0)

        eraser_button = tk.Button(tool_bar, text="Ластик", command=self.choose_eraser)
        eraser_button.grid(row=0, column=1)

        clear_button = tk.Button(tool_bar, text="Очистить", command=self.clear_canvas)
        clear_button.grid(row=0, column=2)

        color_button = tk.Button(tool_bar, text="Выбрать цвет", command=self.choose_color)
        color_button.grid(row=0, column=3)

    def setup_canvas(self):
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def choose_pencil(self):
        self.tool = "pencil"
        self.color = "black"

    def choose_eraser(self):
        self.tool = "eraser"
        self.color = "white"

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        x, y = event.x, event.y

        if self.tool == "pencil":
            self.canvas.create_line((self.last_x, self.last_y, x, y), width=self.line_width, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        elif self.tool == "eraser":
            self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill=self.color, outline=self.color)

        self.last_x = x
        self.last_y = y

    def reset(self, event):
        self.last_x, self.last_y = 0, 0

if _name_ == "_main_":
    root = tk.Tk()
    app = SimpleDrawer(root)
    root.mainloop()

    # Ваш существующий Python-код рисовальщика
</script>

</body>
</html>

