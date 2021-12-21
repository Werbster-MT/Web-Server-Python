#!/usr/bin/env python 3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
recieved = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
resultFinal = None

def analysingValue(value):
    if value:
        return int(value)
    else:
        return -1

try:
    value = analysingValue(recieved)

except:
    value = 'typeError'

def convertUnits(value, unity1, unity2):
    if(value!=-1 and value != 'typeError'):
        if (unity1 == unity2 and unity1 != 'sel'):
            if(unity1 == 'cel'):
                result = 'Unidades iguais => {:.2f} Graus Celsius'.format(value)

            elif(unity1 == 'kel'):
                result = 'Unidade iguais => {:.2f} Kelvin'.format(value)
            else:
                result = 'Unidade iguais => {:.2f} Graus Fahrenheit'.format(value)

        elif (unity1 != 'sel' and unity2 =='sel'):
            result = 'Erro: Selecione uma unidade !'

        elif unity1 == 'cel':
            if (unity2 == 'kel'):
                result = '{} Graus Celsius = {:.2f} Kelvin'.format(value, (value + 273.15))

            elif (unity2 == 'fah'):
                result = '{} Graus Celsius = {:.2f} Graus Fahrenheit'.format(value, ((1.8 * value) + 32))

        elif unity1 == 'fah':
            if (unity2 == 'cel'):
                result = '{} Graus Fahrenheit = {:.2f} Kelvin'.format(value, ((value - 32) / 1.8))

            elif (unity2 == 'kel'):
                result = '{} Graus Fahrenheit = {:.2f} Kelvin'.format(value, (((value - 32) * 5) / 273.15))

        elif unity1 == 'kel':
            if (unity2 == 'cel'):
                result = '{} Kelvin = {:.2f} Graus Celsius'.format(value, (value - 273.15))

            elif (unity2 == 'fah'):
                result = '{} Kelvin = {:.2f} Graus Fahrenheit'.format(value, ((value - 273.15) * 1.8) + 32)

        else:
            result = 'Erro: Selecione uma unidade !'

    elif (value == 'typeError'):
        result = 'Erro: Tipo de Valor inesperado !'

    else:
        result = 'Erro: Campos sem valores !'

    return result

try:
    resultFinal = convertUnits(value, unity1, unity2)

except:
    resultFinal = 'Erro Inesperado'

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Temperatura</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(resultFinal))
print('<a class="back" href="../temperatura.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

