## Navegación
**Es como nos movemos en la interfaz**

PWD: printo work directory: es nuestro GPS y nos informa donde estamos
ls: list : muestra todo lo que esta dentro de una carpeta, es como usar el finder y ver que hay dentro de una
ls -la: es la version detallada de list: nos muestra los permisos, tamano y fecha del archivo, l es "long" detallado, "a" es all incluyendo los archivos ocultos
ls -lah: igual que la pero con formato legible de tamano como K,M,G en vez de grandes numeros
cd nombre-carpeta: change directory: nos movemos en la carpeta es como hacer doble click en una carpeta en finder
cd.. : sube un nivel, ejemplo de esta carpeta de dia 1 a devops semana1
cd../.. sube dos niveles a la vez
cd ~: te lleva directo a la carpeta de usuario
cd - regresa a carpeta anterior
/users/admin: nos lleva a la carpeta origen de todo
## Archivos
**Son los tipos de procesos que podemos hacer en los archivos**

touch nombre.txt: el creador, crea el archivo nuevo con el nombre y el formato que le acompana y si ya existe solo modificara la fecha de modificacion sin borrar el contenido
cat nombre.txt: muestra el contenido del archivo en la terminal en el caso del ejemplo nombre.txt, es la forma de leer el texto y configuraciones sin salir de la terminal
echo "texto" >archivo.txt - echo es para escribir, el > sobreescribe todo y si tenia contenido el archivo se borra todo por lo que hay ahi 
echo "texto" >> archivo.txt basicamente hace lo mismo que el anterior solo que este agrega la informacion por debajo del archivo no sobreescribe sino que agrega
cp archivo.txt destino/: es el formato copy, copia el archivo a otra ubicacion y el original permanece igual
mv archivo.txt destino/: mueve el archivo a otras carpetas designadas, se usa para renombrar archivos tambien
rm archivo: borra el archivo permanentemente, en la terminal no hay papelera de reciclaje, es final

regla importante: no confundir > con >> ya que la primera reescribe completamente y elimina cualquier informacion previa y la consecunte agrega informacion debajo del texto existente

## grep y filtros
los greps y los filtros nos ayudan a encontras explicitamente lo que buscamos, podemos buscarlo por palabras exactas como EXPORT o formatos unicos con la funcion uniq importante utilizar el "" en cada termino que busquemos

## Permisos
permisos se hablo de rwx read write y excecute, **su numeracion es 4 2 1, donde 7 lo es todo, 4 es solo leer, 2 es solo escribir y 1 es excecute solamente**

la combinacion de los mismos en un total de 3 numeros determina la importancia el primer numero es para mi, el segundo es para el grupo y el tercero es para todos los demas

## Procesos
**Son todas las tareas que hace el computador y cada proceso tiene un ID especifico, esto se conoce como PID process ID**

los comandos

psaux: todo los procesos que esta haciendo la PC: divido en 5 columnas, l primera para el usuario que lo esta corriendo, el segundo el PID, el tercero el porcentage de CPU utilizado, cuarto porcentage de RAM, y el quinto el nombre del proceso

ps aux | grep nombre: filtra los procesos por nombre, excelente para encontrar procesos que estamos buscando directamente sin ir uno por uno

top: monitor en tiempo real, muestra los procesos ordenados como dashboard, hay que presional Q para salir en MacOS

Kill PID: mata el proceso, es como un force quit. detiene el proceso del PID que elija

## Variables de entorno
**las variables son valores importantes que el sistema guarda y pueden ser llamados si se necesita lo mismo una y otra vez.**

las variables del sistema se llaman con el simbolo $

$HOME — la ruta de tu carpeta de usuario
$USER — tu nombre de usuario, en tu caso admin.
$SHELL — el shell que estás usando, en tu Mac es /bin/zsh.
$PATH — la lista de carpetas donde la terminal busca los comandos.

