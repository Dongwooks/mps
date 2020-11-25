from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.http import HttpResponse

import os
import pandas as pd
import numpy as np
from random import *
from sklearn import datasets
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Create your views here.
from .models import Actor,Director,Movie
from .models import Section1,Section1_DirectorLists,Section1_ActorLists
from .models import Section2,Section2_MovieLists,Section2_ActorLists
# Create your views here.


def home(request):
    return render(request, 'home.html')

def section1(request):
    return render(request, 'section1.html')
    
def section2(request):
    return render(request, 'section2.html')

def tag_section1(request):
    if request.method == 'GET':
         temp_director_1 = Section1_DirectorLists.objects.values('director_1').last()  
         temp_act1_1 = Section1_ActorLists.objects.values('act1_1').last()  
         temp_act2_1 = Section1_ActorLists.objects.values('act2_1').last()  
         temp_act3_1 = Section1_ActorLists.objects.values('act3_1').last()   
         temp_act4_1 = Section1_ActorLists.objects.values('act4_1').last()
        
         director_1 = temp_director_1['director_1']    
         act1_1 = temp_act1_1['act1_1']      
         act2_1 = temp_act2_1['act2_1'] 
         act3_1 = temp_act3_1['act3_1']  
         act4_1 = temp_act4_1['act4_1']

         return render(request, 'tag_section1.html', {
            'director_1':director_1,
            'act1_1':act1_1,
            'act2_1':act2_1,
            'act3_1':act3_1,
            'act4_1':act4_1 } )
            
    elif request.method == 'POST':

      temp_director_1 = Section1_DirectorLists.objects.values('director_1').last()  
      temp_act1_1 = Section1_ActorLists.objects.values('act1_1').last()  
      temp_act2_1 = Section1_ActorLists.objects.values('act2_1').last()  
      temp_act3_1 = Section1_ActorLists.objects.values('act3_1').last()   
      temp_act4_1 = Section1_ActorLists.objects.values('act4_1').last()  

      director_1 = temp_director_1['director_1']

      act1_1 = temp_act1_1['act1_1']      
      act2_1 = temp_act2_1['act2_1'] 
      act3_1 = temp_act3_1['act3_1']  
      act4_1 = temp_act4_1['act4_1']

      genre_1 = request.POST['genre_1']
      rating_1 = request.POST['rating_1']
      dist_1 = request.POST['dist_1'] 
      
    user1 = Section1(
       director_1 = director_1,
       act1_1 = act1_1,
       act2_1 = act2_1,
       act3_1 = act3_1,
       act4_1 = act4_1,
       genre_1 = genre_1,
       rating_1 = rating_1,
       dist_1 = dist_1
    )
    user1.save()
    
    data = pd.read_csv('models/0.data_final.csv', encoding="euc-kr")
    data2 = pd.read_csv('models/0.data_modify.csv', encoding="euc-kr")

    director = director_1
    act1 = act1_1
    act2 = act2_1
    act3 = act3_1
    act4 = act4_1
    genre = genre_1
    rating = rating_1
    dist = dist_1

# 복사본 사용
    search_data = data2.copy()
# 예측 데이터로 쓸 데이터프레임
    pred_data = pd.DataFrame({"screen_cnt":[0], "holiday":[0], "dir_score":[0], "actor1_score":[0], "actor2_score":[0], "actor3_score":[0],
                          "actor4_score":[0], "dist_score":[0], "Action":[0], "Adventure":[0], "Comedy":[0], "Crime":[0], "Drama":[0],
                          "Family":[0], "Fantasy":[0], "History":[0], "Horror":[0], "Mystery":[0], "Romance":[0], "SF":[0],
                          "Thriller":[0], "War":[0], "12_rating":[0], "15_rating":[0], "20_rating":[0], "all_rating":[0]})

# 감독점수 처리
    temp_dir= director
    temp_data = search_data[search_data['director'] == temp_dir]
    temp_dir_score = temp_data['audi_cnt'].max()
    pred_data['dir_score'] = temp_dir_score

