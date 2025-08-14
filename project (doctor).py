import datetime

# Sample list of doctors and their available time slots
doctors = {
    "Dr. Smith": ["09:00", "10:00", "11:00", "14:00", "15:00"],
    "Dr. Johnson": ["10:00", "11:00", "13:00", "16:00"],
    "Dr. Williams": ["09:30", "11:30", "15:30"]
}

# Store booked appointments as list of dictionaries
appointments = []

def list_doctors():
    print("\nAvailable Doctors:")
    for i, doctor in enumerate(doctors, start=1):
        print(f"{i}. {doctor}")
    print()

def book_appointment():
    list_doctors()
    choice = int(input("Choose a doctor by number: ")) - 1
    if choice < 0 or choice >= len(doctors):
        print("Invalid doctor selection.")
        return
    
    doctor_name = list(doctors.keys())[choice]
    available_slots = doctors[doctor_name]
    
    if not available_slots:
        print(f"\nNo available slots for {doctor_name}.")
        return
    
    print(f"\nAvailable slots for {doctor_name}:")
    for i, slot in enumerate(available_slots, start=1):
        print(f"{i}. {slot}")
    
    slot_choice = int(input("Choose a time slot by number: ")) - 1
    if slot_choice < 0 or slot_choice >= len(available_slots):
        print("Invalid time slot selection.")
        return

    patient_name = input("Enter patient name: ")
    appointment_time = available_slots.pop(slot_choice)  # remove booked slot
    
    appointment = {
        "doctor": doctor_name,
        "patient": patient_name,
        "time": appointment_time,
        "date": datetime.date.today().strftime("%Y-%m-%d")
    }
    appointments.append(appointment)
    print(f"\nAppointment booked for {patient_name} with {doctor_name} at {appointment_time} on {appointment['date']}.")

def view_appointments():
    if not appointments:
        print("\nNo appointments booked yet.")
        return
    
    print("\nAll Appointments:")
    for i, appt in enumerate(appointments, start=1):
        print(f"{i}. Dr: {appt['doctor']} | Patient: {appt['patient']} | Time: {appt['time']} | Date: {appt['date']}")

def main():
    while True:
        print("\n--- Doctor Appointment System ---")
        print("1. List Doctors")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_doctors()
        elif choice == "2":
            book_appointment()
        elif choice == "3":
            view_appointments()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
