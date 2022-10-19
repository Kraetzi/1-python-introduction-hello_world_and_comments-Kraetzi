# In here we try out some print commands in connection with different types

print(int(234))
print(float(43.12))
print(complex(3+2j))
print("'Hello'")
print(bool(1))
print("") #just for styling and separating tasks

"""In here we try to print values and there types in a sentence-like structure
"""
print(123, 'is type of', type(123))
print(4.23, 'is type of', type(4.23))
print((4-1j), 'is type of', type((4-1j)))
print("'How are you'", 'is type of', type("How are you"))
print(True, 'is type of', type(True))
print("") 
print(isinstance(44, int))
print(isinstance('city', str))
print(isinstance(3+2j, complex))
print(isinstance(True, bool))
print(isinstance(3.6, float))
print ("")
print('Is 123 an instance of int?:', isinstance(123, int))
print('Is 43.23 ans instance of bool?:', isinstance(43.23, bool))
print('is 4-1j an instance of complex?:', isinstance(4-1j, complex))
print('Is True an instance of bool?:', isinstance(True, bool))
print('Is "How are you?" an instance of float?:', isinstance('How are you', float))
print("")