# 배우점수 처리
    temp_act = act1
    temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
    temp_act1_score = temp_data['audi_cnt'].max()
    pred_data['actor1_score'] = temp_act1_score

    temp_act = act2
    temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
    temp_act2_score = temp_data['audi_cnt'].max()
    pred_data['actor2_score'] = temp_act2_score

    temp_act = act3
    temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
    temp_act3_score = temp_data['audi_cnt'].max()
    pred_data['actor3_score'] = temp_act3_score

    temp_act = act4
    temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
    temp_act4_score = temp_data['audi_cnt'].max()
    pred_data['actor4_score'] = temp_act4_score
   
# 배급사점수 처리
    temp_dist = dist
    temp_data = search_data[(search_data['distributor'] == temp_dist)]
    temp_dist_score = temp_data['screen_cnt'].head(5).mean()
    temp_dist_score = round(temp_dist_score)
    pred_data['dist_score'] = temp_dist_score
    
# 공휴일 처리
    temp_holiday = randint(0, 1)
    pred_data['holiday'] = temp_holiday
    
# 장르 처리
    if genre == '액션':
      pred_data['Action'] = 1
    elif genre == '어드벤처':
        pred_data['Adventure'] = 1
    elif genre == '코미디':
       pred_data['Comedy'] = 1
    elif genre == '범죄':
     pred_data['Crime'] = 1
    elif genre == '드라마':
       pred_data['Drama'] = 1
    elif genre == '가족':
      pred_data['Family'] = 1
    elif genre == '판타지':
       pred_data['Fantasy'] = 1
    elif genre == '사극':
       pred_data['History'] = 1
    elif genre == '공포(호러)':
       pred_data['Horror'] = 1
    elif genre == '미스터리':
       pred_data['Mystery'] = 1
    elif genre == '멜로/로맨스':
      pred_data['Romance'] = 1
    elif genre == 'SF':
      pred_data['SF'] = 1
    elif genre == '스릴러':
       pred_data['Thriller'] = 1
    elif genre == '전쟁':
      pred_data['War'] = 1

# 등급 처리
    if rating == '12세이상관람가':
        pred_data['12_rating'] = 1
    elif rating == '15세이상관람가':
       pred_data['15_rating'] = 1
    elif rating == '전체관람가':
       pred_data['all_rating'] = 1
    elif rating == '청소년관람불가':
      pred_data['20_rating'] = 1

# 스크린수 처리  
    scr_data = data2.copy()
    scr_data = scr_data.drop(['movieNm', 'director', 'company', 'distributor', 'openDt', 'nation', 'audi_cnt', 'genre', 'rating', 'actor1',
                              'actor2', 'actor3', 'actor4', 'audi_score', 'exp_score'], axis = 1)
    
    target_data2 = scr_data['screen_cnt']
    train_data2 = scr_data.drop(['screen_cnt'], axis = 1)
    
    X_train2, X_test2, y_train2, y_test2 = train_test_split(train_data2, target_data2, test_size = 0.3, random_state = 777)
   
    scr_rf_reg = RandomForestRegressor(random_state=0)
    scr_rf_reg.fit(X_train2, y_train2)
   
    scr_train = pred_data.copy()
    scr_train = scr_train.drop(['screen_cnt'], axis = 1)
    
    scr_pred = scr_rf_reg.predict(scr_train)
    scr_pred = int(round(scr_pred[0]))
    pred_data['screen_cnt'] = scr_pred

# 복사본 사용
    ML_data = data.copy()

# 머신러닝에 사용되지 않는 컬럼 제거
    ML_data = ML_data.drop(['movieNm', 'director', 'company', 'distributor', 'openDt', 'nation', 'genre', 'rating', 'actor1', 'actor2', 
                     'actor3', 'actor4', 'audi_score', 'exp_score'], axis = 1)
    
# 머신러닝 학습
    target_data = ML_data['audi_cnt']
    train_data = ML_data.drop(['audi_cnt'], axis = 1)

    X_train, X_test, y_train, y_test = train_test_split(train_data, target_data, test_size = 0.3, random_state = 777)
    
    rf_reg = RandomForestRegressor(n_estimators=800, max_depth=8, min_samples_leaf=1, min_samples_split=2, random_state=0)
    rf_reg.fit(X_train, y_train)
