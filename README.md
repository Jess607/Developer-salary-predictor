# Developer-salary-predictor
This is a flask web application that predicts developer salaries containerized using docker and deployed on AWS Elastic beanstalk.


# Table Of Contents
* [Installation](https://github.com/Jess607/Exploratory-Data-Analysis-of-IT-employees-in-Europe#installation)
* [About the Project](https://github.com/Jess607/Exploratory-Data-Analysis-of-IT-employees-in-Europe#about-the-project)
* [Data Gathering](https://github.com/Jess607/Exploratory-Data-Analysis-of-IT-employees-in-Europe#data-gathering)
* [File Description](https://github.com/Jess607/Exploratory-Data-Analysis-of-IT-employees-in-Europe#file-description)
* [Technologies Used](https://github.com/Jess607/Exploratory-Data-Analysis-of-IT-employees-in-Europe#file-description)
* [Limitations](https://github.com/Jess607/Exploratory-Data-Analysis-of-IT-employees-in-Europe#limitations)

# Installation 
The code requires python versions of 3.10 as well as other python packages. To install libraries use 
`pip install -r requirements.txt`


# About The Project 
In my previous job as a human capital analyst in a recruiting firm, I often encountered talents who were not quite sure of their salary expectations when considering new roles. I wondered if it were possible to create a model that predicted what a developer would earn based on some personal info and their tech stack. 
This motivated and birthed this project. `Stackoverflow yearly survey data` for 2021 was utilized to create the model. A deep learning model was built using `Tensorflow keras`, packaged using a `flask REST API` alongside an accompanying frontend built using `HTML/CSS` and `Bootstrap`. The code was containerized using `docker` in order to create a microservice application that ran regardless of environment and then deployed on `AWS Elasticbeanstalk`, AWS' PAAS option for easy deployment of code.

# Data Gathering 
Data utilized was gotten from Stackoverflow's yearly developer survey for the year 2021. It comes alongside a schema. All of which are available in the `data` folder in the project directory.

# File Description 
The 

# Limitations 
* The greatest limitation to the EDA process was that the sample data gathered was not sufficiently representative of the population being studied. Thus, full inferential results could not be drawn for certain cities in Europe unli