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

The **Dockerfile** starts with the Ubuntu 20.04 base image. The MAINTAINER command sets the author information for the image. 
- Then, the RUN command is used to update the package list on the Ubuntu image. 
- The COPY command is used to copy the content of the current directory to the /opt/gsom_predictor directory inside the Docker container. 
- The WORKDIR command sets the working directory inside the container as /opt/gsom_predictor. 
- The next RUN command installs the pip3 package manager for Python 3. 
- The final RUN command installs the dependencies listed in requirements.txt file using pip3. 
- The CMD command runs the app.py file using Python 3 inside the container.
	
<h3> ⚙️ How to open the port in a remote VM </h3>
	
We specify the port in a flask app in the script **app.py** by setting 
```
if __name__ == '__main__':
    app.run(debug = True, port = 5444, host = '0.0.0.0')
```
To open the remote VM port of our web application we need to use these lines:
```
sudo apt install ufw
sudo ufw allow 5444 
```
After that we can use applications such as **Postman** to check how our requests for API work.  

<h3> ⚓ How to run app using docker and which port it uses </h3>

Firstly we need to build containers and then run them: 
```
docker build -t <your login>/<directory name>:<version> .      (example: "docker build -t olgaselesnjova/e2e23:v.0.1 .")
docker run --network host -it <your login>/<directory name>:<version> /bin/bash
docker run --network host -d <your login>/<directory name>:<version>   
docker ps     # to show all running containers and info about them
docker stop <container name>    # from the list after docker ps
```
