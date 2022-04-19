kelvin = 10 #mendeklarasikan variabel 
def input(kelvin): #menambahkan fungsi input
    celcius = kelvin - 273.15 ; 
    kelvin = celcius + 273.15;
    print("hasil Kelvin ke celcius : ", celcius)
    print("hasil Celcius ke Kelvin : ", kelvin)
    return celcius, kelvin

print("Nilai Kelvin     : ", kelvin)
celcius = input( 10)
print("")

celcius = 10 #mendeklarasikan variabel 
def input(celcius):
    farenheit = celcius*9/5+32;
    print("Nilai Celcius ke Farenheit : ", farenheit, "F")
    return farenheit

print("Nilai Celcius     : ", celcius,"C")
farenheit= input(10)
print("")

farenheit = 10 #mendeklarasikan variabel 
def input(farenheit):
    celcius = (farenheit-32)*5/9;
    print("Nilai farenheit ke celcius   : ",celcius,"C")
    return celcius

print("Nilai Farenheit  : ", farenheit,"F")
celcius= input(10)
