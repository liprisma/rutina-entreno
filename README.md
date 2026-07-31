# RUTINA-ENTRENO
## Instalalar y ejecutar el programa
### MacOS, Linux y gitTerminal(Windows)
```
git clone https://github.com/liprisma/rutina-entreno.git
git cd rutina-entreno
git python3
```
Una vez se ejecute el programa siga las instrucciones del programa y obtendrá su rutina
Nota:
> Es posible que en algunos IDLE y en terminales pequeñas o en dispositivos pequeños no se puedan ver los títulos bien porque están hechos con ASCII ART

Si elije guardar el resultado en un .txt este se guardará en la misma carpeta en la que está el programa con el nombre `resultado.txt'

## Añadir más ejercicios
Si quiere añadir más ejercicios de un grupo múscular asegurate de que tengan ",", si no lo tienen el programa no detectará el nuevo ejercicio y dará fallos.

Para añadir un nuevo grupo muscular solo añada su nombre sin ninguna coma "," o doble punto ":".

Para añadir un nuevo grupo de calentamiento asegurate de que tenga doble punto":" al final

y por último para añadir un nuevo ejercicio de calentamiento asegurate de que no tenga doble punto ":"

El programa se adaptará a las modificaciones que haga en el txt

## Datos importantes

El programa asume que cada ejercicio durá 5 minutos y descuenta 10 minutos de calentamiento al tiempo que haya añadido que quiera entrenar cada día.
Almenos un ejercicio de cada grupo múscular es agregado idependientemente de la cantidad de días y de tiempo por día
NOTA:
> Si agrega muchos grupos músculares y luego asigna muy pocos días y tiempo de sesión es posible que no sea posible añadirlos todos, en tal caso el programa añadira de manera aleatoria la mayor cantidad posible de grupos músculares antes de que tiempo se agote.
