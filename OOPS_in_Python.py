# Object Oriented Programming in Python

class Computer: # this is a CLASS
  def __init__(self, cpu, ram, storage): # this is a Constructor
    self.cpu = cpu
    self.ram = ram
    self.storage = storage
    
    # "self" keyword refers to the object, same as `this` keyword in JAVA
  
  def config(self): # this is a Method
    print("Processor: "+self.cpu)
    print("RAM: "+ str(self.ram) + "GB")
    print("Storage: "+self.storage)
    
# Function written in a class is called as METHOD

computer1 = Computer("i5 11th gen", 32, "1TB") # this is an OBJECT of class computer
computer1.config() # one way of calling methods

computer2 = Computer("Ryzen 9", 16, "500GB")
Computer.config(computer2) # another way of calling methods

# CONSTRUCTOR allocates the size of an object

####################################################################################################################################################################

# Types of variables in Python
# 1. Instance variable
# 2. Class (static) variable

class Car:
  wheels = 4 # this variable belongs to Class namespace
  def __init__(self):
    # the below two variables, "mil" & "company" belongs to Instance namespace
    self.mil = 10 
    self.company = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 15
c1.company = "Audi"

Car.wheels = 5

print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)

# namespace is an area where you create and store object/variable
# - Class namespace
# - Object/Instance namespace

####################################################################################################################################################################

# Types of Methods in Python
# 1. Instance methods - works with Instance variables
# 2. Class methods - works with Class variables
# 3. Static methods - nothing to do with Instance/Class variables

class Student:
  school = "CVR School of Engineering"

  def __init__(self, m1, m2, m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  def avg(self):
    return (self.m1 + self.m2 + self.m3)/3

  def get_m1(self): # Getters or Accessors
    return self.m1

  def set_m1(self, value): # Setters or Mutators
    self.m1 = value
  
  @classmethod # decorators
  def getSchool(cls):
    return cls.school

  @staticmethod
  def info():
    print("This is a student class in abc module")

s1 = Student(38,56,46)
s2 = Student(46,68,34)

print(s1.avg())
print(s2.avg())

# Accessors Methods - If you want to just fetch the value of Instance variable
# Mutators Methods - If you want to modify the value of Instance variable

print(Student.getSchool())
print(s1.getSchool())
print(Student.info())

####################################################################################################################################################################

# Inner Class in Python
# Can we have a class inside a class?

class Student: # Outer class

  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno
    self.lap = self.Laptop()

  def show(self):
    print(self.name, self.rollno)
    self.lap.show()
  
  class Laptop: # Inner class
    def __init__(self):
      self.brand = "Apple"
      self.cpu = "M1 Pro"
      self.ram = 16

    def show(self):
      print(self.brand, self.cpu, self.ram)

# You can create object of inner class inside the outer class OR 
# You can create object of inner class outside the outer class provided you use outer class name to call it


s1 = Student("Imtiyaz",78)
s2 = Student("Kiran", 98)
s3 = Student("Preetham", 93)

s1.show()
s2.show()
s3.show()

# lap1 = s1.lap()
# lap2 = s2.lap()

# lap1 = Student.Laptop()
# lap1.show()

#lap1 = s1.lap()
s1.show()

####################################################################################################################################################################

# Inheritance in Python
# Using Existing Features of Existing class is known as Inheritance
# In the below code, A is Super Class / Parent Class && B is Sub Class / Child Class

class A:
  def feature1(self):
    print("Feature 1 is working")

  def feature2(self):
    print("Feature 2 is working")

class B(A): # Class B is Child class of class A, B inheritance all the features of A
  def feature3(self):
    print("Feature 3 is working")

  def feature4(self):
    print("Feature 4 is working")

class D:
  def feature6(self):
    print("Feature 6 is working")

  def feature7(self):
    print("Feature 7 is working")

class C(B, D):
  def feature5(self):
    print("Feature 5 is working")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature1()

c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()
c1.feature6()

####################################################################################################################################################################

# Constructor in Inheritance in Python

# Constructor
# Method Resolution Order

# If you create an object of Sub class, it will first try find init of Sub class
# if it's not found, then it'll call init of Super class

class A:
  def __init__(self):
    print("in A init")

  def feature1(self):
    print("Feature 1-A is working")

  def feature2(self):
    print("Feature 2 is working")

class B: 
  def __init__(self):
    #super().__init__()
    print("in B init")

  def feature1(self):
    print("Feature 1-B is working")

  def feature4(self):
    print("Feature 4 is working")

class C(A,B):
  def __init__(self):
    super().__init__()
    print("in C init")

  def feat(self):
    super().feature2()

a1 = C()
a1.feat()

####################################################################################################################################################################

# Polymorphism in Python

# Poly - many
# morph - forms
# One thing can take many forms - polymorphism

# Four Types to implement Polymorphism
# 1 -> Duck Typing
# 2 -> Operator Overloading
# 3 -> Method Overloading
# 4 -> Method Overriding

####################################################################################################################################################################

# Duck Typing in Python

class PyCharm:
  def execute(self):
    print("Compiling...")
    print("Running...")

class MyEditor:
  def execute(self):
    print("Spell Check...✅")
    print("Convention Check...✅")
    print("Compiling...")
    print("Running...")

class Laptop:
  def code(self, ide):
    ide.execute()

ide = MyEditor()

l1 = Laptop()
l1.code(ide)

####################################################################################################################################################################

# Operator Overloading

class Student:
  def __init__(self, m1, m2):
    self.m1 = m1
    self.m2 = m2

  def __add__(self, other):
    m1 = self.m1 + other.m1
    m2 = self.m2 + other.m2
    s3 = Student(m1, m2)
    return s3

  def __gt__(self, other):
    r1 = self.m1+self.m2
    r2 = other.m1 + other.m2
    return r1 > r2

s1 = Student(78,93)
s2 = Student(95,95)

s3 = s1+s2 
print(s3.m1)

if(s1 > s2):
  print("s1 wins")
else:
  print("s2 wins")

####################################################################################################################################################################

# Python doesn't have Method Overloading and Method Overriding

# Method Overloading and Method Overriding

# Methods with same names but different parameters is known as Method Overloading

# In inheritance classes, if we have two Methods of same name and same parameters, is known as Method Overriding
