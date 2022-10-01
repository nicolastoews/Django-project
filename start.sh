#!usr/bin/env bash
#Ejecutar este archivo con . start.sh en terminal para que, en caso de tener un entorno virtual activo, nos lo desactive y active el de este proyecto.

if [ $VIRTUAL_ENVIRONMENT ]
then
    deactivate
fi
. venv/Scripts/activate