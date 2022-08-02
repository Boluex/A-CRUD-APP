from django.urls import path
from.import views
# from. import views
urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('about/',views.about,name='about'),
    path('add_comment/<int:id>',views.add_comment,name='add_comment'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('destroy/<int:id>',views.destroy,name='destroy'),
    path('update/<int:id>',views.update,name='update'),
    path('update_comment/<int:id>',views.update_comment,name='updates'),
    path('comments/<int:id>',views.comments,name='comment'),
]