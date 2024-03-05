import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("CalculatorBot")

        self.display = tk.Entry(master, width=20, font=('Arial', 14), borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: self.click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.equation = ''

    def click(self, value):
        if value == '=':
            try:
                self.equation = str(eval(self.equation))
            except Exception as e:
                self.equation = 'Error'
        elif value == 'C':
            self.equation = ''
        else:
            self.equation += value

        self.display.delete(0, tk.END)
        self.display.insert(0, self.equation)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

