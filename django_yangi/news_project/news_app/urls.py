from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, categoryPageView

urlpatterns = [
  path('', homePageView, name='home_page'),
  path('contact/', ContactPageView.as_view(), name='contact'),
  path('catagory/', categoryPageView, name='catagory'),
  path('news/', news_list, name='all_news_list'),
  path('news/<int:id>/', news_detail, name='news_detail_page')
]