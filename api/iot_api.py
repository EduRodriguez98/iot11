from flask import Blueprint, request, jsonify

from services.main_service import MainService
from services.sensores import Sensores

iotApi = Blueprint('iotApi', __name__)

my_main_service = MainService()
my_sensores = Sensores()


# call para ejecutar
@iotApi.route('execute', methods=['GET'])
def execute():
    if request.is_json:
        my_main_service.main(request.json)
        return jsonify(message='ok'), 200


# call para detener 'execute'
@iotApi.route('ender', methods=['GET'])
def ender():
    my_main_service.ender()
    return jsonify(message='ender done'), 200


# call API para recibir informacion de distancia
@iotApi.route('distance', methods=['GET'])
def distance():
    conf_cerca = None
    conf_lejos = None
    response = my_sensores.distance(conf_cerca=conf_cerca, conf_lejos=conf_lejos)
    return jsonify(response), 200


# call API para recibir informacion de temperatura y humedad
@iotApi.route('temp-and-humi', methods=['GET'])
def temp_and_humi():
    conf_temp = None
    conf_humi = None
    response = my_sensores.temp_and_humi(conf_temp=conf_temp, conf_humi=conf_humi)
    return jsonify(response), 200


# call API para recibir informacion de luz
@iotApi.route('light', methods=['GET'])
def light():
    conf_luz = None
    response = my_sensores.light(conf_luz=conf_luz)
    return jsonify(response), 200
