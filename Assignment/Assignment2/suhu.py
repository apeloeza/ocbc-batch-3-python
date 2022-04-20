  
# Function convert kelvin -> celcius
def convertCelciusToKelvin(celcius):
    """Returns Kelvin temperature conversion from Celcius temperature
        :param celcius: float or int
        :return: float
    """
    return celcius + 273

# Function convert celcius -> kelvin
def convertKelvinToCelcius(kelvin):
    """Returns Celcius temperature conversion from Kelvin temperature
        :param kelvin: float or int
        :return: float
    """
    return kelvin - 273

# Function convert kelvin/celcius -> fahrenheit
def convertToFahrenheit(temp, satuan):
    """Returns Fahrenheit temperature conversion either from Kelvin or Celcius,
        validates if the input temperature either Kelvin or Celcius
        :param temp: float or int
        :param satuan: string
        :return: float
    """
    if (satuan == '°K'):
        temp = convertKelvinToCelcius(kelvin = temp)
    
    temp = float(temp)
    
    return str(round(temp * (9/5) + 32, 2)) + '°F'

# Function convert fahrenheit -> celcius & kelvin
def convertFahrenheitToCelciusAndKelvin(temp):
    """Returns Kelvin and Celcius temperature conversion from Fahrenheit
       :param temp: float or int
    """
    celcius = float((temp - 32)) * (5/9)
    kelvin = convertCelciusToKelvin(celcius = celcius)

    return str(round(celcius, 2)) + '°C', str(round(kelvin, 2)) + '°K'

    

print("0°C equals " + str(convertCelciusToKelvin(0.8)) + "°K")
print("297°K equals " + str(convertKelvinToCelcius(297)) + "°C")
print("310°K equals " + convertToFahrenheit(310, '°K'))
print("27°C equals " + convertToFahrenheit(27, '°C'))
print("89°F equals ", convertFahrenheitToCelciusAndKelvin(89))
