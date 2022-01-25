import sys

def main(dict):

    #print(dict.items())
    #print(dict.values())
    #return { "alertas": [ " temperatura " , " humedad " ] }

    def alert_1 (dict.values):

        alert = {}
        valido = True

    while valido:
        if dict.values['co2'] >=500: 
            valido = False
            alert['co2'] = 'co2'
        if dict.values['temperature'] < 22 and  dict.values['temperature'] > 25:
            valido = False
            alert['temperature'] = 'temperature'
        if dict.values['humidity'] < 60 and dict.values['humidity'] > 75:
            valido = False
            alert['humidity'] = 'humidity'
        if dict.values['sound'] < 20 and dict.values['sound'] > 35:
            valido = False
            alert['sound'] = 'sound'
        if dict.values['illumination'] < 100 and dict.values['illumination'] > 200:
            valido = False
            alert['illumination'] = 'illumination'
        return  { "alertas”: alert[]}

alerta1 = alert_1(dict.values)