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
            if(unity1 == 'kg'):
                result = 'Unidades iguais => {:.2f} Quilogramas'.format(value)

            elif(unity1 == 'g'):
                result = 'Unidade iguais => {:.2f} Gramas'.format(value)
            else:
                result = 'Unidade iguais => {:.2f} Miligramas'.format(value)

        elif (unity1 != 'sel' and unity2 =='sel'):
            result = 'Erro: Selecione uma unidade !'

        elif unity1 == 'kg':
            if (unity2 == 'gr'):
                result = '{} Quilogramas = {:.2f} Gramas'.format(value, (value * 1000))

            elif (unity2 == 'mg'):
                result = '{} Quilogramas = {:.2f} Miligramas'.format(value, (value * 1000000))

        elif unity1 == 'gr':
            if (unity2 == 'kg'):
                result = '{} Gramas = {:.4f} Quilogramas'.format(value, (value / 1000))

            elif (unity2 == 'mg'):
                result = '{} Gramas = {:.2f} Miligramas'.format(value, (value * 1000))

        elif unity1 == 'mg':
            if (unity2 == 'kg'):
                result = '{} Miligramas = {:.6f} Quilogramas'.format(value, (value / 1000000))

            elif (unity2 == 'gr'):
                result = '{} Miligramas = {:.4f} Gramas'.format(value, (value / 1000))

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
print('<title>Resultado: Massa</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(resultFinal))
print('<a class="back" href="../massa.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")