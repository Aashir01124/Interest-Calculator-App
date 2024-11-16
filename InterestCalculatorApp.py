import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = int(principal_entry.get())
        time = int(time_entry.get())
        rate = int(rate_entry.get())

    
        simple_interest = (principal * rate * time) // 100

        compound_interest = principal * ((1 + rate / 100) ** time) - principal
        compound_interest = int(compound_interest)

        result_label.config(text=f"Simple Interest: {simple_interest}\nCompound Interest: {compound_interest}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("300x250")

tk.Label(root, text="Principal:").pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

tk.Label(root, text="Time (years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(root, text="Rate (%):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()