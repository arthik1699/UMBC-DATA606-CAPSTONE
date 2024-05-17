# 1. PROJECT TITLE - USED CARS PRICE PREDICTION [ARTHI KOMMA - SPRING 2024]
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - SPRING 2024 Semester
- Author: Arthi Komma
- GitHub : https://github.com/arthik1699
- Linkedin : www.linkedin.com/in/arthi-komma-07874b1b9
- Presentation : https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/USED%20CARS%20PRICE%20PREDICTION.pptx
- Youtube Video : https://youtu.be/98DgP2k8yoE


## 2. BACKGROUND
  - Building a used car price prediction project involves leveraging machine learning techniques to analyze various factors that influence the pricing of used cars.The project can be useful in several ways, benefiting various stakeholders in the automotive industry, consumers, and related sectors.
  - Research Questions:
    - How accurately can machine learning models predict the prices of used cars based on various features such as make, model, mileage, and year of manufacture?
    - Which features contribute the most to the prediction of used car prices, and how does their importance vary across different car models and makes?
    - What recommendations can be made based on the model's outputs?



## 3. DATA
Description : 

1. Data Source : *[Kaggle](https://www.kaggle.com/datasets/doaaalsenani/usa-cers-dataset)*. :link:

2. Data Size : 277 KB

3. Data Shape
   > - Number of columns =  13
   > - Number of rows    = 2499

4. What does dataset represent - This dataset included Information about 28 brands of clean and used vehicles for sale in US. Twelve features were assembled for each car in the dataset.

5. Target Variable: Price(Integer)

6. Data dictionary:
   
| Feature          | Type            | Description                                                                                              |
|------------------|-----------------|----------------------------------------------------------------------------------------------------------|
| Price            |Integer          | The sale price of the vehicle in the ad                                                                  |
| Year             | Integer         | The vehicle registration year                                                                            |
| Make             | String          | The brand of the car                                                                                     |
| Model            | String          | The model of the vehicle                                                                                 |
| Colour           | String          | The colour of the vehcile                                                                                |
| State/City       | String          | The location in which the car is being available for purchase                                            |
| Mileage          | Float           | Miles travelled by the vehcile                                                                           |
| Vin              | String          | The vehicle identification number is a collection of 17 characters (digits and capital letters)          |
| Title Status     | String          | This feature included binary classification, which are clean title vehicles and salvage insurance        |
| Lot              | Integer         | A lot number is an identification number assigned to a particular quantity                               |
| Condition        | String          | Time                                                                                                     |

## 4. METHODOLOGY

The below methodology has been used to build the Used Cars Price Prediction project.
 ![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/pic1.png)
 
## 5. DATA VISUALIZATIONS
#### 5.1 Value Counts of the Year column
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv1.png)
#### 5.2 Value Counts of the Colors column
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv2.png)
#### 5.3 Value counts of the Make column
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv3.png)
#### 5.4 Distribution of the Countries
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv4.png)
#### 5.5 Value Counts of States
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv5.png)
#### 5.6 Value counts of Models
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv6.png)
#### 5.7 Distribution of Last 5 Years Production Rate
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv7.png)
- It is observed that 2019 has seen twice the production sales of cars when comapred to 2018. 2018 and 2017 almost had same rate of production of cars
#### 5.8 Distribution of Top brands by years
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv8.png)
- Ford has the leading sales numbers compared to its competitors. In 2018, Ford and Nissan almost had same number of models rolling out.
#### 5.9 Distribution of Price range of various models of the cars
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv9.png)
#### 5.10 Correlation matrix
![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/dv10.png)



## 6. MODEL BUILDING

- The dataset's price column serves as the target variable for constructing models. The remaining columns, including brand, model, manufacturing year, mileage, color, state, and country, are utilized to forecast the price of the car.
- Utilizing machine learning algorithms, we can develop predictive models to estimate the price of the Used cars considering various factors like brand, model, manufactured year etc. 
- Data preprocessing plays a crucial role in machine learning workflows, ensuring data compatibility with models. Standardization and Scaling is applied to numerical features, while encoding techniques handle categorical features.
- The dataset is divided into training and testing sets using the train_test_split method. The model is then trained on the training data using the fit method. Predictions are made on the testing data using the predict method. Finally, evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared are calculated.

- The Models used in the project are:
  - **Linear Regression Model** :  The linear regression model utilizes a linear relationship between independent variables and the target variable to make predictions. The accuracy of the model was found to be 57%.
  - **Random Forest Regression Model** : The random forest regression model utilizes an ensemble of decision trees to predict the target variable. The accuracy of the model was found to  be 75%.
  - **XGBoost Regression Model** : The XGBoost regression model utilizes an ensemble of decision trees in a gradient boosting framework to predict the target variable. The accuracy of the model was found to be 73%.

## 7. DEPLOYMENT USING STREAMLIT

Streamlit is an open-source Python library that enables you to create interactive web applications for machine learning, data science, and other tasks with minimal effort. It simplifies the process of building data-driven web apps by allowing you to write Python scripts that automatically transform into interactive web applications.

![image](https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/output.png)

## 8. CONCLUSION

In conclusion, the used car price prediction project leverages machine learning techniques to forecast the price of pre-owned vehicles based on various factors such as make, model, year, mileage, color, location, and title status. By collecting and analyzing historical data on used car sales, we can train machine learning models to recognize patterns and relationships within the data, enabling them to make accurate predictions on unseen instances.

Throughout the project, I utilized a variety of regression techniques such as Linear Regression, Random Forest Regression, XGBoost Regression, K-Neighbors Regression to model the relationship between input features and the target variable (i.e., the price of the used car). After training our models using a labeled dataset, we evaluated their performance using metrics such as Mean Squared Error (MSE), R-squared (R2), and Root Mean Squared Error (RMSE) to ensure their reliability and accuracy.
To facilitate user interaction and enhance accessibility, we deployed our prediction model using Streamlit, a powerful Python library for building interactive web applications. Streamlit allowed us to create an intuitive and user-friendly interface where users can input details about the car they are interested in, and receive instant predictions on its price based on our trained machine learning models.

In summary, the used car price prediction project demonstrates the practical application of machine learning in the automotive industry, providing valuable insights for both buyers and sellers in making informed decisions about used car transactions. Additionally, the integration of Streamlit enables seamless deployment and accessibility of the prediction model, further enhancing its utility and usability for a wide range of users.


