from django.urls import path
from bookmark.views import BookmarkLV, BookmarkAdd

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('add/', BookmarkAdd.as_view(), name='add'),
]