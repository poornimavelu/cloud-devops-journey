## normal concat
a="Cookie and\t";
b="Cream"
ice_cream_flavour = a+b;
print("Hey yo, today's ice cream flaour is:" ,ice_cream_flavour )

## before using str

a="ten rupees"
b="15.7"
total_paise = a+b;
print ("homies all we have is:" , total_paise)

## after using str

a="ten rupees"
b= 15
total_paise = a+str(b);
print ("homies all we have is:" , total_paise)

##using len()

name="bubu"
length=len(name)
print("the number of letters in my nickname is:", str(length))

#using upper , lower

print("example of upper case".upper())
print("example of lower case".lower())

#captilaing first word of upper and lower case

print("hi this is poornima".title())
print('hI THIS IS POORNIMA'.capitalize())

#Indexing

name="Poornima"

first_letter=name[0]
last_letter=name[-1]

print("My first letter of the name :",first_letter+ "\n My last letter of the name is :", last_letter)

#Slicing

name="poornima"

first_five_letters=name[:5]

print("First five letters of my name is" , first_five_letters)