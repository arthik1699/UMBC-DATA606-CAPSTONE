import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle 
import random
from joblib import load



st.image("https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/app/car1.png",width=600, use_column_width='always')
st.markdown("<h2 style='text-align:center;'>Used Cars Price Predicton</h2>",unsafe_allow_html=True)
   

st.sidebar.write("# Created by Arthi Komma")

def random_enumeration(categories):
    unique_categories = sorted(set(categories))
    enumeration = {category: idx for idx, category in enumerate(random.sample(unique_categories, len(unique_categories)))}
    return enumeration



def UserInputs():
    
    
    
    make = st.selectbox("Make",['toyota', 'ford', 'dodge', 'chevrolet', 'gmc', 'chrysler', 'kia',
       'buick', 'infiniti', 'mercedes-benz', 'jeep', 'bmw', 'cadillac',
       'hyundai', 'mazda', 'honda', 'heartland', 'jaguar', 'acura',
       'harley-davidson', 'audi', 'lincoln', 'lexus', 'nissan', 'land',
       'maserati', 'peterbilt', 'ram'])
    model = st.text_input("Model")
    year = st.number_input("Year", min_value=2010, max_value=2020)
    title_status = st.selectbox("title_status",['clean vehicle', 'salvage vehicle'])
    mileage = st.number_input("Mileage")
    color = st.text_input("Color")
    
    state = st.selectbox("State",['new jersey', 'tennessee', 'georgia', 'virginia', 'florida',
       'texas', 'california', 'north carolina', 'ohio', 'new york',
       'pennsylvania', 'south carolina', 'michigan', 'washington',
       'arizona', 'utah', 'kentucky', 'massachusetts', 'nebraska',
       'ontario', 'missouri', 'minnesota', 'oklahoma', 'connecticut',
       'indiana', 'arkansas', 'kansas', 'wyoming', 'colorado', 'illinois',
       'wisconsin', 'mississippi', 'maryland', 'oregon', 'west virginia',
       'nevada', 'rhode island', 'louisiana', 'alabama', 'new mexico',
       'idaho', 'new hampshire', 'montana', 'vermont'])
    country = st.selectbox("Country",['USA','Canada'])
    
    data = {'make': make,
            'model': model,
            'year': year,
            'title_status': title_status,
            'mileage': mileage,
            'color': color,
            'state': state,
            'country': country
            
            }
    
    
    # Randomly enumerate categorical variables
    make_enum = random_enumeration([make])
    model_enum = random_enumeration([model])
    title_status_enum = random_enumeration([title_status])
    color_enum = random_enumeration([color])
    state_enum = random_enumeration([state])
    country_enum = random_enumeration([country])
    

    # Apply enumeration
    df = pd.DataFrame(data, index = [0])
    df['make'] = df['make'].apply(lambda x: make_enum[x])
    df['model'] = df['model'].apply(lambda x: model_enum[x])
    df['title_status'] = df['title_status'].apply(lambda x: title_status_enum[x])
    df['color'] = df['color'].apply(lambda x: color_enum[x])
    df['state'] = df['state'].apply(lambda x: state_enum[x])
    df['country'] = df['country'].apply(lambda x: country_enum[x])
    

    return df
    

def main():
    
    df1 = UserInputs()
    
    

    ## Data Transformation
    df = pd.read_csv("https://github.com/arthik1699/UMBC-DATA606-CAPSTONE/blob/main/app/USA_cars_datasets.csv")
    df = df.drop(['Unnamed: 0','vin','lot','condition'], axis = 1)
    

    categorical_features=[feature for feature in df.columns if df[feature].dtype=='O']

    numerical_features=[feature for feature in df.columns if df[feature].dtype!='O']

    X=df.drop('price',axis=1)
    y=df['price']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)


    train_set=pd.concat([X_train,y_train],axis=1)
    test_set=pd.concat([X_test,y_test],axis=1)

    for feature in categorical_features:
        feature_labels = train_set.groupby(feature)['price'].mean().sort_values().index
        feature_labels = {k:i for i,k in enumerate(feature_labels,0)}
        train_set[feature] = train_set[feature].map(feature_labels)
        test_set[feature] = test_set[feature].map(feature_labels)

    test_set.dropna(inplace = True)
    # Standardize the features
    scaler = StandardScaler()

    scaled_X_train = pd.DataFrame(scaler.fit_transform(train_set.drop('price',axis=1)), columns=X_train.columns)
    scaled_X_train.index = train_set.index
    scaled_X_test = pd.DataFrame(scaler.transform(test_set.drop('price',axis=1)), columns=X_test.columns)
    scaled_X_test.index = test_set.index
    scaled_train = pd.concat([scaled_X_train,train_set['price']],axis=1)
    scaled_test = pd.concat([scaled_X_test,test_set['price']],axis=1)
    X_train = scaled_train.drop('price',axis=1) 
    y_train = scaled_train['price']
    X_test = scaled_test.drop('price',axis=1)
    y_test = scaled_test['price']
    

    # Train the model
    rf = RandomForestRegressor(max_depth=50, random_state=1)
    rf.fit(X_train, y_train)


    result = rf.predict(df1)
    re = int(result[0])
    button_clicked = st.button("Predict")
    st.markdown("<h5 style='text-align:center;'>Price of Car for given Specifications:</h5>",unsafe_allow_html=True)


    if button_clicked:
        
        re = int(result[0])
        # Display the result
        st.write("<h5 style='text-align:center; color:Tomato'>$"+str(re)+"</h5>", unsafe_allow_html=True)


if __name__=='__main__': 
    main()
