from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from .serializers import FeedSerializer, FeedDetailSerializer
from rest_framework.exceptions import ParseError, NotFound
class AllFeeds(APIView):
  def get(self, request):
    all_feeds = Feed.objects.all()
    serializer = FeedSerializer(all_feeds, many =True)  # 받아오는 객체가 2개 이상이면 many=True를 써야함.
    
    return Response(serializer.data)
  
class FeedDetail(APIView):
  def get(self,request,pk):
    try:
      feed = Feed.objects.get(pk=pk)
    except Feed.DoesNotExist:
      raise NotFound
    serializer = FeedDetailSerializer(feed)
    return Response(serializer.data)
  
class FeedReviews(APIView):
  def get(self,reqeust,pk):
    try:
      feed = Feed.objects.get(pk=pk)
    except Feed.DoesNotExist:
      raise NotFound
    review = Review.objects.filter(feed = feed)
    seriailizer = ReviewSerializer(review, many=True)
    return Response(seriailizer.data)
    