from tkinter import *

def Bmi_calculator():
    #input values from the entry widgets
    weight = float(weight_entry.get())
    height_feet = int(feet_entry.get())
    height_inches = int(inch_entry.get())
    
    #height to meters
    total_inches = (height_feet * 12) + height_inches
    height_meters = total_inches * 0.0254
    
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    
    # Display BMI in the BMI entry box
    bmi_entry.config(state='normal')#set it to normal so that the program can enter the value
    bmi_entry.delete(0, END)
    bmi_entry.insert(0, f"{bmi:.2f}")
    bmi_entry.config(state='readonly')#after calculating the users cant modify it
    
    # Determine the BMI category and display a message
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
    
    # Update the message label with the BMI category
    message_label.config(text=message)

# Create the main window
window = Tk()
window.geometry('400x500')
window.title('BMI Calculator')

# Title label
label = Label(window,
              text="BMI Calculator in Kg and m",
              font=('Comic Sans MS', 18),
              fg="#000080",
              relief=RAISED,
              )
label.place(relx=0.5, y=20, anchor='n')

# Weight label and entry
weight_label = Label(window,
                     text="Weight (kg):",
                     font=('Comic Sans MS', 14),
                     fg="#000080",
                     borderwidth=5
                     )
weight_label.place(x=20, y=120)
weight_entry = Entry(window, font=14, borderwidth=5)
weight_entry.place(x=150, y=124)

# Height (Feet) label and entry
feet_label = Label(window,
                   text="Height (ft):",
                   font=('Comic Sans MS', 14),
                   fg="#000080",
                   borderwidth=5)
feet_label.place(x=20, y=180)
feet_entry = Entry(window, font=14, borderwidth=5)
feet_entry.place(x=150, y=184)

# Height (Inches) label and entry
inch_label = Label(window,
                   text="Height (in):",
                   font=('Comic Sans MS', 14),
                   fg="#000080",
                   borderwidth=5)
inch_label.place(x=20, y=245)
inch_entry = Entry(window, font=14, borderwidth=5)
inch_entry.place(x=150, y=250)

# BMI label and entry (display the calculated BMI)
bmi_label = Label(window,
                  text='BMI:',
                  font=('Comic Sans MS', 14),
                  fg="#000080",
                  borderwidth=5)
bmi_label.place(x=20, y=320)
bmi_entry = Entry(window, font=14, borderwidth=5)
bmi_entry.place(x=150, y=325)

# Button to trigger BMI calculation
bmi_button = Button(window, command=Bmi_calculator, text='Calculate BMI', font=('Comic Sans MS', 14), borderwidth=5)
bmi_button.place(x=100, y=380)

# Label to display the dynamic BMI category message
message_label = Label(window, text="", font=('Comic Sans MS', 14), fg="#000080")
message_label.place(x=50, y=450)

# Configure the window's background
window.config(background="White")

# Start the Tkinter event loop
window.mainloop()
