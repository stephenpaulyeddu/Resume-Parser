from tika import parser
import re
from nltk.tokenize import word_tokenize
from nltk import pos_tag

############################################################################################################

# get mobile numbers from text as list 
def get_mobile_number(mobile: str):
    
    # removing spaces from the numbers to clean the input ( to deal with cases like "91 99999 99999" )
    mobile = mobile.replace(' ','')
    
    # Collect all the numerical matches in a list object - mobile_digits
    mobile_digits = re.findall("[0-9]+",mobile)
    
    # create a function internally to return a valid mobile number - This will return true if the digit is 10 or 12 in length
    def is_atleast_10_12_digit(mobile_1):
        return (len(mobile_1) == 10 or len(mobile_1) == 12) # 12 digit because of 91
    

    """
        Remove the 3-4 digit numbers from the list
        These can come up because we pass in entire line as an input 
        and if the line has "mobile: 9999999999 email: iamanemail234@gmail.com"
        then the list will contain [9999999999,234] -- will need to remove 234 from here
    """ 
    
    # Filtering the collection of list for 10 digit number or 12 digit number
    mobile_digits = list(filter(is_atleast_10_12_digit,mobile_digits))
    
    
    """
    Create another list mobile_digits_updated.. which stores valid numbers  
        if the length of digits are 10 then store directly
        if the length of digits are 12 and number starts with 91 -- Removes 91 and stores the 10 digit number
        else it drops the number ( we drop all the 12 digit numbers starting without 91 using the following code - invalid numbers)
    """
    mobile_digits_updated = []
    
    for i in range(len(mobile_digits)):
        if (len(mobile_digits[i]) == 10):
            mobile_digits_updated.append(mobile_digits[i])
        if (len(mobile_digits[i]) == 12 and mobile_digits[i][:2] == '91'):
            mobile_digits_updated.append(mobile_digits[i][2:])
        else:
            pass
    
    try:
        return mobile_digits_updated
    except:
        pass


#########################################################################################################################################


# Identifying email

#get emails from text as string
def get_email(email: str):
    try:
        # find all the combinations of email in the FORM -  "any_string@any_string.any_string"
        element = re.findall('(\S+@\w+.\w+)',email)
        
        # element can have inputs like "Email:any_string@any_string.any_string","Email-any_string@any_string.any_string"
        # in these cases we split string by :,- and take the last string
        
        element_1 = element[0].split("-")
        element_2 = element[0].split(":")
        
         # element = ["Email:any_string@any_string.any_string"]
        # element_2 = ["Email","any_string@any_string.any_string"] -- After SPLIT by :
        # In both the cases last element is the email. so we take the last element from all the 3 lists, element, element_1 and element_2 and append it to new list object email.
        
        emails = []
        emails.append(element[-1].strip())
        emails.append(element_1[-1].strip())
        emails.append(element_2[-1].strip())
        
        ## Email can contain ["Email:any_string@any_string.any_string","any_string@any_string.any_string"] - so we sort it by length and take the first object.
        emails.sort(key = len)
        
        return emails[0]
    except:
        pass


#############################################################################################################################

# get name from keyword:

def get_name_from_keyword(name):
     if(re.findall(r'NAME',name.upper())):
        name = name.upper()
        name = name.replace('NAME','') ## Remove the Word "NAME"
        
        updated_name = ' '
        for j in name:
            if(re.findall(r'[a-zA-Z]', j) or j == ' '):
                updated_name += j  ## Update the name if we find only alphabets, This will remove characters :,- etc
            
        updated_name = updated_name.strip() # Strip for additional spaces.
    
        if name != '':
            return updated_name.title()
        else:
            return None