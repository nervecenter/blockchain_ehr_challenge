import sys, health
from tkinter import *
from tkinter import ttk
from json import JSONDecodeError

def clear(*args):
	address.set("")
	password.set("")
	name.set("")
	dob.set("")
	gender.set("")
	age.set("")
	bmi.set("")
	icd9.set("")
	cpt.set("")
	penicillin_allergy.set("")
	adnet.set("")
	asa.set("")
	bun.set("")
	glucose.set("")
	k.set("")
	co2.set("")
	ca.set("")
	status.set("Cleared.")

def get_record(*args):
	status.set("Fetching record...")
	try:
		record = health.get_record_chain(address.get(), password.get())
	except JSONDecodeError:
		status.set("Incorrect password.")
		return
	except Exception as e:
		status.set(str(e))
		return

	status.set("Successfully got record.")

	demographic = record["demographic"]
	name.set(demographic["name"])
	dob.set(demographic["dob"])
	age.set(demographic["age"])
	gender.set(demographic["gender"])
	weight.set(demographic["weight"])
	bmi.set(demographic["bmi"])

	history = record["history"]
	icd9.set(history["icd9"])
	cpt.set(history["cpt"])
	penicillin_allergy.set(history["penicillin_allergy"])

	anesthesia = record["anesthesia"]
	adnet.set(anesthesia["adnet"])
	asa.set(anesthesia["asa"])

	metabolic = record["metabolic"]
	bun.set(metabolic["bun"])
	glucose.set(metabolic["glucose"])
	k.set(metabolic["k"])
	co2.set(metabolic["co2"])
	ca.set(metabolic["ca"])

def set_record(*args):
	record_dict = {
		"demographic": {
			"name": name.get(),
			"dob": dob.get(),
			"age": age.get(),
			"gender": gender.get(),
			"weight": weight.get(),
			"bmi": bmi.get(),
		},
		"history": {
			"icd9": icd9.get(),
			"cpt": cpt.get(),
			"penicillin_allergy": penicillin_allergy.get(),
		},
		"anesthesia": {
			"adnet": adnet.get(),
			"asa": asa.get(),
		},
		"metabolic": {
			"bun": bun.get(),
			"glucose": glucose.get(),
			"k": k.get(),
			"co2": co2.get(),
			"ca": ca.get(),
		}
	}

	status.set("Setting record...")
	try:
		health.set_record_chain(record_dict, address.get(), password.get())
	except Exception as e:
		status.set(str(e))
		return

	status.set("Successfully set record.")

