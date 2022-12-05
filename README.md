# Developer-salary-predictor
This is a flask web application that predicts developer salaries containerized using docker and deployed on AWS Elastic beanstalk.


# Table Of Contents
* [Installation](https://github.com/Jess607/Developer-salary-predictor#installation)
* [About the Project](https://github.com/Jess607/Developer-salary-predictor#about-the-project)
* [Data Gathering](https://github.com/Jess607/Developer-salary-predictor#data-gathering)
* [File Description](https://github.com/Jess607/Developer-salary-predictor#file-description)
* [Limitations](https://github.com/Jess607/Developer-salary-predictor#limitations)

# Installation 
The code requires python versions of 3.10 as well as other python packages. To install libraries use 
`pip install -r requirements.txt`


# About The Project 
In my previous job as a human capital analyst in a recruiting firm, I often encountered talents who were not quite sure of their salary expectations when considering new roles. I wondered if it were possible to create a model that predicted what a developer would earn based on some personal info and their tech stack. 
This motivated and birthed this project. `Stackoverflow yearly survey data` for 2021 was utilized to create the model. A deep learning model was built using `Tensorflow keras`, packaged using a `flask REST API` alongside an accompanying frontend built using `HTML/CSS` and `Bootstrap`. The code was containerized using `docker` in order to create a microservice application that ran regardless of environment and then deployed on `AWS Elasticbeanstalk`, AWS' PAAS option for easy deployment of code.

# Data Gathering 
Data utilized was gotten from Stackoverflow's yearly developer survey for the year 2021. It comes alongside a schema. All of which are available in the `data` folder in the project directory.

# File Description 
The project contains:
* a `data` folder that holds the data files used for the exploratory data analysis and model building 
* a `model_building` folder that contains three files; an `EDA.ipynb` file where EDA was carried out, a `model.ipynb` file where feature selection, engineering and model building was carried out and a `variables.py` file where feature options were stored
* an `app.py` file where the flask app was built 
* a `templates` folder that hold the html files
* a `static` folder that holds the css files
* a `dockerfile` that holds the docker image used to create the docker container 
* a `model.h5` file which is the saved keras model
* a `preprocessingjoblib` which is a preprocessing pipeline 
* a `requirements.txt` file which holds the requirements used to create the docker image.

# Limitations 
* The greatest limitation to the project was the fact that not all countries could be represented because not all sample collected were a good representation of all countries in the world to be considered for model building. Ultimately, only 
`United States of America`,                               
`India`,                                                    
`Germany`,                                                  
`United Kingdom of Great Britain and Northern Ireland`,   
`Canada`,                                                  
`France`,                                                   
`Brazil`,                                                   
`Poland`,                                                   
`Netherlands`,                                              
`Italy`,                                                    
`Spain`,                                                    
`Russian Federation`,                                       
`Australia` were considered.