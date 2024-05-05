# 1. PROJECT TITLE - USED CARS PRICE PREDICTION
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - SPRING 2024 Semester
- Author: Arthi Komma
- GitHub : https://github.com/arthik1699
- Linkedin : www.linkedin.com/in/arthi-komma-07874b1b9
- Presentation : https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/docs/USED%20CARS%20PRICE%20PREDICTION.pptx


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
| Years            | Integer         | The vehicle registration year                                                                            |
| Brand            | String          | The brand of the car                                                                                     |
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
