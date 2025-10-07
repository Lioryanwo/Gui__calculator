# Simple GUI Calculator (tkinter)

import tkinter as tk

ALLOWED = set("0123456789+-*/(). ")

def is_safe(expr: str) -> bool:
    return all(ch in ALLOWED for ch in expr)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("320x420")
        self.resizable(False, False)

        self.expr = tk.StringVar()
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        # Display
        entry = tk.Entry(self, textvariable=self.expr, font=("Segoe UI", 20),
                         justify="right", bd=8, relief="groove")
        entry.pack(fill="x", padx=10, pady=10, ipady=10)

        # Buttons layout
        btns = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["(", ")", "⌫", "="],
        ]

        frame = tk.Frame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=5)

        for r, row in enumerate(btns):
            for c, label in enumerate(row):
                b = tk.Button(frame, text=label, font=("Segoe UI", 16),
                              bd=1, relief="raised",
                              command=lambda t=label: self.on_press(t))
                b.grid(row=r, column=c, sticky="nsew", padx=4, pady=4, ipady=8)

        for i in range(4):
            frame.columnconfigure(i, weight=1)
        for i in range(len(btns)):
            frame.rowconfigure(i, weight=1)

    def bind_events(self):
        self.bind("<Return>", lambda e: self.evaluate())
        self.bind("<KP_Enter>", lambda e: self.evaluate())
        self.bind("<BackSpace>", lambda e: self.backspace())
        self.bind("<Escape>", lambda e: self.clear())
        self.bind("<Key>", self.on_key)

    def on_key(self, event):
        ch = event.char
        if ch in ALLOWED:
            self.expr.set(self.expr.get() + ch)

    def on_press(self, t):
        if t == "=":
            self.evaluate()
        elif t == "C":
            self.clear()
        elif t == "⌫":
            self.backspace()
        else:
            self.expr.set(self.expr.get() + t)

    def clear(self):
        self.expr.set("")

    def backspace(self):
        self.expr.set(self.expr.get()[:-1])

    def evaluate(self):
        s = self.expr.get()
        if not is_safe(s) or not s.strip():
            self.expr.set("Error")
            return
        try:
            # eval מוגבל רק לתווים המותרים (+ - * / . ( ) ספרות ורווח)
            result = eval(s, {"__builtins__": {}}, {})
            self.expr.set(str(result))
        except Exception:
            self.expr.set("Error")

if __name__ == "__main__":
    Calculator().mainloop()
