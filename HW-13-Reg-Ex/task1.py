import re

# Task 1 ################################################################

class PasswordTooShortError(Exception):
    pass

class NoUppercaseLetterError(Exception):
    pass

class NoLowercaseLetterError(Exception):
    pass

class NoDigitError(Exception):
    pass

class NoSpecialCharacterError(Exception):
    pass

class MyRegex:
    def __init__(self, passwd):
        self.passwd = passwd
        ...
        self.validate()

    def validate(self):
        if re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?\W).{8,}$", self.passwd):
            return 'Your password is strong enough'
        
        elif not re.match(r"(?=.*\d)", self.passwd):
            raise NoDigitError("Пароль повинен містити хоча б одну цифру")

        elif not re.match(r"(?=.*[A-Z])", self.passwd):
            raise NoUppercaseLetterError("Пароль повинен містити хоча б одну букву верхнього регістру")

        elif not re.match(r"(?=.*[a-z])", self.passwd):
            raise NoLowercaseLetterError("Пароль повинен містити хоча б одну букву нижнього регістру")

        elif not re.match(r"(?=.*\W)", self.passwd):
            raise NoSpecialCharacterError("Пароль повинен містити хоча б один спеціальний символ")
        
        elif not re.match(r"([^\s]{8,})", self.passwd):
            raise PasswordTooShortError("Пароль занадто короткий, має бути не менше 8 символів")
        
    
    
    @staticmethod
    def demo():
        
        try:
            test = MyRegex('nopassword1!').validate()
        except NoUppercaseLetterError as e:
            print(e) # Пароль повинен містити хоча б одну букву верхнього регістру
            
        try:
            test = MyRegex('Short1!').validate()
        except PasswordTooShortError as e:
            print(e) # Пароль занадто короткий, має бути не менше 8 символів

        try:
            test = MyRegex('UPPERCASE123!').validate()
        except NoLowercaseLetterError as e:
            print(e) # Пароль повинен містити хоча б одну букву нижнього регістру

        try:
            test = MyRegex('NoNumbers!').validate()
        except NoDigitError as e:
            print(e) # Пароль повинен містити хоча б одну цифру

        try:
            test = MyRegex('NoSpecialChar123').validate()
        except NoSpecialCharacterError as e:
            print(e) # Пароль повинен містити хоча б один спеціальний символ


MyRegex.demo()
    