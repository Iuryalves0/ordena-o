""" 
Dada uma lista de palavras, escreva um programa que solicite ao usuario uma lista de frutas
e mostre:
- a lista original
- a lista ordenada
- a lista na ordem inversa
 caso o usuario digite sair, pare de solicitar dados.
"""
import os
os.system("cls||clear")

lista_frutas = []

while True:
    nome = input("Digite uma fruta: ")
    if nome == "sair":
        break
    else:
        lista_frutas.append(nome)

lista_organizada = sorted(lista_frutas)
lista_invertida = sorted(lista_frutas, reverse=True)
#exibindo resultados
print("lista digitada pelo usuario: ")
print(lista_frutas)

print("\nlista de maneira ordenada: ")
print(lista_organizada)

print("\nlista inversa: ")
print(lista_invertida)