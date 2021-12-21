#!/usr/bin/env python 3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
recieved = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')

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
    if (value != -1 and value != 'typeError'):
        if (unity1 == unity2 and unity1 != 'sel'):
            if (unity1 == 'seg'):
                result = 'Unidades iguais => {:.2f} Segundos'.format(value)

            elif (unity1 == 'min'):
                result = 'Unidade iguais => {:.2f} Minutos'.format(value)

            else:
                result = 'Unidade iguais => {:.2f} Horas'.format(value)

        elif (unity1 != 'sel' and unity2 =='sel'):
            result = 'Erro: Selecione uma unidade !'

        elif unity1 == 'seg':
            if (unity2 == 'min'):
                result = '{} Segundos = {:.2f} Minutos'.format(value, (value / 60))

            elif (unity2 == 'hr'):
                result = '{} Segundos = {:.4f} Horas'.format(value, (value / 3600))

        elif unity1 == 'min':
            if (unity2 == 'seg'):
                result = '{} Minutos = {:.2f} Segundos'.format(value, (value * 60))

            elif (unity2 == 'hr'):
                result = '{} Minutos = {:.2f} Horas'.format(value, (value / 60))

        elif unity1 == 'hr':
            if (unity2 == 'seg'):
                result = '{} Horas = {:.2f} Segundos'.format(value, (value * 3600))

            elif (unity2 == 'min'):
                result = '{} Horas = {:.2f} Minutos'.format(value, (value * 60))

        else:
            result = 'Erro: Selecione uma unidade !'

    elif(value == 'typeError'):
        result = 'Erro: Tipo de Valor inesperado !'

    else:
        result = 'Erro: Campos sem Valores !'

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
print('<title>Resultado: Tempo</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(resultFinal))
print('<a class="back" href="../tempo.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

