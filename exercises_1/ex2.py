# Celsius to Fahrenheit (°C to °F) App
# Write a console programme that
# (1) Allows users to enter a number as temperature in Celsius
# (2) Makes sure what users entered is valid
# (3) Prints the temperature in Fahrenheit

def convert_celsius_to_fahrenheit():
    try:
        print('Enter a number as temperature in Celsius:')
        celsius = float(input())
        print('Temperature in Fahrenheit is', (celsius*9/5 + 32))
    except:
        print('The value must be number!')
        convert_celsius_to_fahrenheit()

convert_celsius_to_fahrenheit()
