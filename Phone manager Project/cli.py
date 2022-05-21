# a command line interface for phone book manager
import sys
import phonenumber as pm

try:
    argument =sys.argv[1].lower()

    if argument == 'help':
        print("""
          -------  Welcome to the help section of the phonebook manager --------
           ----- addcontacts -> To add new contact ------
          ---  searchcontact -> To search for a specific contact by lastname ---
           --------- getallcontacts -> Returns all contacts --------
           ------- getacontact -> gets a contact using firstname -----
           ------- deletecontact -> deletes a contact using the specified id ------
           ------- Updateacontact -> Update a new contact -------- (--)
        
    
        """)
    elif argument == 'getallcontacts':
        print('getting all the contacts')
        all_contact=pm.get_all_contact()
        for contact in all_contact:
            print(contact)

    elif argument == 'addcontact':
        data = sys.argv[2]
        if len(data)>1:
            list_data ={}
            for element in list_data:
                key, value =element.split(':')
                our_dict[key]=value
            pm.add_a_contact(
                our_dict.get('firstname'),
                our_dict.get('phone'),
                our_dict.get('lastname') or '',
                our_dict.get('email') or ''
                )

    elif argument =='searchcontact':
        x=input('what is the contact last name?')
        #prompts for a response and search using lastname
        result=pm.search_contact(x)
        print(result)

    elif argument =='getacontact':
        #input the contact name after your argument 
        data= input('what is the contact firstname? ')
        result=pm.get_a_contact(data)
        print(result)

    elif argument =='deleteacontact':
        fill=input('what is the contact id?')
        pm.delete_a_contact(fill)

    elif argument =="addcontacts":
        firstname=input('what is your firstname ')
        lastname=input('what is your lastname ')
        phone=input('what is your phonenumber ')
        email=input('what is your email ')
        pm.add_a_contact(firstname, phone, lastname, email)
        print('contact has been added successfully')

    elif argument =='updateacontact':
        id=sys.argv[2]
        firstname=input('what is your firstname ')
        lastname=input('what is your lastname ')
        phone=input('what is your phonenumber ')
        email=input('what is your email ')
        pm.update_contact(id,firstname,lastname,phone,email)
        print('Contact has been sucessfully updated')

        



        
except Exception as ex:
    print("""
    invalid argument 
    ------------------------
     Type help to get a list of arguments
     
     
     
      """)
