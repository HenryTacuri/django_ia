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
    def predecirIOJson():


        ProductRelated = 1
        ProductRelated_Duration =0.000000
        BounceRates = 0.20
        ExitRates = 0.20
        PageValues = 0.0
        Month = "Feb"
        Region = 0
        VisitorType = "Returning_Visitor"
        Weekend = 9

        modeloRF

        resul=modeloRF.ModeloRF.predecirIntencionCompra(modeloRF.ModeloRF, ProductRelated=ProductRelated, ProductRelated_Duration=ProductRelated_Duration, BounceRates=BounceRates, ExitRates=ExitRates, PageValues=PageValues, Month=Month, Region=Region, VisitorType=VisitorType, Weekend=Weekend)  

        data = {'result': resul}
        resp=JsonResponse(data)
        resp['Access-Control-Allow-Origin'] = '*'

        return resp
    
