from django.shortcuts import render
from practicaDespliegue.logica import modeloRF #para utilizar el método inteligente
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
import pandas as pd 

class Clasificacion():
    
    @csrf_exempt
    @api_view(['GET','POST'])
    def predecirIOJson(request):
        print(request)
        print('***********************************************')
        print(request.body)
        print('***********************************************')
        body = json.loads(request.body.decode('utf-8'))
        #Formato de datos de entrada

        ProductRelated = int(body.get('ProductRelated'))
        ProductRelated_Duration = float(body.get('ProductRelated_Duration'))
        BounceRates = float(body.get('BounceRates'))
        ExitRates = float(body.get('ExitRates'))
        PageValues = float(body.get('PageValues'))
        Month = str(body.get('Month'))
        Region = int(body.get('Region'))
        VisitorType = str(body.get('VisitorType'))
        Weekend = int(body.get('Weekend'))

        modeloRF

        resul=modeloRF.ModeloRF.predecirIntencionCompra(modeloRF.ModeloRF, ProductRelated=ProductRelated, ProductRelated_Duration=ProductRelated_Duration, BounceRates=BounceRates, ExitRates=ExitRates, PageValues=PageValues, Month=Month, Region=Region, VisitorType=VisitorType, Weekend=Weekend)  

        data = {'result': resul}
        resp=JsonResponse(data)
        resp['Access-Control-Allow-Origin'] = '*'

        return resp
    
