# Python-Weather-App
A Python program that tells you the weather, using the Open Weather API, both in celsius and fahrenheit
The majority of the code was developed using ask python, with some changes to make the app more user friendly. 
Here is the link of for the website to see more on how it works, what libraries you need and why. If you want to just use that code, follow the link. https://www.askpython.com/python/examples/gui-weather-app-in-python
If you want to be able to switch from celsius to farhenheit, use mine, particulariy the functions that allow you to switch. 

MAJOR TIP 
if you get this error from the console:
AttributeError: 'NoneType' object has no attribute 'delete'

Fix the text field error. Instead of writing :
textfield = Text(mainWindow, width=46, height=9,
                 font=(40)).pack()
Write: 
textfield = Text(mainWindow, width=46, height=9,
                 font=(40))
textfield.pack(pady="10")
