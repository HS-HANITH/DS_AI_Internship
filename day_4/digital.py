contacts = {
    "Ravi": 9876543210,
    "Anita": 9123456789,
    "Suresh": 9988776655
}
contacts["Meena"] = 9012345678
contacts["Ravi"] = 900000000
existing_contact = contacts.get("Anita", "Contact not found")
missing_contact = contacts.get("Rahul", "Contact not found")

# Step 5: Display all contacts
print("Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")

# Step 6: Print safe lookup results
print("\nSafe Lookups:")
print("Anita:", existing_contact)
print("Rahul:", missing_contact)
