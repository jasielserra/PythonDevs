# -*- coding: utf-8 -*-

"""
Curso de Desenvolvedor Python

Material auxiliar para a aula Python Básico - Aula 04

Este material refere-se ao conteúdo apresentado na vídeo-aula.

Exercicio 02


"""

x = range(0,16)

#intervalo de 1 a 9
print x[1:10]


#intervalo de 8 a 13
print x[8:14]


#todos numeros pares
print x[::2]

#todos os numeros impares
print x[1::2]

#todos os multiplos de 2
todos =  x[2::2] + x[3::3] + x[4::4]
unicos_elementos = set(todos)
print list(unicos_elementos)

#lista reversa
print x[::-1]


#Razão entre a soma do intervalo 10 a 15 pelo intervalo 3 a 9 em float.
print sum(x[10:16]) / float(sum(x[3:10]))
