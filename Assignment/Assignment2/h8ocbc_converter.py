c=10; k=10; f=10 
# soal 1
def input(kelvin): #menambahkan fungsi input
    '''
        kita akan menambahkan fungsi input
        membuat parameter Celcius dan Kelvin
    '''
    celcius = kelvin - 273.15 ; 
    kelvin = celcius + 273.15;
    print("hasil Kelvin ke celcius : ", celcius)
    print("hasil Celcius ke Kelvin : ", kelvin)
    return celcius, kelvin

print("nilai awal Kelvin   : ",k)
input(10)
print("")
#soal 2
def input(nilai, satuan):
    '''
        kita akan menambahkan fungsi input dengan 2 argumen
        membuat percabangan
        jika satuan c maka menjalankan parameter farenheit1
        dan jika satuan c maka menjalankan parameter farenheit2
    '''
    if satuan=='c':
        farenheit1 = nilai*5/9 + 32;
        print("Nilai Celcius ke  farenheit  : ",farenheit1,"C")
    elif satuan=='k':
        farenheit2=(nilai+32)*9/5-273;
        print("Nilai kelvin ke farenheit  : ",farenheit2,"F")
    else: 
        print("not found")
    
print("Nilai Farenheit  : ", f,"F")
input(10,'k')
print("")
#soal 3
def input(farenheit, satuan):
    '''
        kita akan menambahkan fungsi input dengan 2 argumen
        membuat percabangan
        jika satuan c maka menjalankan parameter Celcius
        dan jika satuan c maka menjalankan parameter Kelvin
    '''
    if satuan=='c':
        celcius = (farenheit-32)*5/9;
        print("Nilai farenheit ke celcius   : ",celcius,"F")
    elif satuan=='k':
        kelvin=(farenheit-32)*5/9+273;
        print("Nilai farenheit ke kelvin   : ",kelvin,"K")
    else: 
        print("not found")
    
print("Nilai Farenheit  : ", f,"F")
input(10,'k')