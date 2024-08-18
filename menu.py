from app import get_add_button, openPage


# Program Summary: Stores locations of 'add' buttons for the specific class you want so that during your pass time you can quickly add them to your schedule
# Have to approve Duo Push from phone every time


classes_dicts = []

text = """
Enter :
- a: To add a class to your registration cart
- r: To remove a class from your registration cart
- d: To click add buttons for all classes (Hint: Do this right as your pass time starts, CANNOT BE DONE BEFORE)
"""

ucsb_user = input("Enter your UCSB username:")
ucsb_pass = input("Enter your UCSB password:")



user_input = input(text)

while user_input != "q":


    if user_input == "a":
        cname = input("Enter only the name part of the class, Ex: ANTH 3 INTRO ARCH --> INTRO ARCH ")
        encode = input("Enter the enrollment code of the specific section you'd like to sign up for")
        classes_dicts.append(get_add_button(ucsb_user, ucsb_pass, cname.strip(), encode.strip()))

    if user_input == "r":
        encode = input("Enter the enrollment code of the specific class you'd like to remove").strip()

        for x in classes_dicts:
            if x["enrollment code"] == encode:
                classes_dicts.remove(x)

    if user_input == "d":
        openPage(ucsb_user, ucsb_pass)
        for i in classes_dicts:
            i["button"].click()


    if user_input == "l":
        for j in classes_dicts:
            print(f"{j['name']} - {j['enrollment code']}")


    user_input = input(text)