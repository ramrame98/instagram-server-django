from django.urls import path
from .views import AllFeeds, FeedDetail,FeedReviews

urlpatterns = [
    path("", AllFeeds.as_view()),
    path("<int:pk>", FeedDetail.as_view()),
    path("<int:pk>/reviews", FeedReviews.as_view())
]


# api/v1/feeds
# api/v1/feeds/1
# api/v1/feeds/1/reviews
