import re


class EmailValidator:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise ValueError(f"Invalid email address: {email}")

    @classmethod
    def validate(cls, email):

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


# Example usage:
try:
    email_obj = EmailValidator("example@domain.com")
    print(f"Valid email: {email_obj.email}")
except ValueError as e:
    print(e)

try:
    email_obj = EmailValidator("invalid-email")
    print(f"Valid email: {email_obj.email}")
except ValueError as e:
    print(e)
