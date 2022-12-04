from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

app=Flask(__name__)


def base_model():
    #Instantiating sequential class
    model=tf.keras.models.Sequential()
    #Create layers using 2 hidden layers with the rectified linear activation function and 64 units
    model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    model.add(tf.keras.layers.Dense(units=64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
    model.add(tf.keras.layers.Dense(units=64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
    model.add(tf.keras.layers.Dense(units=1, activation='linear'))
    #Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])
    return model


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods = ["GET", "POST"])

def predict():
    if request.method == "POST":
        #variable for age
        age=request.form['Age']
        #variable for country
        country=request.form['Country']
        #variable for gender
        gender=request.form['Gender']
        #variable for edlevel
        edlevel=request.form['EdLevel']
        #variable for devtype
        devtype=request.form['DevType']
        #variable for orgsize
        orgsize=request.form['OrgSize']
        #variable for employment type
        employment=request.form['Employment']
        #variable for yearscode
        yearscode=request.form['YearsCode']
        #inputs for programming languages
        prog_languages=request.form.getlist('LanguageHaveWorkedWith')
        C=0
        Cplus=0
        Csharp=0
        Dart=0
        Go=0
        BashShell=0
        HTMLCSS=0
        Java=0
        JavaScript=0
        Nodejs=0
        TypeScript=0
        Python=0
        Kotlin=0
        R=0
        SQL=0
        for i in prog_languages:
            if i=='C':
                C=1   
            if i=='C++':
                Cplus=1
            if i=='C#':
                Csharp=1
            if i=='Dart':
                Dart=1
            if i=='Go':
                Go=1
            if i=='Bash/Shell':
                BashShell=1
            if i=='HTML/CSS':
                HTMLCSS=1
            if i=='Java':
                Java=1
            if i=='JavaScript':
                JavaScript=1
            if i=='Node.js':
                Nodejs=1
            if i=='TypeScript':
                TypeScript=1
            if i=='Python':
                Python=1
            if i=='Kotlin':
                Kotlin=1
            if i=='R':
                R=1
            if i=='SQL':
                SQL=1
        #inputs for databases
        databases=request.form.getlist('DatabaseHaveWorkedWith')
        MSserver=0
        Mysql=0
        Postgresql=0
        Redis=0
        MongoDB=0
        SQlite=0
        MariaDB=0
        Firebase=0
        Oracle=0
        DynamoDB=0
        Nodatabase=0
        for i in databases:
            if i=='Microsoft SQL Server':
                MSserver=1   
            if i=='MySQL':
                Mysql=1
            if i=='PostgreSQL':
                Postgresql=1
            if i=='Redis':
                Redis=1
            if i=='MongoDB':
                MongoDB=1
            if i=='SQLite':
                SQlite=1
            if i=='MariaDB':
                MariaDB=1
            if i=='Firebase':
                Firebase=1
            if i=='Oracle':
                Oracle=1
            if i=='DynamoDB':
                DynamoDB=1
            if i=='I dont use databases':
                Nodatabase=1
        #input for cloud platforms
        platforms=request.form.getlist('PlatformHaveWorkedWith')
        AWS=0
        GCP=0
        Azure=0
        othercloud=0
        nocloud=0
        for i in platforms:
            if i=='AWS':
                AWS=1   
            if i=='GCP':
                GCP=1
            if i=='Microsoft Azure':
                Azure=1
            if i=='Other Cloud Platforms':
                othercloud=1
            if i=='I dont use any cloud platforms':
                nocloud=1
        #inputs for webframeworks
        webframe=request.form.getlist('WebframeHaveWorkedWith')
        reactjs=0
        spring=0
        angular=0
        asp=0
        django=0
        flask=0
        jquery=0
        otherweb=0
        noweb=0
        for i in webframe:
            if i=='React.js':
                reactjs=1
            if i=='Spring':
                spring=1
            if i=='Angular':
                angular=1
            if i=='ASP.NET or ASP.NET Core':
                asp=1
            if i=='Django':
                django=1
            if i=='Flask':
                flask=1
            if i=='jQuery':
                jquery=1
            if i=='Other webframeworks':
                otherweb=1
            if i=='I dont use any webframeworks':
                noweb=1
        #inputs for other frameworks
        otherframe=request.form.getlist('MiscTechHaveWorkedWith')
        numpy=0
        pandas=0
        keras=0
        apache=0
        hadoop=0
        netframe=0
        netcore=0
        flutter=0
        reactnat=0
        pytorch=0
        nootherweb=0
        for i in otherframe:
            if i=='NumPy':
                numpy=1
            if i=='Pandas':
                pandas=1
            if i=='Keras/Tensorflow':
                keras=1
            if i=='Apache Spark':
                apache=1
            if i=='Hadoop':
                hadoop=1
            if i=='.NET Framework':
                netframe=1
            if i=='.NET Core/.NET 5':
                netcore=1
            if i=='Flutter':
                flutter=1
            if i=='React Native':
                reactnat=1
            if i=='Torch/PyTorch':
                pytorch=1
            if i=='No other frameworks used':
                nootherweb=1
        #inputs for other frameworks
        tools=request.form.getlist('ToolsTechHaveWorkedWith')
        git=0
        docker=0
        kubernetes=0
        terraform=0
        notool=0
        for i in tools:
            if i=='Git':
                git=1
            if i=='Docker':
                docker=1
            if i=='Kubernetes':
                kubernetes=1
            if i=='Terraform':
                terraform=1
            if i=='No extra tools used':
                notool=1
        #input numpy array
        data=np.array([employment, country, edlevel,yearscode,devtype,orgsize,age,gender,C,Cplus,Csharp,Dart,Go,BashShell,HTMLCSS,Java,JavaScript,Nodejs,TypeScript,Python,Kotlin,R,SQL,MSserver,Mysql,Postgresql,
        Redis,MongoDB,SQlite,MariaDB,Firebase,Oracle,DynamoDB,Nodatabase, AWS,GCP,Azure,othercloud,nocloud,reactjs,spring,angular,asp,django,flask,jquery,noweb,otherweb, numpy,
        pandas,keras,apache,hadoop,netframe,netcore,flutter,reactnat,pytorch,nootherweb,git,docker,kubernetes,terraform,notool]).reshape(1,-1)

        cols=['Employment', 'Country', 'EdLevel', 'YearsCode', 'DevType', 'OrgSize',
       'Age', 'Gender', 'C', 'C++', 'C#', 'Dart', 'Go',
       'Bash/Shell', 'HTML/CSS', 'Java', 'JavaScript', 'Node.js', 'TypeScript',
       'Python', 'Kotlin', 'R', 'SQL', 'Microsoft SQL Server', 'MySQL',
       'PostgreSQL', 'Redis', 'MongoDB', 'SQLite', 'MariaDB', 'Firebase',
       'Oracle', 'DynamoDB', 'I dont use databases', 'AWS', 'GCP',
       'Microsoft Azure', 'Other Cloud Platforms',
       'I dont use any cloud platforms', 'React.js', 'Spring', 'Angular',
       'ASP.NET or ASP.NET Core', 'Django', 'Flask', 'jQuery',
       'I dont use any webframeworks', 'Other webframeworks', 'NumPy',
       'Pandas', 'Keras/Tensorflow', 'Apache Spark', 'Hadoop',
       '.NET Framework', '.NET Core/.NET 5', 'Flutter', 'React Native',
       'Torch/PyTorch', 'No other frameworks used', 'Git', 'Docker',
       'Kubernetes', 'Terraform', 'No extra tools used']

       
        dataframe=pd.DataFrame(data=data, columns=cols)
        preprocess=joblib.load('preprocessing.joblib')
        processed_data=preprocess.transform(dataframe)
        processed_data=processed_data.astype(float)
        model_new=tf.keras.wrappers.scikit_learn.KerasRegressor(build_fn=base_model, epochs=400, batch_size=1000, verbose=1)
        model_new.model=tf.keras.models.load_model('model.h5')
        prediction=model_new.model.predict(processed_data, verbose=0)
        predict=float(prediction)
        return render_template('index.html',prediction_text="Your predicted salary is $ {}".format(int(np.exp(predict))))

if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)