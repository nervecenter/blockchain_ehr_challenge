import sys, health
from tkinter import *
from tkinter import ttk

def clear(*args):
	address.set("")
	password.set("")
	first.set("")
	last.set("")
	street.set("")
	city.set("")
	state.set("")
	zipcode.set("")
	hospital.set("")
	condition.set("")
	status.set("Cleared.")

def get_record(*args):
	status.set("Fetching record...")
	try:
		record = health.get_record_chain(address.get(), password.get())
	except Exception as e:
		status.set(e.message)
		return

	status.set("Successfully got record.")

	first.set(record["first"])
	last.set(record["last"])
	street.set(record["street"])
	city.set(record["city"])
	state.set(record["state"])
	zipcode.set(record["zipcode"])
	hospital.set(record["hospital"])
	condition.set(record["condition"])

def set_record(*args):
	record_dict = {
		"first": first.get(),
		"last": last.get(),
		"street": street.get(),
		"city": city.get(),
		"state": state.get(),
		"zipcode": zipcode.get(),
		"hospital": hospital.get(),
		"condition": condition.get()
	}
	
	status.set("Setting record...")
	try:
		health.set_record_chain(record_dict, address.get(), password.get())
	except Exception as e:
		status.set(e.message)
		return

	status.set("Successfully set record.")

if __name__ == "__main__":
	root = Tk()
	root.title(sys.argv[1])

	address = StringVar()
	password = StringVar()
	first = StringVar()
	last = StringVar()
	street = StringVar()
	city = StringVar()
	state = StringVar()
	zipcode = StringVar()
	hospital = StringVar()
	condition = StringVar()

	status = StringVar()

	frame = ttk.Frame(root, padding="3 3 12 12")
	frame.grid(column=0, row=0, sticky=(N, W, E, S))
	frame.columnconfigure(0, weight=1)
	frame.rowconfigure(0, weight=1)

	ttk.Label(frame, text="Address:").grid(column=2, row=0, sticky=W)
	address_entry = ttk.Entry(frame, width=20, textvariable=address)
	address_entry.grid(column=3, row=0, sticky=(W, E))

	ttk.Label(frame, text="Password:").grid(column=2, row=1, sticky=W)
	password_entry = ttk.Entry(frame, show="*", width=20, textvariable=password)
	password_entry.grid(column=3, row=1, sticky=(W, E))

	separator = ttk.Separator(frame, orient=HORIZONTAL)
	separator.grid(column=3, row=2, sticky=(W, E))

	ttk.Label(frame, text="First name:").grid(column=2, row=3, sticky=W)
	first_entry = ttk.Entry(frame, width=20, textvariable=first)
	first_entry.grid(column=3, row=3, sticky=(W, E))

	ttk.Label(frame, text="Last name:").grid(column=2, row=4, sticky=W)
	last_entry = ttk.Entry(frame, width=20, textvariable=last)
	last_entry.grid(column=3, row=4, sticky=(W, E))

	ttk.Label(frame, text="Street address:").grid(column=2, row=5, sticky=W)
	street_entry = ttk.Entry(frame, width=20, textvariable=street)
	street_entry.grid(column=3, row=5, sticky=(W, E))

	ttk.Label(frame, text="City:").grid(column=2, row=6, sticky=W)
	city_entry = ttk.Entry(frame, width=20, textvariable=city)
	city_entry.grid(column=3, row=6, sticky=(W, E))

	ttk.Label(frame, text="State:").grid(column=2, row=7, sticky=W)
	state_entry = ttk.Entry(frame, width=20, textvariable=state)
	state_entry.grid(column=3, row=7, sticky=(W, E))

	ttk.Label(frame, text="Zip code:").grid(column=2, row=8, sticky=W)
	zipcode_entry = ttk.Entry(frame, width=20, textvariable=zipcode)
	zipcode_entry.grid(column=3, row=8, sticky=(W, E))

	ttk.Label(frame, text="Hospital:").grid(column=2, row=9, sticky=W)
	hospital_entry = ttk.Entry(frame, width=20, textvariable=hospital)
	hospital_entry.grid(column=3, row=9, sticky=(W, E))

	ttk.Label(frame, text="Condition:").grid(column=2, row=10, sticky=W)
	condition_entry = ttk.Entry(frame, width=20, textvariable=condition)
	condition_entry.grid(column=3, row=10, sticky=(W, E))

	get_button = ttk.Button(frame, text="Get Record", command=get_record)
	get_button.grid(column=2, row=11, sticky=W)
	set_button = ttk.Button(frame, text="Set Record", command=set_record)
	set_button.grid(column=3, row=11, sticky=W)
	clear_button = ttk.Button(frame, text="Clear", command=clear)
	clear_button.grid(column=4, row=11, sticky=W)

	status_box = ttk.Labelframe(frame)
	status_box.grid(row = 12, sticky=W, columnspan=4)
	status_label = ttk.Label(status_box, textvariable=status)
	status.set("Waiting for input.")
	status_label.grid(columnspan=4, sticky=N)

	for child in frame.winfo_children():
		child.grid_configure(padx=5, pady=5)

	root.mainloop()
