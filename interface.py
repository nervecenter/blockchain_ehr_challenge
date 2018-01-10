import sys
from tkinter import *
from tkinter import ttk

def clear(*args):
	address.set("")
	first.set("")
	last.set("")
	street.set("")
	city.set("")
	state.set("")
	zipcode.set("")
	hospital.set("")
	condition.set("")

def get_record(*args):
	pass

def set_record(*args):
	pass

if __name__ == "__main__":
	root = Tk()
	root.title(sys.argv[1])

	address = StringVar()
	first = StringVar()
	last = StringVar()
	street = StringVar()
	city = StringVar()
	state = StringVar()
	zipcode = StringVar()
	hospital = StringVar()
	condition = StringVar()

	frame = ttk.Frame(root, padding="3 3 12 12")
	frame.grid(column=0, row=0, sticky=(N, W, E, S))
	frame.columnconfigure(0, weight=1)
	frame.rowconfigure(0, weight=1)

	ttk.Label(frame, text="Address:").grid(column=2, row=0, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=address)
	first_entry.grid(column=3, row=0, sticky=(W, E))

	separator = ttk.Separator(frame, orient=HORIZONTAL)
	separator.grid(column=3, row=1, sticky=(W, E))

	ttk.Label(frame, text="First name:").grid(column=2, row=2, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=first)
	first_entry.grid(column=3, row=2, sticky=(W, E))

	ttk.Label(frame, text="Last name:").grid(column=2, row=3, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=last)
	first_entry.grid(column=3, row=3, sticky=(W, E))

	ttk.Label(frame, text="Street address:").grid(column=2, row=4, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=street)
	first_entry.grid(column=3, row=4, sticky=(W, E))

	ttk.Label(frame, text="City:").grid(column=2, row=5, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=city)
	first_entry.grid(column=3, row=5, sticky=(W, E))

	ttk.Label(frame, text="State:").grid(column=2, row=6, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=state)
	first_entry.grid(column=3, row=6, sticky=(W, E))

	ttk.Label(frame, text="Zip code:").grid(column=2, row=7, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=zipcode)
	first_entry.grid(column=3, row=7, sticky=(W, E))

	ttk.Label(frame, text="Hospital:").grid(column=2, row=8, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=hospital)
	first_entry.grid(column=3, row=8, sticky=(W, E))

	ttk.Label(frame, text="Condition:").grid(column=2, row=9, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=condition)
	first_entry.grid(column=3, row=9, sticky=(W, E))

	get_button = ttk.Button(frame, text="Get Record", command=get_record)
	get_button.grid(column=2, row=10, sticky=W)
	set_button = ttk.Button(frame, text="Set Record", command=set_record)
	set_button.grid(column=3, row=10, sticky=W)
	clear_button = ttk.Button(frame, text="Clear", command=clear)
	clear_button.grid(column=4, row=10, sticky=W)

	status_box = ttk.Labelframe(frame)
	status_box.grid(row = 11, sticky=W, columnspan=4)
	status = ttk.Label(status_box, text="Waiting for input.")
	status.grid(columnspan=4, sticky=N)

	for child in frame.winfo_children():
		child.grid_configure(padx=5, pady=5)

	root.mainloop()