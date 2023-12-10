
from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'terms', 'is_user']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["is_user"] = user.is_user
        token["is_admin"] = user.is_admin
        token["is_author"] = user.is_author

        token["name"] = user.name
        token["email"] = user.email
        
        token["profile_pic"] = user.profile_pic.url if user.profile_pic else None

        return token


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'



class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_author']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         token["is_user"] = user.is_user
#         token["is_admin"] = user.is_admin
#         token["is_author"] = user.is_author

#         return token


class AuthorsProfileSerializer(ModelSerializer):
    class Meta:
        model = AuthorsProfile
        fields = '__all__'



class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_admin']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         token["is_user"] = user.is_user
#         token["is_admin"] = user.is_admin
#         token["is_author"] = user.is_author

#         return token

class AdminProfileSerializer(ModelSerializer):
    class Meta:
        model = AdminProfile
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
