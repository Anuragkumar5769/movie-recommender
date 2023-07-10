# importing Flask and other modules
from flask import Flask, request, render_template ,redirect,url_for
import pickle
import numpy as np
import pandas as pd
import csv
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import bs4 as bs
import urllib.request
import requests



# Flask constructor
app = Flask(__name__)

dataframe= pd.read_pickle(open(r"C:\Users\anura\OneDrive\Desktop\web development\flask-wala\static\new_df.pkl",'rb'))
movies_name_list= dataframe['original_title'].values.tolist()

df2= pd.read_pickle(open(r"C:\Users\anura\OneDrive\Desktop\web development\flask-wala\static\og_data.pkl",'rb'))

vectorizer = CountVectorizer(max_features=5000,stop_words='english')
v=vectorizer.fit_transform(dataframe['tags'])

similarity=cosine_similarity(v)
list(enumerate(similarity[0]))

def listToString(s):
 
    # initialize an empty string
    str1 = " "
 
    # return string
    return (str1.join(s))

def convert(obj):
    res2 = list(eval(obj))
    l=[]
    i=0
    while(i<len(res2)):
        l.append(res2[i]['name'])
        l.append('|')
        i+=1
    return l

def convert_cast(obj):
    res3 = list(eval(obj))
    l=[]
    i=0
    while(i<3):
        l.append(res3[i]['name'])
        l.append(',')
        i+=1
    return l

def recommend(movie):
    movie_index= dataframe[dataframe['original_title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True  ,key=lambda x:x[1])[0:7] #0 index is movie himself
    tit=[]
    dat=[]
    rating=[]
    moviedetails=[]
    movietypes=[]
    movieid=[]
    cast=[]
    
    for i in movies_list:
        tit.append(df2.iloc[i[0]].original_title)
        dat.append((df2.iloc[i[0]].release_date)[0:4])
        rating.append(df2.iloc[i[0]].vote_average)
        moviedetails.append(''.join([str(elem) for elem in (df2.iloc[i[0]].overview)]))
        movietypes.append(listToString(convert(df2.iloc[i[0]].genres)))
        movieid.append(df2.iloc[i[0]].id)
        cast.append(listToString(convert_cast(df2.iloc[i[0]].cast)))

    print(moviedetails[0])
    return_df = pd.DataFrame()
    return_df['Title'] = tit
    return_df['Year'] = dat
    return_df['Ratings'] = rating
    return_df['Overview']=moviedetails
    return_df['Types']=movietypes
    return_df['ID']=movieid
    return_df['cast']=cast
    return return_df 


 

@app.route('/',methods =["GET","POST"])
def home():
        if request.method =="POST":
            movie_name_input=(request.form["movie-name_input"])
            # nya_list=recommend(movie_name)
            return redirect(url_for("main",movie_name=movie_name_input)) 
            
        else:
             return render_template("index.html",movies_name_list=movies_name_list)
   

@app.route('/<movie_name>')
def main(movie_name):
        if movie_name not in movies_name_list:
            random_list=df2.sample(n=6)
            tit=[]
            dat=[]
            rating=[]
            moviedetails=[]
            movietypes=[]
            movieid=[]
            cast=[]
            
            i=0
            while i<6:
                tit.append(random_list.iloc[i].original_title)
                dat.append((random_list.iloc[i].release_date)[0:4])
                rating.append(random_list.iloc[i].vote_average)
                moviedetails.append(''.join([str(elem) for elem in (random_list.iloc[i].overview)]))
                movietypes.append(listToString(convert(random_list.iloc[i].genres)))
                movieid.append(random_list.iloc[i].id)
                cast.append(listToString(convert_cast(random_list.iloc[i].cast)))
                i=i+1

            return render_template('negative.html',movie_type=movietypes,movieid=movieid,movie_overview=moviedetails,year=dat,Ratings=rating,movie_title=tit,cast=cast)

        
        else:    
            m_name = movie_name
            
            # with open('movieR.csv', 'a',newline='') as csv_file:
            #     fieldnames = ['Movie']
            #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #     writer.writerow({'Movie': m_name})
            result_final = recommend(m_name)
            names = []
            dates = []
            ratings = []
            overview=[]
            types=[]
            mid=[]
            cast=[]
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                dates.append(result_final.iloc[i][1])
                ratings.append(result_final.iloc[i][2])
                overview.append(result_final.iloc[i][3])
                types.append(result_final.iloc[i][4])
                mid.append(result_final.iloc[i][5])
                cast.append(result_final.iloc[i][6])
                
            return render_template('content.html',movie_type=types,movieid=mid,movie_overview=overview,year=dates,Ratings=ratings,movie_title=names,search_name=m_name,cast=cast)

       


if __name__=='__main__':
    app.run(debug=True)
