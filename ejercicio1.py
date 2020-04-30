print ("BIENVENIDO A EMPAREJANDO.COM")

nombre= input("Tu nombre :")
ano= int(input( "¿Año de nacimiento? :" ))
tegusta= input("¿Te gusta taburete? :")

edad  =  2020 - ano

print ("hola", nombre, ". Si no me equivoco tienes", edad, "años.")

if tegusta == "si" or tegusta == "Si":
  print('OK Boomer, lo tuyo va a ser un caso difícil.')
elif tegusta == "no" or tegusta == "No":
  print('Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.')
  
  


num=0

while (num<=edad-1):

  #sum=num+sum

  num=num+1

  print('Que no cumple ' +str(num-1))
else:
    (num<=edad)
    print ("Que si cumpla" ,num)