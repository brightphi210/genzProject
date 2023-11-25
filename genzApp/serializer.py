
from .models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'terms']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        # extra_kwargs = {'password': {'write_only': True}}

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # depth = 1


class StorySerializer(ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'
        # depth = 1

class MagazineStorySerializer(ModelSerializer):
    class Meta:
        model = MagazineStories
        fields = '__all__'

class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ['id', 'email', 'subscribed', 'subscribed_date']
        # depth = 1


# =================== Subscriptio ================================
class SubscriptionPlanSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['user', 'price', 'category', 'start_date', 'end_date', 'payment_status']
