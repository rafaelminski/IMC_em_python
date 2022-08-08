peso = float ( input ( "digite seu peso em kg " ))
altura = float ( input ( "digite sua altura em m " ))
imc  =  peso / altura ** 2

if  imc  <  18.5 :
        print ( "Baixo peso" )
elif  imc  <  25 :
        print ( "Peso adequado" )
elif  imc  <  30 :
        print ( "Sobrepeso" )
else :
        print ( "Obeso" )