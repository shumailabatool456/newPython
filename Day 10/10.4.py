def formated_name(f_name, l_name):
    """ Take a first and last name and format it 
    to return the title case version if the  name."""
    if f_name == "" or l_name == "":
     return "You did't provide valid input"
    formated_f_name =f_name.title()
    formated_l_name = l_name.title()
    return f" Result:{formated_f_name} {formated_l_name}"
formated_name()