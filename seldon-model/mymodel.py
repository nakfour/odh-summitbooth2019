import boto3
import botocore
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import json


class mymodel(object):
 
    def __init__(self):
        print("Initializing")
        # Create an S3 client
        s3 = boto3.client(service_name='s3',aws_access_key_id='foo', aws_secret_access_key='bar', endpoint_url='http://ceph:8000')
        key = "uploaded/model.pkl"
        try:
        	print("Trying to download model")
        	s3.download_file(Bucket='MODEL', Key=key, Filename="model.pkl")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

        # Replace with path of trained model
        print("Loading model to seldon")
        model_path = 'model.pkl'
        #self.model = load_model(model_path)
        self.clf = joblib.load(model_path) 
        print("Model uploaded to class")
        #self.model = 'None'
 
    def predict(self,x,features_names):
        print("HERERERERERERERERERERERERE")
        print(x)
        print(type(x))
        result = "PASS"
        featurearray=[float(i) for i in x.split(',')]
        print(featurearray)
        rowdf = pd.DataFrame([featurearray], columns = ['Time','V1','V2','V3','V4', 'V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'])
        print(rowdf)
        predictions = self.clf.predict(rowdf)
        #predictions = self.clf.predict_proba()
        # initialize list of lists
        return predictions
