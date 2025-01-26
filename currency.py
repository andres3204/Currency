import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button

from PIL import Image, ImageTk

import os 

# clear function
def clear():
    radioConverter.set(None)
    amountText.delete(0, tk.END)

# exit function
def exit():
    root.quit()

# global rates defaults
usToCanRate = 1.45
canToUsRate = 0.7

def setUsToCanRate():
    setRate = Toplevel(root)
    setRate.title("USD to CAD rate")
    setRate.geometry("300x100")

    global usToCanRate
    rateUsToCanLabel = Label(setRate, text="Enter the conversion rate:")
    rateUsToCanLabel.grid()
    rateUsToCanText = tk.Entry(setRate)
    rateUsToCanText.grid()

    def updateRate():
        try:        
            rate = float(rateUsToCanText.get())
            global usToCanRate
            usToCanRate = rate
            messagebox.showinfo("Rate Set", f"New USD to CAD rate: {usToCanRate}")
            setRate.destroy()
        
        except Exception:
            messagebox.showerror("Error", "Please enter a valid numeric rate")
    
    rateUsToCanButton = Button(setRate, text="Done!", command=updateRate)
    rateUsToCanButton.grid(row=2, column=0, pady=5)

def setCanToUsRate():
    setRate = Toplevel(root)
    setRate.title("CAD to USD rate")
    setRate.geometry("300x100")

    global canToUsRate
    rateCanToUsLabel = Label(setRate, text="Enter the conversion rate:")
    rateCanToUsLabel.grid()
    rateCanToUsText = tk.Entry(setRate)
    rateCanToUsText.grid()

    def updateRate():
        try:
            rate = float(rateCanToUsText.get())
            global canToUsRate
            canToUsRate = rate
            messagebox.showinfo("Rate Set", f"New CAD to USD rate: {canToUsRate}")
            setRate.destroy()

        except Exception:
            messagebox.showerror("Error", "Please enter a valid numeric rate")
    
    rateCanToUsButton = Button(setRate, text="Done!", command=updateRate)
    rateCanToUsButton.grid(row=2, column=0, pady=5)

def usToCan(amount):
    return round(amount * usToCanRate, 2)

def canToUs(amount):
    return round(amount * canToUsRate, 2)

def about():
    aboutWindow = Toplevel(root)
    aboutWindow.title("About")
    aboutWindow.geometry("500x800")

    try:
        image = Image.open("me.png")
        photo = ImageTk.PhotoImage(image)
        img_label = Label(aboutWindow, image=photo)
        img_label.image = photo  # Keep a reference
        img_label.grid(row=0, column=1, padx=(20, 10))

    except Exception as e:
        messagebox.showerror("File not loading: me.png")

    titleLabel = Label(aboutWindow, text="About Me") 
    titleLabel.grid(row=1, column=1, padx=10, pady=10)  
    nameLabel = Label(aboutWindow, text="Andres Jimenez")
    nameLabel.grid(row=2, column=1, padx=10, pady=10)
    dateLabel = Label(aboutWindow, text="January 22, 2025")
    dateLabel.grid(row=3, column=1, padx=10, pady=10)


# convert function
def convert():
    try: 
        amount = float(amountText.get())
        selectedRadio = radioConverter.get()
        if (selectedRadio == "Option 1"):
            result = usToCan(amount)
            message = f"{amount} USD = {result} CAD"
        elif (selectedRadio == "Option 2"):
            result = canToUs(amount)
            message = f"{amount} CAD = {result} USD"
        else:
             messagebox.showwarning("Please select a convertion option")
             return
        
        messagebox.showinfo("Conversion Result", message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric amount")

# program starts
root = tk.Tk()
root.geometry("400x150")
root.title("Currency Converter")
root.resizable(False, False)

# amount textbox
amount = tk.Label(root, text="Amount in Dollars: ")
amount.grid(row=4, column=0)
amountText = tk.Entry(root)
amountText.grid(row=4, column=1)

# radio buttons
question = tk.Label(root, text="How would you like to convert?")
radioConverter = tk.StringVar()
radio1 = tk.Radiobutton(root, text="US to Canadian", variable=radioConverter, value="Option 1")
radio2 = tk.Radiobutton(root, text="Canadian to US", variable=radioConverter, value="Option 2")
question.grid()
radio1.grid()
radio2.grid()

# button to convert
button = tk.Button(root, text="Convert", command=convert)
button.grid()

# menu 
menuBar = tk.Menu(root)

# file menu 
fileMenu = tk.Menu(menuBar)
fileMenu.add_command(label="Clear", command=clear)
fileMenu.add_command(label="Exit", command=exit)
menuBar.add_cascade(label="File", menu=fileMenu)

# rate menu
rateMenu = tk.Menu(menuBar)
rateMenu.add_command(label="US to Canadian", command=setUsToCanRate)
rateMenu.add_command(label="Canadian to US", command=setCanToUsRate)
menuBar.add_cascade(label="Rates", menu=rateMenu)

# help menu
helpMenu = tk.Menu(menuBar)
helpMenu.add_command(label="About", command=about)
menuBar.add_cascade(label="Help", menu=helpMenu)

root.config(menu=menuBar)

# start tkinter :)
root.mainloop()