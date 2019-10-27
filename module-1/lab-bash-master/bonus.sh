#!/bin/bash
#Acá el código - se debe ejecutar en la ruta: /lab-bash-master:
echo --------------------------------
echo 'Este es el bonus del ejercicio'
name='Hecho por Juan Munoz:'
echo $name
cd lorem/

for i in $( ls ); do
	echo $i
	echo 'characthers length:'
	echo -n $i | wc -c
	echo '----Next File:'
done

#bonus de Pedro
echo ----------------------------------
echo 'Acá empieza el ejercicio de Pedro'
echo 'A continuación el listado de archivos que contienen .py en la libreria:'
cd ..
cd house.py/
#ls | grep -i *.py
#find . | grep -i .py

for j in $(find . | grep -i .py ); do
	echo $j
	echo $( wc -l $j )
done
