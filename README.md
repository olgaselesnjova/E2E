<h2> 🌃 Analyzing Real Estate Data in St. Petersburg </h2>
<h3> 📙 Data source: </h3>

The [dataset](https://github.com/olgaselesnjova/E2E/blob/main/spb.real.estate.archive.sample5000.tsv) is taken from [Yandex.Realty](https://realty.yandex.ru)

**Description of the dataset:**

Real estate listings for apartments in St. Petersburg and Leningrad Oblast from 2016 till the middle of August 2018. 

<h3> ✏️ Used statistics: </h3>

1. Median and mean price for sell and rent houses in St. Petersburg.
2. Removed outliers: too cheap or too expensive apartments which seem to be a wrong data. 
3. The most cheapest and most expensive prices per square meter.
4. How many rent offers have the commission and what is the most popular commission.

🔍 File [EDA_real_estate_data.ipynb](https://github.com/olgaselesnjova/E2E/blob/main/EDA_real_estate_data.ipynb) contains the EDA of the dataset.

<h3> Some ot the vizes: </h3>

![alt text](https://github.com/olgaselesnjova/E2E/blob/main/images/1.JPG)
![alt text](https://github.com/olgaselesnjova/E2E/blob/main/images/2.JPG)
![alt text](https://github.com/olgaselesnjova/E2E/blob/main/images/3.JPG)

<h3> ✏️ Data prepsocessing </h3>
For data preprocessing we used **SimpleImputer** with a default strategy "mean" in scikit-learn to replace missing values in a numerical dataset by the mean value of the corresponding column.
**OneHotEncoder** is used to convert categorical variables into a format that can be used by ML algorithms.

```
mapper = DataFrameMapper([([feature], SimpleImputer()) for feature in numeric_features] +\
                         [([feature], OneHotEncoder(handle_unknown = 'ignore')) for feature in nominal_features], 
                            df_out=True)  
```		

<h3> 📍 ML </h3>
I automated the data processing and model building process by using **pipeline** to increase the efficiency, accuracy and reproducibility of models.

```
xgboost_pipeline = Pipeline(steps = [('preprocessing', mapper), 
                             ('scaler', StandardScaler()),
                             ('xgb', xgb.XGBRegressor(objective="reg:linear", random_state=42))])
```			     
I tried several simple models and here are the results: 

- Model Results (Accuracy - from best to worst): 
    - XGBRegressor = 63.65%
    - CatBoostRegressor = 62.23%
    - DecisionTreeClassifier = 9.92% - without tunning, just a model
    - CatBoostClassifier = takes to long to load
    - RandomForestClassifier = the kernel died

The best result provides **XGBRegressor** with hyperparameters:

```
param_grid = dict(xgb__learning_rate = [0.1], xgb__n_estimators = [100], xgb__max_depth = [5])
xgboost = GridSearchCV(estimator=xgboost_pipeline, param_grid=param_grid, cv=3, n_jobs=2, verbose=2)
```
 
<h3> 💻 How to install instructions and run the web-app with virtual environment </h3>
	
<h3> 📎 Information about Dockerfile </h3>
describe it's content
	
<h3> ⚙️ How to open the port in a remote VM </h3>
	
<h3> ⚓ How to run app using docker and which port it uses </h3>
