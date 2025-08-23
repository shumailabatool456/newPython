# Functions with output
def formate_name(f_name, l_name):
    print(f_name.title()) 
    print(l_name.title())
formate_name("shumaila", "batool")
# Also
def formate_name(f_name, l_name):
    formated_f_name =f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")
formate_name("shumaila", "batool")
#And
def formate_name(f_name, l_name):
    full_name = f_name + " " + l_name
    print(full_name.title())
formate_name("shumaila", "batool")

