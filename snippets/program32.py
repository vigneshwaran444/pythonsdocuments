class MyClass:
   variable="blah"

def function(self):
  print("this is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable="yackity"

#Then print out both values

print(myobjectx.variable)
print(myobjecty.variable)
