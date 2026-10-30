import tkinter as tk
import psutil

def update_stats():
    cpu = psutil.cpu_percent()              # % since the last call
    ram = psutil.virtual_memory().percent   # % of RAM in use
    cpu_label.config(text=f"CPU: {cpu}%")
    ram_label.config(text=f"RAM: {ram}%")
    root.after(1000, update_stats)          # run again in 1000 ms

root = tk.Tk()
root.title("System Monitor")
root.geometry("250x110")

cpu_label = tk.Label(root, text="CPU: --", font=("Arial", 16))
cpu_label.pack(pady=5)
ram_label = tk.Label(root, text="RAM: --", font=("Arial", 16))
ram_label.pack(pady=5)

update_stats()
root.mainloop()
