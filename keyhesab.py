import tkinter as tk
from tkinter import ttk


def calculate():
  n1 = num1.get()

  if n1 is not None:
    res = int(n1) * 15 /3.5
    result_label["text"] = f"گرم بر هر سانت: {res}"
  else:
    result_label["text"] = "Error! Values must be integers"


root = tk.Tk()
root.title("کیحساب")
root.minsize(230,90)
root.maxsize(230,90)

ttk.Label(root, text="قطرداخلی:").grid(row=0, column=0)
result_label = ttk.Label(root, text="نتیجه")
result_label.grid(row=2, column=1)
ttk.Label(root, text="!کاوش بدون محدودیت").grid(row=4, column=0)

num1 = ttk.Entry(root)
num1.grid(row=0, column=1)

ttk.Button(root, text="محاسبه", command=calculate).grid(row=3, column=1)

root.mainloop()