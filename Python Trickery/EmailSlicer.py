import re

def email_slicer(email):
    if '@' not in email:
        print("Not a valid email")
        return None
    else:
        try:
            username, domain = email.split('@')
        except ValueError:
            print("Invalid email address")
            return None

        if re.match("^[A-Za-z0-9._%+-]+$", username) and re.match("^[A-Za-z0-9.-]+$", domain):
            print('Username:', username)
            print('Domain:', domain)
            return username, domain
        else:
            print("Invalid characters in email")
            return None
