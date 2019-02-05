"""
.. module:: Arithmetic

Arithmetic
*************

:Description: Arithmetic

 Evalua la expresion aritmetica de un string

:Authors: bejar
    

:Version: 

:Created on: 06/02/2018 8:21 

"""

import socket
import argparse
from FlaskServer import shutdown_server
import requests
from flask import Flask, request
from requests import ConnectionError
from multiprocessing import Process

__author__ = 'bejar'

app = Flask(__name__)

problems = {}
probcounter = 0


@app.route("/message")
def message():
    """
    Entrypoint para todas las comunicaciones

    :return:
    """
    mess = request.args['message']

    if '|' not in mess:
        return 'ERROR: INVALID MESSAGE'
    else:
        # Sintaxis de los mensajes "TIPO|PARAMETROS"
        messtype, messparam = mess.split('|')

        if messtype not in ['SOLVE']:
            return 'ERROR: INVALID REQUEST'
        else:
            # parametros mensaje SOLVE = "SOLVERADDRESS,PROBID,PROB"
            if messtype == 'SOLVE':
                param = messparam.split(',')
                print(param)
                if len(param) == 3:
                    solveraddress, probid, prob = param
                    p1 = Process(target=solver, args=(solveraddress, probid, prob))
                    p1.start()
                    return 'OK'
                else:
                    return 'ERROR: WRONG PARAMETERS'


@app.route("/stop")
def stop():
    """
    Entrada que para el agente
    """
    shutdown_server()
    return "Parando Servidor"


def solver(saddress, probid, prob):
    """
    Hace la resolucion de un problema

    :param param:
    :return:
    """
    try:
        res = eval(prob)
    except Exception:
        res = 'ERROR: SYNTAX ERROR'

    requests.get(saddress + '/message', params={'message': f'SOLVED|{probid},{res}'})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--open', help="Define si el servidor esta abierto al exterior o no", action='store_true',
                        default=True)
    parser.add_argument('--port', type=int, help="Puerto de comunicacion del agente")
    parser.add_argument('--dir', default=None, help="Direccion del servicio de directorio")

    # parsing de los parametros de la linea de comandos
    args = parser.parse_args()

    # Configuration stuff
    if args.port is None:
        port = 9020
    else:
        port = args.port

    if args.open:
        hostname = '0.0.0.0'
    else:
        hostname = socket.gethostname()

    if args.dir is None:
        raise NameError('A Directory Service addess is needed')
    else:
        diraddress = args.dir

    # Registramos el solver aritmetico en el servicio de directorio
    solveradd = f'http://{socket.gethostname()}:{port}'
    solverid = socket.gethostname().split('.')[0] + '-' + str(port)
    mess = f'REGISTER|{solverid},ARITH,{solveradd}'

    done = False
    while not done:
        try:
            resp = requests.get(diraddress + '/message', params={'message': mess}).text
            done = True
        except ConnectionError:
            pass

    if 'OK' in resp:
        print(f'ARITH {solverid} successfully registered')
        # Ponemos en marcha el servidor Flask
        app.run(host=hostname, port=port, debug=True, use_reloader=False)

        mess = f'UNREGISTER|{solverid}'
        requests.get(diraddress + '/message', params={'message': mess})
