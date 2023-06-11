The Assignment

Take the data from the Student Performance dataset, create a pipeline to clean it and create a MongoDB instance to house your data. Upload the code you used to clean your data and input into mongo GitHub and submit the link here.

UCI Machine Learning Repository: Student Performance Data Set
https://archive.ics.uci.edu/ml/datasets/Stud

Steps taken
1. Cleaned the data from UCI on clean_data.ipynb
2. Created the base.py from the cleaned csv
3. Created a new database on MongoDB, created .env with the new MONGO_URL and login credientals to connect to the database
4. to_mongo.py to link and upload the cleaned data to MongoDB

06082023 - Update
Added streamlit function: front_page.py
Added pages / query.py
Able to query school data.
