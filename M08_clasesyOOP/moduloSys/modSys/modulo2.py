# # modulo2.py 

# def suma(a,b):
#     return a+b  

# c = suma(1,2)

# print("La suma es: ",c)


# edicion para que al cargar el modulo no se ejecute la suma

def suma(a,b):
    return a+b 

if (__name__ == '__main__'):
    c = suma(1,2)
    print("La suma es: ",c)