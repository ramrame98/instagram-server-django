from django.urls import path
from .views import AllFeeds, UserNameFeeds

urlpatterns = [
    path("", AllFeeds.as_view()),
    path("<str:username>", UserNameFeeds.as_view())
]



# api/v1/feeds
# api/v1/feeds/1
# api/v1/feeds/1/reviews