export MI_VARIABLE="valor" — crea una variable disponible en la sesión actual. Si cierras la terminal desaparece.
Para hacerla permanente se agrega al archivo ~/.zshrc que carga cada vez que abres iTerm2.

## macOS específico
**Estos son comandos que solo existen en Mac, no en Linux:**

open . — abre el Finder en la carpeta donde estás parado. El . significa "aquí mismo".
open archivo.txt — abre el archivo con la app por defecto, igual que hacer doble click en el Finder.
open -a "Visual Studio Code" . — abre una app específica. Puedes abrir cualquier app instalada en tu Mac desde la terminal.
pbcopy — copia al portapapeles desde la terminal. Equivale a seleccionar texto y hacer Cmd+C. 
pbpaste — pega el contenido del portapapeles en la terminal. Equivale a Cmd+V.

**En Linux estos comandos no existen. Cuando trabajes en servidores remotos solo tendrás los comandos universales. Pero en tu Mac del día a día te ahorran tiempo.**

## Git — ramas
- git branch: muestra todas las ramas, la verde es donde estás parado
- git checkout -b (nombre): crea una rama nueva y te mueve a ella
- git merge (nombre): fusiona una rama con la rama actual
- git log --oneline: historial compacto de commits
- git diff: muestra exactamente qué líneas cambiaron

## Git - flujo profesional

- Que es una rama y para que sirve: las ramas son basicamente rutas alternas o realidades paralelas de un mismo programa, su funcion es hacer cambios o probar cosas nuevas sin comprometer el codigo fuente o principal que usan los clientes
- git diff, cuando usarlo?: debemos usarlos antes de commiterar cualquier codigo, de esta forma estamos anuentes de cualquier cambio que podamos realizar antes de procesarlo, con diff nos muestra con verde lo que estamos agregando y con rojo lo que estamos borrando
- git stash/ git stash pop: basicamente estos son lineas de codigo que guardamos pero que dejamos en segundo plano, si deseamos que esten nuevamente en el codigo utilizamos el stash pop y reapareceran. 
- Que es un conflicto y como se resuelve?: los conflictos suceden cuando se intenta mezclar documentos y hay una o varias lineas de codigo que estan en las mismas lineas, debido a que estan en la misma zona tenemos un error de conflicto y no podemos mezclarlas automaticamente, sin embargo desde Visual studio code tenemos las opciones de mezclar ambas o desechar alguna de las dos
- Porque se borran las ramas despues del merge? Se borran porque las ramas no estan hechas para permanecer en el sistema sino que sirven para ser exclusivamente temporales si despues del trabajo no se utilizaran las mismas se borran, y en lo personal tambien son buenas en caracter de seguridad para la infraestructura general y evitar errores a futuro
- El flujo completo de trabajo: rama → trabajo → commit → merge → push → borrar rama
- Rama: creamos la rama con el codigo git checkout -b feature/(nombre-del-archivo)
- Trabajo: Serian todos los procesos que estan dentro de esta seccion editar los archivos, crear scripts y demas cambios que se busquen hacer
- Revision: git diff, para tener una representacion grafica de que es lo que realmente cambio
- Commit: git add -A && git commit -m "tipo:descripcion de lo que se hace" son los pasos para tomar la "fotografia" digital del codigo que estamos haciendo al ser validado y mantenerlo de esta forma
- Merge: Regresamos al main con git checkout (nombre-del-inicio-o-main) y fusionamos la rama con git merge (nombre-de-la-rama)
- Push: se suben los cambios a Github para que sea publicamente visibles los cambios
- Borrar la rama: git branch -d (nombre-de-la-rama) esto borra la rama que ha sido creada

## Python para DevOps

