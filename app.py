from tkinter import *
import string
import random
from tkinter import messagebox

# Function to generate a random password based on strength
def generator():
    # Clear the previous password
    passwordField.delete(0, END)

    # Available characters
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    # Generate password based on choice
    if choice.get() == 1:
        password = ''.join(random.choices(small_alphabets, k=password_length))
    elif choice.get() == 2:
        password = ''.join(random.choices(small_alphabets + capital_alphabets, k=password_length))
    elif choice.get() == 3:
        password = ''.join(random.choices(all_characters, k=password_length))

    # Insert the password into the entry field
    passwordField.insert(0, password)


# Function to copy the password to clipboard without pyperclip
def copy():
    random_password = passwordField.get()
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(random_password)  # Append the password to the clipboard
    messagebox.showinfo("Copied", "Password copied to clipboard!")  # Show a message when copied


# Setting up the GUI
root = Tk()
root.config(bg='gray20')
choice = IntVar()
Font = ('arial', 13, 'bold')

# Password Generator Label
passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

# Radio buttons for password strength
weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)

# Password length label and spinbox
lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

# Generate password button
generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

# Entry field to display the generated password
passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

# Copy password button
copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

# Start the GUI
root.mainloop()
