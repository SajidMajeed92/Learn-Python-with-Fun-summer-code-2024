# Tkinter Programming
# Tkinter is the standard GUI library for Python.
# Python when combined with Tkinter provides a fast and easy way to create GUI applications.
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

# The foundational element of a Tkinter GUI is the window.
# Windows are the containers in which all other GUI elements live.
# These other GUI elements, such as text boxes, labels, and buttons, are known as widgets.
# Widgets are contained inside of windows.


import tkinter as tk
window = tk.Tk()
window.title('widget Label')
'''Any Widgets you wants are added here '''
window.geometry('250x250')
label = tk.Label(text="Summer code Python course 2024")
label.pack()
label = tk.Label(text="Python course 2024")
label.pack()
button=tk.Button(text='Click Me',
                 fg='white',
                 background='Black',
                 font='verdana',
                 height=5,
                 width=5)
button.pack()
window.mainloop()