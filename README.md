# Bienvenido al proyecto EduCoin

**EduCoin** es una cadena de bloques basica que sirve como prueba de concepto

## Ejecutar la cadena de bloques

Este proyecto esta divido en 3 aplicaciones:

- src/client: permite generar e introducir en la cadena de bloques
- src/node: software que controla la cadena de bloques, debe ejecutarse en cada nodo de la red
- src/network: directorio con las direcciones de todos los nodos registrados en la red

lo primero que tienes que hacer es ejecutar la aplicacion de nodos, debes entrar en el
folder src/nodes y ejecutar el archivo index.py pasando como parametro el puerto que
utilizará para recibir peticiones.

`python index.py -p 5001`

una vez que por lo menos un nodo este corriendo podemos utilizar el cliente en src/client para acceder a la cadena de bloques, lo primero que debemos hacer es crear una billetera.

`python main.py --wallet`

esto generara tu direccion y tu llave privada, debes almacenarlas para poder realizar
transacciones.

![wallet](assets/wallet.png)
