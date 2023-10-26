# develop a contact management program where users can edit ,add,delete and search contact details using a dictionary.the menu options would faciliate bthese actions
contact_management={}

def add_contact():
    name=input("enter the name : ")
    phone=input("enter the phone number")
    email=input("enter the email adress")
    contact_management[name]={"phone":phone,"email":email}
    print("the name is added sucessfully!!!")

def edit():
   name=input("enter the name you want to edit: ")
   if name in contact_management[name]:
        phone=("enter the phone number for {name} " )
        email=("enter the email adress for {email} " )
        contact_management[name]={"name":"name","email":"email"}
        print("details for {name} is succesfull")
   else:
        print("the name is not here.")

def delete():
    name=input("enter the name you want to delete: ")
    if name in contact_management[name]:
        del contact_management[name]
        print("the name is deleted...")
    else:
        print("the namee is not here")   

def search():
    name=input("enter the name you want to search ") 
    if name in contact_management:
        contact=contact_management[name]
        print("phone: {contact['phone']}")
        print("email : {contact['email]}")

    else:
        print("The name is not here") 

def list_all_contacts():
    print("\nAll Contacts:")
    for name, contact in contact_management.items():
        print(f"Name: {name}, Phone: {contact_management['Phone']}, Email: {contact_management['Email']}") 


def menu():
    print("1.Add contacts ")
    print("2.edit ")
    print("3.delete ")
    print("4.search ")
    print("5.exit ")


while True:
    menu()
    choice=int(input("enter your choice"))
     
    if choice==1:
        add_contact()
        list_all_contacts()
    elif choice==2:
        edit()
        list_all_contacts()
    elif choice==3:
        delete()
        list_all_contacts()
    elif choice==4:
        search()
        
    elif choice==5:
        exit()
    else:
        print("invalid input")