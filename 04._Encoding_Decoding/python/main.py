txt = "My name is Ståle"

x = txt.encode()

print(type(x))

decoded_string = x.decode() 
print('The decoded string is :')
print(decoded_string) 