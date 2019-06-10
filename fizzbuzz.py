#!/usr/local/bin/python3
from unittest import TestCase, main

def fizzbuzz(num):
    '''
    Função que irá retornar para a main "Fizz"
    caso seja múltiplo de 3, "Buzz" caso seja 
    múltiplo de 5 e "FizzBuzz" caso seja 
    múltiplo de 3 e 5
    '''
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz" 
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: 
        return num

class Testes(TestCase):
    def testa_fizzbuzz(self):
        #Testes com retornos "num"
        self.assertEqual(fizzbuzz(1), 1)
        #Testes com retornos "Fizz"
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(12), "Fizz")
        self.assertEqual(fizzbuzz(93), "Fizz")

        #Testes com retornos "Buzz"
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(50), "Buzz")
        self.assertEqual(fizzbuzz(70), "Buzz")
        #Testes com retornos "FizzBuzz"
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(90), "FizzBuzz")

if __name__ == "__main__":
    main()