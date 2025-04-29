import random
import string
import tkinter as tk

#generate password
def gen_pwd() :
    try :
        len = int(length_entry.get())
        if len <= 0 :
            raise ValueError
        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(len))
        output_label.config(text=password)

    except ValueError :
        output_label.config(text = "Please enter a valid number.")

#gui
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Enter Password Length :").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=10)

gen_btn = tk.Button(root, text="Generate Password", command=gen_pwd)
gen_btn.pack(pady=10)

output_label = tk.Label(root, text="", font=("Courier", 12))
output_label.pack(pady=10)

root.mainloop()