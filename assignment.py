class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName:
            return firstName + lastName


class Costumer(Person):
    def __init__(self,gender,nameSet,firstName,lastName,streetAddress,zipCode,city,emailAddress,userName,telephoneNumber):
        self.gender = gender
        self.nameSet = nameSet
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streetAddress
        self.zipCode = zipCode
        self.city = city
        self.emailAddress = emailAddress
        self.userName = userName
        self.telephoneNumber = telephoneNumber

class Libarian(Person):
    def __init__(self):


class Author(Person):
    def __init__(self):


class Book:
    def __init__(self,Author,isbn,country,link,pages,title, year,imagelink,language):
        self.Author = Author
        self.isbn = isbn
        self.country = country
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year
        self.imagelink = imagelink
        self.language = language

class BookItem(Book):
    def __init__(self):