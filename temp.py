from tkinter import *

# Create a new Tkinter window
window = Tk()
window.title("Miles to KM Converter")

# Configure padding around the window
window.config(padx=20, pady=20)

# Define a font (currently unused)
def_font = ("Arial", 12)

# Input field for user to enter a value in miles
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Create a label for displaying "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create a label for displaying "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Label to display the converted result in km, initial value set to "0"
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Create a label for displaying "KM"
km_label = Label(text="KM")
km_label.grid(column=2, row=1)

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f}")

# Create a button to trigger the conversion
convert_button = Button(text="Convert", command=miles_to_km)
convert_button.grid(column=1, row=2)

# Start the Tkinter event loop to display the window
window.mainloop()
