from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit,ResizeToFill


# Create your models here.

class Actor(models.Model):
    actorname = models.CharField(max_length=128,
                                verbose_name='배우이름')
    career = models.TextField(default = '',verbose_name='대표 작품',)   
    photo1 = ProcessedImageField(
        upload_to='actor_images/',
        processors=[ResizeToFill(350,500)],
    )
    def __str__(self):
        return 'Name: %s' %(self.actorname)
    class Meta:
        db_table = 'actors_list'
        verbose_name = '배우 리스트'
        verbose_name_plural = '배우 리스트'

class Director(models.Model):
    directorname = models.CharField(max_length=128,
                                verbose_name='감독이름')
    career2 = models.TextField(default = '',verbose_name='대표 작품',)   
    photo2 = ProcessedImageField(
        upload_to='director_images/',
        processors=[ResizeToFill(350,500)],
    )
    def __str__(self):
        return 'Name: %s' %(self.directorname)
    class Meta:
        db_table = 'directors_list'
        verbose_name = '감독 리스트'
        verbose_name_plural = '감독 리스트'

           
class Movie(models.Model):
    moviename = models.CharField(max_length=128,
                                verbose_name='영화이름')
    career3 = models.TextField(default = '',verbose_name='대표 작품',)   
    photo3 = ProcessedImageField(
        upload_to='movie_images/',
        processors=[ResizeToFill(350,500)],
    )
    def __str__(self):
        return 'Name: %s' %(self.moviename)
    class Meta:
        db_table = 'movies_list'
        verbose_name = '영화 리스트'
        verbose_name_plural = '영화 리스트'

class Section1(models.Model):
    director_1 = models.TextField(default = '', verbose_name='감독이름')
    act1_1 = models.TextField(default = '', verbose_name='배우이름1')
    act2_1 = models.TextField(default = '', verbose_name='배우이름2')
    act3_1 = models.TextField(default = '', verbose_name='배우이름3')                            
    act4_1 = models.TextField(default = '', verbose_name='배우이름4')
    genre_1 = models.TextField(default = '', verbose_name='장르')
    rating_1 = models.TextField(default = '', verbose_name='연령')
    dist_1 = models.TextField(default = '', verbose_name='배급사')
    
    def __str__(self):
        return self.act1_1

    class Meta:
        db_table = 'section0110'
        verbose_name = '섹션1 선택 리스트(감독1,배우4,옵션3)'
        verbose_name_plural = '섹션1 선택 리스트(감독1,배우4,옵션3)'

class Section1_DirectorLists(models.Model):
    director_1  = models.TextField(default = '', verbose_name='영화 이름')

    def __str__(self):
        return director_1
    class Meta:
        db_table = '_director_list'
        verbose_name = '섹션1 감독 리스트'
        verbose_name_plural = '섹션1 감독 리스트' 


class Section1_ActorLists(models.Model):
    act1_1 = models.TextField(default = '', verbose_name='배우이름1')
    act2_1 = models.TextField(default = '', verbose_name='배우이름2')
    act3_1 = models.TextField(default = '', verbose_name='배우이름3')                            
    act4_1 = models.TextField(default = '', verbose_name='배우이름4')

    def __str__(self):
        return self.act1_1

    class Meta:
        db_table = '_actor_list1'
        verbose_name = '섹션1 배우 리스트들'
        verbose_name_plural = '섹션1 배우 리스트들'

class Section2(models.Model):
    moviename = models.TextField(default = '', verbose_name='영화 이름')
    act1_2 = models.TextField(default = '', verbose_name='배우이름1')
    act2_2 = models.TextField(default = '', verbose_name='배우이름2')
    act3_2 = models.TextField(default = '', verbose_name='배우이름3')                            
    act4_2 = models.TextField(default = '', verbose_name='배우이름4')
    def __str__(self):
        return self.moviename

    class Meta:
        db_table = '_section02'
        verbose_name = '섹션2  선택 리스트(영화1,배우4)'
        verbose_name_plural = '섹션2  선택 리스트(영화1,배우4)'

class Section2_MovieLists(models.Model):
    
    moviename = models.TextField(default = '', verbose_name='영화 이름')
    def __str__(self):
        return self.moviename 
    class Meta:
        db_table = '_movie_list'
        verbose_name = '섹션2 영화 리스트들'
        verbose_name_plural = '섹션2 영화 리스트들'  
        
class Section2_ActorLists(models.Model):
    act1_2 = models.TextField(default = '', verbose_name='배우이름1')
    act2_2 = models.TextField(default = '', verbose_name='배우이름2')
    act3_2 = models.TextField(default = '', verbose_name='배우이름3')                            
    act4_2 = models.TextField(default = '', verbose_name='배우이름4')
    def __str__(self):
        return self.act1_2

    class Meta:
        db_table = '_actor_list'
        verbose_name = '섹션2 배우 리스트들'
        verbose_name_plural = '섹션2 배우 리스트들'

