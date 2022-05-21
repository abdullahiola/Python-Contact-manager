import phonenumber
from phonenumber import cursor, connection
from tkinter import *

root = Tk()
root.title('CONTACT MANAGER')

e = Entry(root, width=30, borderwidth=10)
e.grid(row=0, column=0, columnspan=20)
def search():
    pass

def add_a_contact(firstname, phone,lastname, email):
    firstN = firstname.strip()
    lastN = lastname.strip()
    emaiL = email.strip()

    if firstN == "" or firstN == None:
        print('first name required')
    elif lastN == "" or firstN == None:
        print('last name required')
    elif emaiL == "" or emaiL == None:
        print('email is required')
    else:
        query = "insert into contact(firstname,lastname,email,phone)values('{}','{}','{}','{}')".format(
            firstname, lastname, email, phone)
        print(query)
        cursor.execute(query)
        # to write the the changes into the database
        connection.commit()

def edit(id,first_name,last_name,email,phone):
    query = f"""
    update contact
    set lastname='{last_name.lower()}', email = '{email.lower()}', firstname = '{first_name.lower()}', phone = '{phone}'
    where contactid={id}
    """
    cursor.execute(query)
    connection.commit()
    print(f"contact with contactId {id} has being updated")

def delete():
    pass

search_btn = Button(root, text='Search', font=('Algerian', 19), fg='white', bg='light blue', command=search)
add_btn = Button(root, text='Add', font=('Algerian', 20), fg='white', bg='red', command=add_a_contact(firstname='chris',lastname='taj', email='imhanlahimichristabel@gmail.com', phone='07043255869'))
edit_btn = Button(root, text='Edit', font=('Algerian', 20), fg='white', bg='green', command=edit(id=9, last_name='imhanlahimi', email='', phone='07043255869', first_name='christabel'))
delete_btn = Button(root, text='Delete', font=('Algerian', 20), fg='white', bg='black', command=delete)

search_btn.grid(row=0, column=20)
add_btn.grid(row=1, column=0)
edit_btn.grid(row=1, column=10)

delete_btn.grid(row=1, column=20)

root.mainloop()
