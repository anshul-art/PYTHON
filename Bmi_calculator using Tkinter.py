from tkinter import *
from tkinter import Toplevel

# Function to show the BMI chart as a tooltip
def show_bmi_chart(event):
    # Create a new Toplevel window for the tooltip
    global chart_window
    chart_window = Toplevel(window)
    chart_window.title("BMI Categories")
    chart_window.geometry("300x200")
    chart_window.overrideredirect(1)  # Remove window decorations

    # Position the chart window near the question mark symbol
    x = event.x_root + 20
    y = event.y_root + 10
    chart_window.geometry(f"+{x}+{y}")
    
    # Add the BMI categories chart in the window
    chart_text = """BMI Categories:
    - < 16: Severely underweight
    - 16 - 18.5: Underweight
    - 18.5 - 24.9: Normal weight
    - 25 - 29.9: Overweight
    - 30 - 34.9: Obesity I
    - 35 - 39.9: Obesity II
    - ≥ 40: Obesity III"""
    chart_label = Label(chart_window, text=chart_text, font=('Comic Sans MS', 10), justify=LEFT)
    chart_label.pack(padx=10, pady=10)

def hide_bmi_chart(event):
    if 'chart_window' in globals() and chart_window.winfo_exists():
        chart_window.destroy()

# Function to calculate BMI
def Bmi_calculator():
    weight = float(weight_entry.get())
    height_feet = int(feet_entry.get())
    height_inches = int(inch_entry.get())
    
    total_inches = (height_feet * 12) + height_inches
    height_meters = total_inches * 0.0254
    
    bmi = weight / (height_meters ** 2)
    
    bmi_entry.config(state='normal')
    bmi_entry.delete(0, END)
    bmi_entry.insert(0, f"{bmi:.2f}")
    bmi_entry.config(state='readonly')
    
    if bmi < 16:
        message = "You are severely underweight."
    elif 16 <= bmi < 18.5:
        message = "You are underweight."
    elif 18.5 <= bmi < 25:
        message = "You have a normal weight."
    elif 25 <= bmi < 30:
        message = "You are overweight."
    elif 30 <= bmi < 35:
        message = "You are in the obese category I."
    elif 35 <= bmi < 40:
        message = "You are in the obese category II."
    else:
        message = "You are in the obese category III."
    
    message_label.config(text=message)

def reset_fields():
    weight_entry.delete(0, END)
    feet_entry.delete(0, END)
    inch_entry.delete(0, END)
    bmi_entry.config(state='normal')
    bmi_entry.delete(0, END)
    bmi_entry.config(state='readonly')
    message_label.config(text="")

# Create the main window
window = Tk()
window.geometry('400x500')
window.title('BMI Calculator')

# Title label
label = Label(window, text="BMI Calculator", font=('Comic Sans MS', 18), fg="#000080", relief=RAISED)
label.place(relx=0.4, y=20, anchor='n')

# Question mark label to trigger the BMI chart tooltip
question_mark = Label(window, text="?", font=('Comic Sans MS', 18, 'bold'), fg="blue", cursor="hand2")
question_mark.place(x=270, y=20)
question_mark.bind("<Enter>", show_bmi_chart)   # Show chart on hover
question_mark.bind("<Leave>", hide_bmi_chart)   # Hide chart when hover out

# Weight label and entry
weight_label = Label(window, text="Weight (kg):", font=('Comic Sans MS', 14), fg="#000080", borderwidth=5)
weight_label.place(x=20, y=120)
weight_entry = Entry(window, font=14, borderwidth=5)
weight_entry.place(x=150, y=124)

# Height (Feet) label and entry
feet_label = Label(window, text="Height (ft):", font=('Comic Sans MS', 14), fg="#000080", borderwidth=5)
feet_label.place(x=20, y=180)
feet_entry = Entry(window, font=14, borderwidth=5)
feet_entry.place(x=150, y=184)

# Height (Inches) label and entry
inch_label = Label(window, text="Height (in):", font=('Comic Sans MS', 14), fg="#000080", borderwidth=5)
inch_label.place(x=20, y=245)
inch_entry = Entry(window, font=14, borderwidth=5)
inch_entry.place(x=150, y=250)

# BMI label and entry (display the calculated BMI)
bmi_label = Label(window, text='BMI:', font=('Comic Sans MS', 14), fg="#000080", borderwidth=5)
bmi_label.place(x=20, y=320)
bmi_entry = Entry(window, font=14, borderwidth=5, state='readonly')
bmi_entry.place(x=150, y=325)

# Button to trigger BMI calculation
bmi_button = Button(window, command=Bmi_calculator, text='Calculate BMI', font=('Comic Sans MS', 14), borderwidth=5)
bmi_button.place(x=60, y=380)

# Reset button to clear all fields
reset_button = Button(window, command=reset_fields, text='Reset', font=('Comic Sans MS', 14), borderwidth=5)
reset_button.place(x=220, y=380)

# Label to display the dynamic BMI category message
message_label = Label(window, text="", font=('Comic Sans MS', 14), fg="#000080")
message_label.place(x=50, y=450)

# Configure the window's background
window.config(background="White")

# Start the Tkinter event loop
window.mainloop()

