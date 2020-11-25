from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Actor,Director,Movie
from .models import Section1,Section1_DirectorLists,Section1_ActorLists
from .models import Section2,Section2_MovieLists,Section2_ActorLists

# Register your models here.
    

class ActorAdmin(admin.ModelAdmin):
    field =('actorname', 'photo1','career1', )
    list_display = ('actorname', 'photo1',) #'get_image')
    search_fields = ['actorname']
    list_filter = ('actorname',)
    # readonly_field = [] #필드 고정 = 수정 못하게
    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height={height} />'.format(
            url = obj.photo1.url,
            width = 50,
            height= 50,
        )
     )

class DirectorAdmin(admin.ModelAdmin):
    field =('directorname', 'photo2','career2', )
    list_display = ('directorname', 'photo2',) #'get_image')
    search_fields = ['directorname']
    list_filter = ('directorname',)

    # readonly_field = [] #필드 고정 = 수정 못하게

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height={height} />'.format(
            url = obj.photo2.url,
            width = 50,
            height= 50,
        )
     )

class MovieAdmin(admin.ModelAdmin):
    field =('moviename', 'photo3','career3', )
    list_display = ('moviename', 'photo3',) #'get_image')
    search_fields = ['moviename']
    list_filter = ('moviename',)
    # readonly_field = [] #필드 고정 = 수정 못하게

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height={height} />'.format(
            url = obj.photo3.url,
            width = 50,
            height= 50,
        )
     )
class Section1Admin(admin.ModelAdmin):
    field =('director_1','act1_1','act2_1','act3_1','act4_1','genre_1',)
    list_display = ('director_1','act1_1','act2_1','act3_1','act4_1','genre_1',)

class DirectorlistAdmin(admin.ModelAdmin):
    field =('id', 'director_1',  )
    list_display = ('id','director_1',)

class Actorlist1Amin(admin.ModelAdmin):
    field =('id','act1_1','act2_1','act3_1','act4_1',)
    list_display = ('id','act1_1','act2_1','act3_1','act4_1',)


class Section2Admin(admin.ModelAdmin):
    field =('moviename','act1_2','act2_2','act3_2','act4_2',)
    list_display = ('moviename','act1_2','act2_2','act3_2','act4_2',)

class MovielistAdmin(admin.ModelAdmin):
    field =('moviename',  )
    list_display = ('moviename',)

class Actorlist2Amin(admin.ModelAdmin):
    field =('act1_2','act2_2','act3_2','act4_2',)
    list_display = ('act1_2','act2_2','act3_2','act4_2',)
   
admin.site.register(Section1, Section1Admin)
admin.site.register(Section1_DirectorLists,DirectorlistAdmin)  
admin.site.register(Section1_ActorLists,Actorlist1Amin)

admin.site.register(Section2, Section2Admin) 
admin.site.register(Section2_MovieLists,MovielistAdmin)    
admin.site.register(Section2_ActorLists,Actorlist2Amin)  

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
