from django.urls import reverse
import pandas as pd
from sklearn.pipeline import Pipeline
from tensorflow.python.keras.models import load_model, model_from_json
from keras import backend as K
from practicaDespliegue.logica import modeloRF
import pickle
import keras
import zipfile

class ModeloRF():
    """Clase modelo Preprocesamiento y RF"""

    #Función para cargar preprocesador y el modelo de Random Forest
    def cargarPipeline(self,nombreArchivoPipeline):
        with open(nombreArchivoPipeline+'.pickle', 'rb') as handle:
            pipeline = pickle.load(handle)
        return pipeline

    def predecirIntencionCompra(self, ProductRelated = 1, ProductRelated_Duration = 0.000000, BounceRates = 0.20, ExitRates = 0.20, PageValues = 0.0, Month = 'Feb', Region = 1, VisitorType = 'Returning_Visitor', Weekend = 0):  
        
        nombreArchivoPipeline = "Recursos/pipePreprocesadores"
        pipe=self.cargarPipeline(self, nombreArchivoPipeline)

        archivo_zip = 'Recursos/modeloRF.zip'
        destino = 'Recursos/'

        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            zip_ref.extractall(destino)

        nombreArchivoRF = "Recursos/modeloRF"
        modeloRF2=self.cargarPipeline(self, nombreArchivoRF)

        cnames=['ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues', 'Month', 'Region', 'VisitorType', 'Weekend']
        Xnew=[ProductRelated, ProductRelated_Duration, BounceRates, ExitRates, PageValues, Month, Region, VisitorType, Weekend]
        
        categorical_nominal_features = ['Month', 'Region', 'VisitorType', 'Weekend']
        numeric_features = ['ProductoRelated','ProductoRelated_duration','BounceRates', 'ExitRates', 'PageValues']

        Xnew_Dataframe = pd.DataFrame(data=[Xnew],columns=cnames)

        Xnew_Dataframe_Transformado = pipe.transform(Xnew_Dataframe)
        
        cnamesDataset1=[]
        cnamesDataset2 = pipe.named_steps['prepcn'].transformers_[0][1].named_steps['onehot'].get_feature_names_out(categorical_nominal_features)       
        cnamesDataset3 = numeric_features
        cnamesDataset1.extend(cnamesDataset3)
        cnamesDataset1.extend(cnamesDataset2)

        dataframeTransformado = pd.DataFrame(data=Xnew_Dataframe_Transformado,columns=cnamesDataset1)

        y_pred = modeloRF2.predict(dataframeTransformado)

        pred = y_pred.flatten()[0]# de 2D a 

        if pred == 1:
            #pred='El usuario realizara una compra'
            pred = 1
        else:
            #pred='El usuario no realizara una compra'
            pred = 0
        
        return pred
    
#target (Posee enfermedad cardiaca:1, No posee enfermedad cardiaca:0)


#resul=modeloSNN.modeloSNN.predecirNuevoCliente(modeloSNN.modeloSNN,PLAZOMESESCREDITO=PLAZOMESESCREDITO,MONTOCREDITO=MONTOCREDITO,TASAPAGO=TASAPAGO,EDAD=EDAD,CANTIDADPERSONASAMANTENER=CANTIDADPERSONASAMANTENER,EMPLEO=EMPLEO)
