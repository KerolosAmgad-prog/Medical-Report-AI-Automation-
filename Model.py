import pandas as pd                                 # it use for reading a big dataframe
#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_absolute_error


#/////////////////////////////////////////Function of the reading data/////////////////////////////
def load_data (filepath):
    data=pd.read_csv(filepath)
    data["gender"]=(data["gender"]=="male").astype(int)
    return data

#///////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////Function of spliting the data//////////////////////////////////
def preprocess_data(data):
    x=data.drop(columns=['post_bp','post_temp','blood_flow_rate'])
    y_bp=data["post_bp"]
    y_temp = data["post_temp"]
    y_flow=data["blood_flow_rate"]
    #test_size =0.2, training data =80% ,test data =20%
    #random state is make random data by 42 percent for testing and training
    return train_test_split (x,y_bp,y_temp,y_flow,test_size=0.2,random_state=42)
#/////////////////////////////////////////////////////////////////////////////////////////////////


#//////////////////////////////////Function of tranining the data ///////////////////////////////

def train_models(x_tran,y_bp_train,y_temp_train,y_flow_train):

    #the training of the  post blood pressure :
    bp_model=RandomForestRegressor(n_estimators=100,random_state=42)
    bp_model.fit(x_tran,y_bp_train)

    #the training of the post temperature :
    temp_model=RandomForestRegressor(n_estimators=100,random_state=42)
    temp_model.fit(x_tran,y_temp_train)

    #the training of the flow rate :
    flow_model=RandomForestRegressor(n_estimators=100,random_state=42)
    flow_model.fit(x_tran,y_flow_train)

    return bp_model,temp_model,flow_model

#///////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////Function of predict of blood pressure and temperature/////////
def predict(bp_model,temp_model,flow_model,x_test):
    # adding to it (x_test )
    bp_pred=bp_model.predict(x_test)
    temp_pred=temp_model.predict(x_test)
    flow_pred = flow_model.predict(x_test)
    return bp_pred,temp_pred,flow_pred
#///////////////////////////////////////////////////////////////////////////////////////////////

