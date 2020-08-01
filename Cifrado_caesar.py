# CIFRADO CAESAR

message = input("Mensaje: ")
shift = int(input("Valor de desplazamiento: "))

new_message = ""

for i in message:
    if i >= "a" and i <= "z":                                                  # Procesar una minuscula determinando su posicion en el alfabeto (0-25) añadirla al mensaje
       pos = ord(i) - ord("a")
       pos = (pos + shift) % 26
       new_char = chr(pos + ord("a"))
       new_message = new_message + new_char
       
    elif i >= "A" and i <= "Z":                                                # Procesar las mayusculas
       pos = ord(i) - ord("A")
       pos = (pos + shift) % 26
       new_char = chr(pos + ord("A"))
       new_message = new_message + new_char
       
    else:                                                                      # Si el caracter no es mayuscula ni minuscula
       new_message = new_message + i
    
print("Mensaje cifrado:", new_message)
