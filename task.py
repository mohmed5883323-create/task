# محمد حسن محمد عبد الوهاب سكشن 9 

import tkinter as tk

root = tk.Tk()
root.title("واجهة بسيطة")
root.geometry("300x250")

options = ["اختيار 1", "اختيار 2", "اختيار 3"]
selected = tk.StringVar()
selected.set(options[0])

option_menu = tk.OptionMenu(root, selected, *options)
option_menu.pack(pady=20)

def btn1_action():
    print("تم الضغط على الزر الأول")

def btn2_action():
    print("تم الضغط على الزر الثاني")

btn1 = tk.Button(root, text="زر 1", width=15, command=btn1_action)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="زر 2", width=15, command=btn2_action)
btn2.pack(pady=10)

root.mainloop()