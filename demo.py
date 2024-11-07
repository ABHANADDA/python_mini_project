import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import datetime

root = tk.Tk()
root.title("Weather Visualization Dashboard")
root.geometry("600x500")

dates = []
temperatures = []

def add_data():
    try:
        date_str = date_entry.get()
        temp = float(temp_entry.get())
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        dates.append(date)
        temperatures.append(temp)
        date_entry.delete(0, tk.END)
        temp_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Data added successfully!")
    except ValueError:
       messagebox.showerror("Error", "Invalid input. Please enter date in YYYY-MM-DD format and temperature as a number.")

def plot_data():
    if dates and temperatures:
        plt.figure("Temperature Trends")
        plt.plot(dates, temperatures, marker="o", linestyle="-", color="blue")
        plt.title("Temperature Over Time")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        plt.gcf().autofmt_xdate() 
        plt.grid()
        plt.show()
    else:
        messagebox.showwarning("Warning", "No data to plot. Please add data first.")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.pack(padx=20 , pady=10)

ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(column=0, row=0, sticky=tk.W)
date_entry = ttk.Entry(frame)
date_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Temperature (°C):").grid(column=0, row=1, sticky=tk.W)
temp_entry = ttk.Entry(frame)
temp_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

add_button = ttk.Button(frame, text="Add Data", command=add_data )
add_button.grid(column=0, row=2, columnspan=2, pady=5)

plot_button = ttk.Button(frame, text="Plot Data", command=plot_data)
plot_button.grid(column=0, row=3, columnspan=2, pady=5)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
root.mainloop()
