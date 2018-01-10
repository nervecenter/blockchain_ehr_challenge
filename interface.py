import sys
from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
	root = Tk()
	root.title(sys.argv[1])

	first = StringVar()
	last = StringVar()
	street = StringVar()
	city = StringVar()
	state = StringVar()
	zipcode = StringVar()

	frame = ttk.Frame(root, padding="3 3 12 12")
	frame.grid(column=0, row=0, sticky=(N, W, E, S))
	frame.columnconfigure(0, weight=1)
	frame.rowconfigure(0, weight=1)

	ttk.Label(frame, text="First name:").grid(column=2, row=1, sticky=W)
	first_entry = ttk.Entry(frame, width=7, textvariable=first)
	first_entry.grid(column=3, row=1, sticky=(W, E))

	for child in frame.winfo_children():
		child.grid_configure(padx=5, pady=5)

	root.mainloop()