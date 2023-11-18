import extract_fields

# a = extract_fields.get_mobile_number(" Mobile NUmber: 9922119922") # get mobile numbers from any text
# print(a)

# b = extract_fields.get_email(" Email: i_am_an_email@gmail.com") # get email from any text
# print(b)

# c = extract_fields.get_name_from_keyword("Name - I am a Name") # this returns name if keyword Name is present
# print(c)


resume_loc = "C:\\Users\\this pc\\Downloads\\Jaswanth's Resume.pdf"

parsed_resume = extract_fields.parser.from_file(resume_loc)

list_ = parsed_resume['content'].split('\n')

print(list_)