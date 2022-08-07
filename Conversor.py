ciclo = True
while(ciclo):
 cantidad_dolares = input("Cuantos dolares tienes?: ")
 cantidad_dolares = float(cantidad_dolares)
 valor_dolar = (input("Que precio tiene el dolar?: "))
 valor_dolar = float(valor_dolar)
 bolivares = valor_dolar * cantidad_dolares
 bolivares = round(bolivares, 2)
 bolivares = str(bolivares)
 print("Tienes " + bolivares + " bolivares")
 consulta = input("quieres realizar otra operacion? ")
 if consulta == ("no") or (consulta == "n"):
   ciclo = False
   print("Fin")
