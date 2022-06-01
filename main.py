# Crear fichero de texto para agregar párrafos o frases
# Devolver la cantidad de palabras contenida en el fichero

f = open('words.text', 'w')
while True:
    
    f.write(input("Introduce un párrafo o frase: \n "))
    f.write(" ")
    if input("¿Desea ingresar otro párrafo o frase? si/no \n").lower() == "no":
        break

f = open('words.text', 'r')
num_words = 0
for line in f:
    words = line.split()
    print(words)
    num_words = num_words + len(words)
print("La cantidad de palabras es: ", num_words)