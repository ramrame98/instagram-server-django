from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import UserSerializer
from feeds.serializers import FeedSerializer
class ReviewSerializer(ModelSerializer):
  user = UserSerializer()
  feed = FeedSerializer()
  class Meta:
    model = Review
    fields = "__all__"
