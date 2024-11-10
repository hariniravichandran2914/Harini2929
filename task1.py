import tkinter as tk

def convert():
    temp = float(entry.get())
    scale = var.get()
    
    if scale == 'C':
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        result.config(text=f"{temp}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K")
    elif scale == 'F':
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        result.config(text=f"{temp}°F = {celsius:.2f}°C, {kelvin:.2f}K")
    elif scale == 'K':
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        result.config(text=f"{temp}K = {celsius:.2f}°C, {fahrenheit:.2f}°F")

# GUI Setup
window = tk.Tk()
window.title("Temp Converter")

entry = tk.Entry(window)
entry.grid(row=0, column=1)

var = tk.StringVar(value="C")
tk.Radiobutton(window, text="Celsius", variable=var, value="C").grid(row=1, column=0)
tk.Radiobutton(window, text="Fahrenheit", variable=var, value="F").grid(row=1, column=1)
tk.Radiobutton(window, text="Kelvin", variable=var, value="K").grid(row=1, column=2)

tk.Button(window, text="Convert", command=convert).grid(row=2, column=1)
result = tk.Label(window)
result.grid(row=3, column=0, columnspan=3)

window.mainloop()