#결과 저장    
    result = rf_reg.predict(pred_data)
    result = int(round(result[0]))
    context = {'result':result}
    return render(request, 'result.html', context)

def result(request):

    return render(request, 'result.html')

def tag_section2(request):
   if request.method == 'GET':
        temp_moviename = Section2_MovieLists.objects.values('moviename').last()  
        temp_act1_2 = Section2_ActorLists.objects.values('act1_2').last()  
        temp_act2_2 = Section2_ActorLists.objects.values('act2_2').last()  
        temp_act3_2 = Section2_ActorLists.objects.values('act3_2').last()   
        temp_act4_2 = Section2_ActorLists.objects.values('act4_2').last()
        
        moviename = temp_moviename['moviename']

        act1_2 = temp_act1_2['act1_2']      
        act2_2 = temp_act2_2['act2_2'] 
        act3_2 = temp_act3_2['act3_2']  
        act4_2 = temp_act4_2['act4_2']
        return render(request, 'tag_section2.html', {
            'moviename':moviename,
            'act1_2':act1_2,
            'act2_2':act2_2,
            'act3_2':act3_2,
            'act4_2':act4_2 } )
            
   elif request.method == 'POST':
      temp_moviename = Section2_MovieLists.objects.values('moviename').last()  
      temp_act1_2 = Section2_ActorLists.objects.values('act1_2').last()  
      temp_act2_2 = Section2_ActorLists.objects.values('act2_2').last()  
      temp_act3_2 = Section2_ActorLists.objects.values('act3_2').last()   
      temp_act4_2 = Section2_ActorLists.objects.values('act4_2').last() 

      moviename = temp_moviename['moviename']

      act1_2 = temp_act1_2['act1_2']      
      act2_2 = temp_act2_2['act2_2'] 
      act3_2 = temp_act3_2['act3_2']  
      act4_2 = temp_act4_2['act4_2']
      
   user2 = Section2(
       moviename= moviename,
       act1_2 = act1_2,
       act2_2 = act2_2,
       act3_2 = act3_2,
       act4_2 = act4_2
    )

   user2.save()

   data = pd.read_csv('models/0.data_final.csv', encoding="euc-kr")
   data2 = pd.read_csv('models/0.data_modify.csv', encoding="euc-kr")

   moviename = moviename
   act1 = act1_2
   act2 = act2_2
   act3 = act3_2
   act4 = act4_2

   search_data = data2

# 예측 데이터로 쓸 데이터프레임
   pred_data = pd.DataFrame({"screen_cnt":[0], "audi_score":[0], "exp_score":[0], "holiday":[0], "dir_score":[0], "actor1_score":[0],
                             "actor2_score":[0], "actor3_score":[0], "actor4_score":[0], "dist_score":[0], "Action":[0], "Adventure":[0],
                             "Comedy":[0], "Crime":[0], "Drama":[0], "Family":[0], "Fantasy":[0], "History":[0], "Horror":[0],
                             "Mystery":[0], "Romance":[0], "SF":[0], "Thriller":[0], "War":[0], "12_rating":[0], "15_rating":[0],
                             "20_rating":[0], "all_rating":[0]})
                             
# 배우점수 처리
   temp_act = act1
   temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
   temp_act1_score = temp_data['audi_cnt'].max()
   pred_data['actor1_score'] = temp_act1_score


   temp_act = act2
   temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
   temp_act2_score = temp_data['audi_cnt'].max()
   pred_data['actor2_score'] = temp_act2_score


   temp_act = act3
   temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
   temp_act3_score = temp_data['audi_cnt'].max()
   pred_data['actor3_score'] = temp_act3_score

   temp_act = act4
   temp_data = search_data[(search_data['actor1'] == temp_act) | (search_data['actor2'] == temp_act) | (search_data['actor3'] == temp_act) | (search_data['actor4'] == temp_act)]
   temp_act4_score = temp_data['audi_cnt'].max()
   pred_data['actor4_score'] = temp_act4_score

