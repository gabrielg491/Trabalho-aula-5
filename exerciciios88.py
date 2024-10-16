# 5 faça um programa que mostre tosdos os numeros impares enre 50 a 100
import time
print("começando a contagem")
contador = 50

while contador < 101:
    print(contador)
    time.sleep(1)
    contador += 3

print("Fim da contagem")
