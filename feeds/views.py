from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from users.models import User
from .serializers import FeedSerializer
from rest_framework.exceptions import ParseError, NotFound

# 전체 게시글을 불러오는 API
class AllFeeds(APIView):
  def get(self, request):
    all_feeds = Feed.objects.all()
    serializer = FeedSerializer(all_feeds, many =True)  # 받아오는 객체가 2개 이상이면 many=True를 써야함.
    
    return Response(serializer.data)

# 유저네임을 기반으로 특정 유저의 게시글을 불러오는 API 
class UserNameFeeds(APIView):
  def get(self,request,username):
    print("username", username)
    try:
      user= User.objects.get(username=username)
      print("user.id", user.id)
      
      user_feeds = Feed.objects.filter(user_id=user.id)
      print("user_feeds", user_feeds)
    except Feed.DoesNotExist:
      raise NotFound
    serializer = FeedSerializer(user_feeds, many=True)
    return Response(serializer.data)
  
# class FeedReviews(APIView):
#   def get(self,reqeust,pk):
#     try:
#       feed = Feed.objects.get(pk=pk)
#     except Feed.DoesNotExist:
#       raise NotFound
#     review = Review.objects.filter(feed = feed)
#     seriailizer = ReviewSerializer(review, many=True)
#     return Response(seriailizer.data)
    