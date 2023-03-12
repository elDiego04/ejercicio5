def es_bisiesto(anio):

    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

print(es_bisiesto(2000))  
print(es_bisiesto(1900))  
print(es_bisiesto(2022))   
print(es_bisiesto(2024))   
