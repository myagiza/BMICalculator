import tkinter as tk

#window
new_window = tk.Tk()
new_window.title("BMI CALCULATOR")
new_window.geometry("250x200")

#first label

label = tk.Label(new_window, text="Enter your height (m)", font=("Arial 10 bold"))
label.pack()
#entrybox
entry = tk.Entry(width=20)
entry.pack()

#second label

label2 = tk.Label(new_window, text="Enter your weight (kg)", font=("Arial 10 bold"))
label2.pack()

#entrybox
entry2 = tk.Entry(width=20)
entry2.pack()

#Calculate
def calculated_button():
    try:
        value1 = float(entry.get())
        value1_cm = value1 / 100
        value2 = float(entry2.get())
        BMI = value2 / (value1_cm* 2 )
        print(BMI)
        if BMI < 19:
            underweight_label = tk.Label(text=f"You are underweight.\nYour BMI : {BMI}")
            underweight_label.pack()
        elif 18.5 <= BMI <= 24.9:
            underweight_label = tk.Label(text=f"You are normalweight.\nYour BMI : {BMI}")
            underweight_label.pack()
        elif 25 <= BMI <= 29.9:
            underweight_label = tk.Label(text=f"You are overweight.\nYour BMI : {BMI}")
            underweight_label.pack()
        elif 30 <= BMI <= 39.9:
            underweight_label = tk.Label(text=f"You are obesity.\nYour BMI : {BMI}")
            underweight_label.pack()
        else:
            underweight_label = tk.Label(text=f"You are morbid obesity.\nYour BMI : {BMI}")
            underweight_label.pack()
    except:
        label_Error = tk.Label(text="INVALID VALUE !!")
        label_Error.pack()


calculate_button = tk.Button(text="Calculate",command=lambda: [calculated_button()])
calculate_button.pack()


new_window.mainloop()