- Que es una funcion y para que sirve?: Una funcion puede entenderse como un proceso autonomo que puede ser activado y desactivado a preferencia. asi como tambien activado las veces necesario segun el codigo y su funcionamiento asi como tambien los factores de decision
- Que hace try/except?: Try inicia el proceso, podemos traducirlo como pruebas, dentro del try pueden haber factores condicionales como if, else. en su contra parte el except es eso unico que no vamos a tratar de realizar, o aquello que maneja todo lo que no este dentro de los factores condicionales antes utilizados en el codigo. Ejemplo de esto lo tenemos cuando en el script Consumidor_api.py inicia la funcion try y except, donde try maneja toda la conexion de la API con nuestro programa. sin embargo en los casos donde no recibamos absolutamente nada de la API utilizamos el except, donde maneja el error y nos informa que ha sucedido
- Que es request.get() y para que se usa?: Un request es una herramienta que se utiliza para solicitar informacion a una API externa y nos provee la informacion con datos. informando en los parentesis la URL nos trae la informacion solicitada
- Que es un status code?: Es el estado de nuestra conexion a la URL o API, una coneccion 200 significa que la conexion fue satisfactoria, un connection error significa que no pudimos tener ningun tipo de acceso a la URL, ni siquiera un codigo de error. hubo nulo contacto
- Que hace open() con modo "a" vs modo "w"?: en el modo "a" sirve para agregar al final sin borrar, muy parecido a lo que hace >> en la terminal, "w" rescribe todo por el texto nuevo que se produce, lo mismo que > en una terminal
- Para que sirve el health check antes de consultar una API?: En mi opinion es un paso bastante importante y escencial para comprobar que las bases de nuestro proceso funcionen antes de construir. es como probar los cimientos, el healthcheck nos ayuda a saber que una conexion es exitosa o no. De esta forma podemos tener seguridad de lo que se va a ejecutar va a funcionar y no ser propensos a errores mayores.

## Bash Scripting

- Que es el shebang, y porque va primero? El Shebang en mi opinion es el icono indicativo, la senal de que un programa se maneja en la terminal, tambien una medida de seguridad para evitar confusiones y la breve explicacion por debajo del comando que indica para que es el programa antes de ejecucion
- Que hace $(): lo entiendo como las adiciones automaticas del sistema, que no tengo que proveer manualmente, como la fecha del dia, la hora y demas
- Diferencia entre local y una variable normal: La version local informa que la variable solo se ejecuta en esa seccion y no en ninguna otra del codigo, diferencia de las que no tienen.
- Que es case y cuando usarlo vs if/elif: case: se utiliza para valores fijos, como por ejemplo una tabla de eleccion. if/elif: cuando son condiciones mas complejas como multiples variables
- while true y como se sale del loop: while true en si es una repeticion continua hasta que se salga del punto incial despues de que termine un programa, para salir se utiliza la tecla indicada, en la mayoria de los casos en bash es 0
- que significa exit 0: es basicamente la salida, el 0 es el indicador universal de finalizacion de programa. 
- Para que sirve: Chmod +x: funciona para dar permisos de ejecucion, es asi en este caso ya que la x en permisos es de ejecutrar, es como decir, te doy permiso (chmod) de ejecutar (+x)

## Proyecto integrador - Semana1

- Que combina el proyecto? El proyecto combina todas las funciones relacionadas en python, el flujo de conectividad, menu interactivo, y generador de reporte HTML donde ayuda a aprender un poco mas e incursionar en diferentes formas de trabajo. 
- Que fue lo mas dificil de construirlo solo?: Mas que nada lo complicado es el recordad los terminos de programacion, tomo mas del tiempo esperado el recordar y documentar todo lo que necesitaba, aunque esto es algo normal. en mi opinion la programacion es mas de "Saber donde encontrar" que "Esforzarnos en recordar"
- Que aprendi sobre como python genera HTML desde un script?: Fue algo bastante inesperado, sin embargo es conocido que python es uno de los lenguajes de programacion mas versatiles y potentes, lo que lo hace una excelente herramienta de desarrollo actual y futuro.
