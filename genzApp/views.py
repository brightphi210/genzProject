from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status

from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets

from .models import *

from .serializer import *



from rest_framework.response import Response
from .models import *

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .signals import send_email_confirmation

@api_view(["GET"])
def enpoint(request):
    data = {
        "Enpoint" : "Api/",
        "Login" : "api/token",


        "Getting User" : "api/user",
        "Get, Update, Delete User" : "api/user/id",
        "Get and Update User Profile" : "api/userprofile/update/id",


        "Getting Author" : "api/author",
        "Get, Update, Delete Author" : "api/author/id",
        "Get and Update Author Profile" : "api/authorprofile/update/id",

        # '===================== NEWS ======================== 

        "Get and Create News" : "api/news",
        "Get and Create NewsLetter" : "api/newsLetter",

        # '===================== STORY ======================== 
        'Get and Create Stories' : "api/stories",
        'Get and Create MagazineStories' : "api/magazineStories",


        # ===================== SUB ===============================
        "Monthly Subscription" : "api/subMonthly",
        "Yearly Subscription" : "api/subYearly",
        "Yearly Print Subscription" : "api/subYealyPrint",
        

    }

    return Response(data)

class UserGetCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['is_user'] = True
        email = request.data.get('email', None)


        # Check if a user with the given email already exists
        if email and User.objects.filter(email=email).exists():

            user = User.objects.get(email=response.data['email'])

            send_email_confirmation(user.email)

            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Registration failed, customize the error message
            error_message = {'message': 'User registration failed. Please check the provided data.'}
            response.data = error_message
            return response
        

from django.shortcuts import render, redirect, get_object_or_404

def confirm_email(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    user.is_active= True
    user.save()
    return redirect('http://127.0.0.1:8000/api/token/')


class UserGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def users_update(self, serializer):
        instance = serializer.save()



    def users_destroy(self, instance):
        return super().perform_destroy(instance)

class UserProfileGetUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'

    def user_update(self, serializer):
        instance = serializer.save()


class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass    


# ========================= Authors ===========================
class AuthorGetCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['is_author'] = True

        email = request.data.get('email', None)

        # Check if a user with the given email already exists
        if email and User.objects.filter(email=email).exists():
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Registration failed, customize the error message
            error_message = {'message': 'User registration failed. Please check the provided data.'}
            response.data = error_message
            return response


class AuthorGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'

    def users_update(self, serializer):
        instance = serializer.save()


    def users_destroy(self, instance):
        return super().perform_destroy(instance)

class AuthorProfileGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = AuthorsProfile.objects.all()
    serializer_class = AuthorsProfileSerializer 
    lookup_field = 'pk'

    def user_update(self, serializer):
        instance = serializer.save()







# ========================= Admin ===========================
class AdminGetCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

    def create(self, request, *args, **kwargs):
        # request.data._mutable = True
        request.data['is_admin'] = True

        email = request.data.get('email', None)

        # Check if a user with the given email already exists
        if email and User.objects.filter(email=email).exists():
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Registration failed, customize the error message
            error_message = {'message': 'User registration failed. Please check the provided data.'}
            response.data = error_message
            return response


class AdminGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    lookup_field = 'pk'

    def users_update(self, serializer):
        instance = serializer.save()


    def users_destroy(self, instance):
        return super().perform_destroy(instance)

class AdminProfileGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = AuthorsProfile.objects.all()
    serializer_class = AdminProfileSerializer 
    lookup_field = 'pk'

    def user_update(self, serializer):
        instance = serializer.save()


# =================== News =======================
class MagazineGet(generics.ListAPIView):
    # queryset = Magazine.objects.all()
    pass


class NewsGet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'News created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'News creation failed. Please check the provided data.'}
            response.data = error_message
            return response


class StoryGet(generics.ListCreateAPIView):

    queryset = Stories.objects.all()
    serializer_class = StorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Story created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'Story creation failed. Please check the provided data.'}
            response.data = error_message
            return response
        


class MagazineStoryGet(generics.ListCreateAPIView):

    queryset = MagazineStories.objects.all()
    serializer_class = MagazineStorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Magazine Story created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'Magaznie Story creation failed. Please check the provided data.'}
            response.data = error_message
            return response



class NewsLetterView(generics.ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Subcription successfull'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'Subsription creation failed. Please check the provided data.'}
            response.data = error_message
            return response



class BasicSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Basic')
    serializer_class = SubscriptionPlanSerializer

class StandardSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Standard')
    serializer_class = SubscriptionPlanSerializer

class PremiumSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Premium')
    serializer_class = SubscriptionPlanSerializer



class NotificationGetCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerrializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Notification was created successfully'})
        else:
            error_message = {'message': 'Notification was not created successfully'}
            response.data = error_message
            return response
    



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer