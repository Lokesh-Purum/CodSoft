import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")
        
        # Initialize ContactBook
        self.contact_book = []

        # Create UI elements
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)

        self.label_phone = tk.Label(root, text="Phone Number:")
        self.label_phone.grid(row=1, column=0, sticky="e")
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=1, column=1)

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=2, column=0, sticky="e")
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1)

        self.label_address = tk.Label(root, text="Address:")
        self.label_address.grid(row=3, column=0, sticky="e")
        self.entry_address = tk.Entry(root)
        self.entry_address.grid(row=3, column=1)

        self.btn_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.btn_add.grid(row=4, column=0, columnspan=2, pady=10)

        self.btn_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.btn_view.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_search = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.btn_search.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.btn_update.grid(row=7, column=0, columnspan=2, pady=10)

        self.btn_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.btn_delete.grid(row=8, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        
        if name and phone_number:  # Ensure name and phone number are not empty
            contact = Contact(name, phone_number, email, address)
            self.contact_book.append(contact)
            self.listbox.insert(tk.END, f"{contact.name} - {contact.phone_number}")
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contact_book:
            self.listbox.insert(tk.END, f"{contact.name} - {contact.phone_number}")

    def search_contact(self):
        keyword = self.entry_name.get().strip()
        if not keyword:
            messagebox.showerror("Error", "Please enter a name to search.")
            return
        
        self.listbox.delete(0, tk.END)
        found = False
        for contact in self.contact_book:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                self.listbox.insert(tk.END, f"{contact.name} - {contact.phone_number}")
                found = True
        
        if not found:
            messagebox.showinfo("Not Found", "No matching contacts found.")

    def update_contact(self):
        selected_contact = self.listbox.curselection()
        if not selected_contact:
            messagebox.showerror("Error", "Please select a contact to update.")
            return
        
        index = selected_contact[0]
        contact = self.contact_book[index]
        
        new_phone_number = self.entry_phone.get()
        new_email = self.entry_email.get()
        new_address = self.entry_address.get()
        
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address
        
        self.listbox.delete(index)
        self.listbox.insert(index, f"{contact.name} - {contact.phone_number}")
        messagebox.showinfo("Success", "Contact updated successfully!")
        self.clear_entries()

    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if not selected_contact:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return
        
        index = selected_contact[0]
        del self.contact_book[index]
        self.listbox.delete(index)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        self.clear_entries()

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