if __name__ == "__main__":
	root = Tk()
	root.title(sys.argv[1])

	address = StringVar()
	password = StringVar()

	# Demographic info
	name = StringVar()
	dob = StringVar()
	age = StringVar()
	gender = StringVar()
	weight = StringVar()
	bmi = StringVar()

	# Patient history
	icd9 = StringVar()
	cpt = StringVar()

	penicillin_allergy = StringVar()

	# Anesthesia info
	adnet = StringVar()
	asa = StringVar()

	# Metabolic numbers
	bun = StringVar()
	glucose = StringVar()
	k = StringVar()
	co2 = StringVar()
	ca = StringVar()

	# Application status, communicates actions and errors
	status = StringVar()

	frame = ttk.Frame(root, padding="3 3 12 12")
	frame.grid(column=0, row=0, sticky=(N, W, E, S))
	frame.columnconfigure(0, weight=1)
	frame.rowconfigure(0, weight=1)

	ttk.Label(frame, text="Address:").grid(column=2, row=0, sticky=W)
	ttk.Label(frame, text="Password:").grid(column=2, row=1, sticky=W)
	# Separator
	ttk.Label(frame, text="Name:").grid(column=2, row=3, sticky=W)
	ttk.Label(frame, text="Date of birth:").grid(column=2, row=4, sticky=W)
	ttk.Label(frame, text="Age:").grid(column=2, row=5, sticky=W)
	ttk.Label(frame, text="Gender:").grid(column=2, row=6, sticky=W)
	ttk.Label(frame, text="Weight:").grid(column=2, row=7, sticky=W)
	ttk.Label(frame, text="BMI:").grid(column=2, row=8, sticky=W)
	ttk.Label(frame, text="ICD9:").grid(column=2, row=9, sticky=W)
	ttk.Label(frame, text="CPT:").grid(column=2, row=10, sticky=W)
	ttk.Label(frame, text="Penicillin allergy:").grid(column=2, row=11, sticky=W)
	ttk.Label(frame, text="ADNet score:").grid(column=2, row=12, sticky=W)
	ttk.Label(frame, text="ASA score:").grid(column=2, row=13, sticky=W)
	ttk.Label(frame, text="BUN:").grid(column=2, row=14, sticky=W)
	ttk.Label(frame, text="Glucose:").grid(column=2, row=15, sticky=W)
	ttk.Label(frame, text="Potassium (K):").grid(column=2, row=16, sticky=W)
	ttk.Label(frame, text="CO2:").grid(column=2, row=17, sticky=W)
	ttk.Label(frame, text="Calcium (CA):").grid(column=2, row=18, sticky=W)


	address_entry = ttk.Entry(frame, width=20, textvariable=address)
	password_entry = ttk.Entry(frame, show="*", width=20, textvariable=password)
	separator = ttk.Separator(frame, orient=HORIZONTAL)
	name_entry = ttk.Entry(frame, width=20, textvariable=name)
	dob_entry = ttk.Entry(frame, width=20, textvariable=dob)
	age_entry = ttk.Entry(frame, width=20, textvariable=age)
	gender_entry = ttk.Entry(frame, width=20, textvariable=gender)
	weight_entry = ttk.Entry(frame, width=20, textvariable=weight)
	bmi_entry = ttk.Entry(frame, width=20, textvariable=bmi)
	icd9_entry = ttk.Entry(frame, width=20, textvariable=icd9)
	cpt_entry = ttk.Entry(frame, width=20, textvariable=cpt)
	penicillin_allergy_entry = ttk.Entry(frame, width=20, textvariable=penicillin_allergy)
	adnet_entry = ttk.Entry(frame, width=20, textvariable=adnet)
	asa_entry = ttk.Entry(frame, width=20, textvariable=asa)
	bun_entry = ttk.Entry(frame, width=20, textvariable=bun)
	glucose_entry = ttk.Entry(frame, width=20, textvariable=glucose)
	k_entry = ttk.Entry(frame, width=20, textvariable=k)
	co2_entry = ttk.Entry(frame, width=20, textvariable=co2)
	ca_entry = ttk.Entry(frame, width=20, textvariable=ca)

	address_entry.grid(column=3, row=0, sticky=(W, E))
	password_entry.grid(column=3, row=1, sticky=(W, E))
	separator.grid(column=3, row=2, sticky=(W, E))
	name_entry.grid(column=3, row=3, sticky=(W, E))
	dob_entry.grid(column=3, row=4, sticky=(W, E))
	age_entry.grid(column=3, row=5, sticky=(W, E))
	gender_entry.grid(column=3, row=6, sticky=(W, E))
	weight_entry.grid(column=3, row=7, sticky=(W, E))
	bmi_entry.grid(column=3, row=8, sticky=(W, E))
	icd9_entry.grid(column=3, row=9, sticky=(W, E))
	cpt_entry.grid(column=3, row=10, sticky=(W, E))
	penicillin_allergy_entry.grid(column=3, row=11, sticky=(W, E))
	adnet_entry.grid(column=3, row=12, sticky=(W, E))
	asa_entry.grid(column=3, row=13, sticky=(W, E))
	bun_entry.grid(column=3, row=14, sticky=(W, E))
	glucose_entry.grid(column=3, row=15, sticky=(W, E))
	k_entry.grid(column=3, row=16, sticky=(W, E))
	co2_entry.grid(column=3, row=17, sticky=(W, E))
	ca_entry.grid(column=3, row=18, sticky=(W, E))

	# Buttons
	get_button = ttk.Button(frame, text="Get Record", command=get_record)
	set_button = ttk.Button(frame, text="Set Record", command=set_record)
	clear_button = ttk.Button(frame, text="Clear", command=clear)

	get_button.grid(column=2, row=19, sticky=W)
	set_button.grid(column=3, row=19, sticky=W)
	clear_button.grid(column=4, row=19, sticky=W)

	# Status box
	status_box = ttk.Labelframe(frame)
	status_box.grid(row = 20, sticky=W, columnspan=4)
	status_label = ttk.Label(status_box, textvariable=status)
	status.set("Waiting for input.")
	status_label.grid(columnspan=4, sticky=N)

	for child in frame.winfo_children():
		child.grid_configure(padx=5, pady=5)

	root.mainloop()