# 기존 영화 데이터
   idx = search_data['movieNm'].index[search_data['movieNm'] == moviename]
   ori_data = search_data.iloc[idx]

   ori_audi_cnt = ori_data['audi_cnt'].iloc[0]    # 기존 영화 관객수

   col_list = ['screen_cnt', 'audi_score', 'exp_score', 'holiday', 'dir_score', 'dist_score', 'Action', 'Adventure', 'Comedy', 'Crime',
           'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Mystery', 'Romance', 'SF', 'Thriller', 'War', '12_rating', '15_rating',
           '20_rating', 'all_rating']
   for col in col_list:
      pred_data[col] = ori_data[col].iloc[0]

# 복사본 사용
   ML_data = data.copy()

# 머신러닝에 사용되지 않는 컬럼 제거
   ML_data = ML_data.drop(['movieNm', 'director', 'company', 'distributor', 'openDt', 'nation', 'genre', 'rating', 'actor1', 'actor2', 
                   'actor3', 'actor4'], axis = 1)

# 머신러닝 학습
   target_data = ML_data['audi_cnt']
   train_data = ML_data.drop(['audi_cnt'], axis = 1)

   X_train, X_test, y_train, y_test = train_test_split(train_data, target_data, test_size = 0.3, random_state = 777)

   rf_reg = RandomForestRegressor(n_estimators=800, max_depth=8, min_samples_leaf=1, min_samples_split=2, random_state=0)
   rf_reg.fit(X_train, y_train)

# 예측 결과 출력
   result = rf_reg.predict(pred_data)
   result = int(round(result[0]))
   context = {'result': result}
   return render(request, 'result.html', context)


def director_list(request):
    all_directors = Director.objects.all().order_by('-id')

    if request.method == 'GET':
        
        return render(request, 'director_list.html',{'directors':all_directors})

    elif request.method == 'POST':
        director_1 = request.POST.get('director_1',None)
        tag_result = request.POST.get('director_1')
        section1_list = Section1_DirectorLists(
            director_1 = director_1,
         )
        section1_list.save()
        
        return render(request, 'section1.html', {'tag_result':tag_result})

def actor1_list(request):
    all_actors = Actor.objects.all().order_by('-id')
    if request.method == 'GET':
        return render(request, 'actor_list.html',{'actors':all_actors})
    elif request.method == 'POST':
        act1 = request.POST.get('act1_1',None)
        act2 = request.POST.get('act2_1',None) 
        act3 = request.POST.get('act3_1',None) 
        act4 = request.POST.get('act4_1',None)
        

        actorlist1 = Section1_ActorLists(
             act1_1 = act1,
             act2_1 = act2,
             act3_1 = act3,
             act4_1 = act4,
        )
        actorlist1.save()
        
        return redirect('main/tag_section1/') 


def movie_list(request):
    all_movies = Movie.objects.all().order_by('-id')
    if request.method == 'GET':
        return render(request, 'movie_list.html',{'movies':all_movies})

    elif request.method == 'POST':
        moviename1 = request.POST.get('moviename')
        tag_result = request.POST.get('moviename')
        section2_list = Section2_MovieLists(
            moviename = moviename1
        )
        section2_list.save()
        res_data = {}
        return render(request, 'section2.html', {'tag_result':tag_result})
    

def actor2_list(request):
    all_actors = Actor.objects.all().order_by('-id')
    if request.method == 'GET':
        return render(request, 'actor_list2.html',{'actors':all_actors})
    elif request.method == 'POST':
        act1_2 = request.POST.get('act1_1')
        act2_2 = request.POST.get('act2_1')
        act3_2 = request.POST.get('act3_1')
        act4_2 = request.POST.get('act4_1')

        section2_list = Section2_ActorLists(
             act1_2 = act1_2,
             act2_2 = act2_2,
             act3_2 = act3_2,
             act4_2 = act4_2,
            )
        section2_lists = section2_list.save()
        
        return redirect('main/tag_section2/')
 


