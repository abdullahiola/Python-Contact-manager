import collections 
from dbconnect import cursor, connection


def tuple_to_named_tuple(contact_list):    
    # create a namedtuple for row from db
    contact_tp = collections.namedtuple('contact',['id','firstname','lastname','email','phonenumber'])
    all_contact=[]
    for contact in contact_list:
        # convert each tuple contact to named tuple
        c=contact_tp(*contact)
        #add the contact tuple to all_contact list
        all_contact.append(c)
    return all_contact
        


def get_all_contact():
    query_string = 'select * from contact'
    cursor.execute(query_string)
    contacts=cursor.fetchall()
    return tuple_to_named_tuple(contacts)

def search_contact(word):
    #search by lastname 
    query = f"select * from contact where lastname like '%{word}%' or firstname like '%{word}%' "
    cursor.execute(query)
    result = cursor.fetchall()
    return tuple_to_named_tuple(result)

def add_a_contact(firstname, phone,lastname, email):
    firstN = firstname.strip()
    lastN = lastname.strip()
    emaiL = email.strip()

    if firstN == "" or firstN == None:
        print('first name required')
    elif lastN == "" or firstN == None:
        print('first name required')
    elif emaiL == "" or emaiL == None:
        print('first name required')
    else:
        query = "insert into contact(firstname,lastname,email,phone)values('{}','{}','{}','{}')".format(
            firstname, lastname, email, phone)
        cursor.execute(query)
        # to write the the changes into the database
        connection.commit()

def update_contact(id,first_name = "",last_name ="",email="",phone=""):
    query = f"""
    update contact
    set lastname='{last_name.lower()}', email = '{email.lower()}', firstname = '{first_name.lower()}', phone = '{phone}'
    where contactid={id}
    """
    cursor.execute(query)
    connection.commit()
    print(f"Contact with contactId {id} is being updated")

def get_a_contact(firstname):
    query = f"select *from contact where firstname = '{firstname}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def delete_a_contact(id):
    query = f"delete from contact where contactid = {id}"
    cursor.execute(query)
    connection.commit()
    print(f"contact with id {id} succesfully deleted")

if __name__ == '__main__':
    get_all_contact()
    #search_contact('t')
    connection.close()

