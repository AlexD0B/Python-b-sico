cantidad_bolivares = input("Cuantos bolivares tienes?: ")
cantidad_bolivares = float(cantidad_bolivares)
valor_dolar = (input("Que precio tiene el dolar?: "))
valor_dolar = float(valor_dolar)
dolares = cantidad_bolivares / valor_dolar
dolares = str(dolares)
print("Tienes " + dolares + " bolivares")
