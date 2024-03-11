class Person:

   def __init__(self, name: str, email: str):
       self.name = name
       self.email = email

   def update_email_domain(self, new_domain: str):
       old_domain = self.email.split("@")[1]
       self.email = self.email.replace(old_domain, new_domain)


class Student(Person):

   def __init__(self, name: str, id: str, email: str, credits: str):
       self.name = name
       self.id = id
       self.email = email
       self.credits = credits

person1 = Person('pepe', 'perez')
print (person1)
print (Person.mro())
print (Person.__bases__)
print (type(Person))
student1 = Student('pepe', '1','pepe@gmail.com','18')
print (student1)
print (Student.mro())
print (Student.__bases__)
print (type(Student))
