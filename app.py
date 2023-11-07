import pandas as pd
import numpy as np
import joblib
import streamlit as st
model = joblib.load("customer_segmentation_kmeans_model")

## defining a function to make predictions
def predict(input_data):

    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    result = model.predict(input_data_reshaped)
    #print("This Customer belongs to cluster no: ", result[0])
    prediction =result[0]
    print("This customer belongs to cluster ", prediction)

    if prediction == 0:
        return "Customers with medium annual income and medium annual spend"
    elif prediction==1:
        return "Customers with high annual income but high annual spend"
    elif prediction==2:
       return "Customers with low annual income and high annual spend"
    elif result[0]==3:
        return "Customers low annual income and low annual spend"
    elif result[0]==4:
        return "Customers with high annual income but low annual spend"

def main():
        ## adding some information about the app's functioning to the sidebar
        st.sidebar.info('This app is created to segment customer based on their behavior')

        ## adding the title for the streamlit app
        st.title("Customer Segmentation Prediction App")

        ## adding a number input box to get Annual income value
        p1 = st.number_input('Annual Income')

        ## adding a number input box to get spending score value
        p2 = st.number_input('SpendingScore')

        #code for prediction
        result = ' '

        #creating a button for prediction
        if st.button("predict"):
            result = predict([p1,p2])

        st.success(result)

if __name__ == '__main__':
  main()



