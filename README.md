# customer_segmentation_analysis_using_kmeans_and_implementation_using_streamlit

PROBLEM STATEMENT:

To develop a web application using streamlit for customer segmentation analysis using kmeans algorithm.

Customer segmentation is grouping customers based on characteristics such as age, annual income, spending score.
It helps the organization to understand the customer, knowing the difference between the customer groups help them to make strategic decision regarding product growth and marketing.
The oppurtunities of customer segmentation are endless, it totally depends upon the customerdata that we use.

In this project we are using mallcustomer.csv dataset which is available in kaggle.
In this dataset we can see every features are independent of each other. we don't know what to predict. this dataset is a perfect example for unsupervised learning.

Our aim is to group certain customers into a specific category, such that these group shares a common behaviour that helps us to make some plan of action.
For achieving this we are using kmeans algorithm, so that at the end we will create a dependent variable with finite number of values which refers to the classes/group were each customer belongs.

PROJECT IMPLEMENTATION:

Step 1: Import necessary libraries 

For our project we need pandas,numpy for data analization and seaborn, matplotlib for data visualization.

Step 2: Load the dataset and view the properties, characteristics of the dataset. Create a dataset that contains the values of required features.

Step 3: From sklearn library import cluster and create an empty list for storing the values for wcss(within cluster sum of squares).

Step 4: To determine the optimal number of clusters we are using elbow method. Elbow method is a plot between no:of clusters and wcss. The goal is to find the point at which increasing the number of clusters doesn't significantly reduce WCSS anymore, and this point is often referred to as the "elbow." With the help of kmeans algorithm we find the values for k and wcss and based on these value plot the elbow graph.

Step 5:Once the value for the cluster is fixed, we will predict the values for y which denotes in which class each customer belongs.
This step is accomplished with the help of kmeans algorithm.

Step 6: Plot the clusters which shows were each customer belongs along with their centroids.

Step 7: Test the model with required feature values and find the cluster where it belongs.

Step 8: Save the model using joblib library.

Step 9: Open a .py file to deploy the model as a web application. Here we are using streamlit library. Add some code to develop features to your website like title, input button and output button to predict.

Step 10: Run .py file in your prompt to view the website to perform the customer segmentation analysis.





