from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status

from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
        "Get Profile" : "api/userprofile",
        "Get and Update User Profile" : "api/userprofile/update/id",

        'Change Password' : "api/change_password",
        'Forget Password Email Code' : "api/reset_password_email",
        'Forget Password' : "api/reset_password",


        'Notifications' : 'api/notifications',
        'Notifications Read' : 'api/notificationsread',




    # '===================== Author ======================== 
        "Getting Author" : "api/author",
        "Get, Update, Delete Author" : "api/author/id",
        "Get and Update Author Profile" : "api/authorprofile/update/id",

        # '===================== NEWS ======================== 

        "Get and Create News" : "api/news",
        "Get and Create NewsLetter" : "api/newsLetter",

        # '===================== STORY ======================== 
        'Get and Create Stories' : "api/stories",
        'Get, update, and delete a Story' : "api/story/update/id",
        'Get and Create MagazineStories' : "api/magazineStories",
        'Get update, and delete a Magazine Story' : "api/magazineStory/update/id",

        'Get and Create Magazines' : "api/magazines",
        'Get, Update and Magazines' : "api/magazine/update/id",

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
        # request.data._mutable = True
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
    return redirect('https://genz-square.vercel.app/login')



class UserGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def users_update(self, serializer):
        instance = serializer.save()



    def users_destroy(self, instance):
        return super().perform_destroy(instance)



class UserProfileGet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class UserProfileGetUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'

    def user_update(self, serializer):
        instance = serializer.save()
        


# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")

            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(new_password)
            self.object.save()
            return Response({"detail": "Password changed successfully."})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.core.mail import send_mail
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
import random



class ResetEmailView(generics.GenericAPIView):
    
    serializer_class = ResetPasswordEmailSerializer

    def post(self, request, *args, **kwargs, ):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = request.data.get('email')
        user = User.objects.get(email=email)

        code = random.randint(1000, 9999)
        # code = 123

        PasswordReset.objects.update_or_create(user=user, defaults={'code': code})


        if email:
            # Create and send the email
            if email and User.objects.filter(email=email).exists():

                subject = 'Confirm your email'
                message = f'This is your code: {code}'
                from_email = 'smtp.gmail.com'
                recipient_list = [email]
            
                send_mail(subject, message, from_email, recipient_list)

                return Response({'detail': 'Email sent successfully'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'detail': 'Email was not sent successfully'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']
        new_password = serializer.validated_data['new_password']

        # Validate the code and user
        user = User.objects.get(email=email)
        myUser = PasswordReset.objects.get(user = user)
        if myUser.code == code:
            # Update the user's password
            user.set_password(new_password)
            user.save()

            # Optionally, clear the password reset code
            user.code = None
            user.save()

            return Response({'detail': 'Password reset successfully.'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid code or user.'}, status=status.HTTP_400_BAD_REQUEST)
# class ResetPasswordView(generics.UpdateAPIView):
#     serializer_class = ResetPasswordSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self, queryset=None):
#         return self.request.user

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             old_password = serializer.data.get("old_password")
#             new_password = serializer.data.get("new_password")

#             if not self.object.check_password(old_password):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

#             self.object.set_password(new_password)
#             self.object.save()
#             return Response({"detail": "Password changed successfully."})

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========================= Authors ===========================
class AuthorGetCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        # request.data._mutable = True
        request.data['is_author'] = True

        email = request.data.get('email', None)

        # Check if a user with the given email already exists
        if email and User.objects.filter(email=email).exists():
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Author created successfully'}, status=status.HTTP_201_CREATED)
        
        else:
            # Registration failed, customize the error message
            error_message = {'message': 'Author registration failed. Please check the provided data.'}
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
# class MagazineGet(generics.ListAPIView):
#     queryset = Magazine.objects.all()
#     serializer_class = MagazineSerialiser


class NewsGet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body', 'category']

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
    search_fields = ['title', 'intro', 'body', 'category']

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
        
        
class StoryGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stories.objects.all()
    serializer_class = StorySerializer
    lookup_field = 'pk'

    def stories_update(self, serializer):
        instance = serializer.save()

    def stories_destroy(self, instance):
        return super().perform_destroy(instance)



class MagazineStoryGet(generics.ListCreateAPIView):

    queryset = MagazineStories.objects.all()
    serializer_class = MagazineStorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body', 'category']

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


class MagazineStoryGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MagazineStories.objects.all()
    serializer_class = MagazineStorySerializer
    lookup_field = 'pk'

    def stories_update(self, serializer):
        instance = serializer.save()

    def stories_destroy(self, instance):
        return super().perform_destroy(instance)
    


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
        
class NotificationReadGetCreate(generics.ListCreateAPIView):
    queryset = NotificationRead.objects.all()
    serializer_class = NotificationSerrializerRead
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Notification was created successfully'})
        else:
            error_message = {'message': 'Notification was not created successfully'}
            response.data = error_message
            return response
    


class MagazineGetCreate(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerialiser
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Magazine was created successfully'})
        else:
            error_message = {'message': 'Magazine was not created successfully'}
            response.data = error_message
            return response


class MagazineGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerialiser
    lookup_field = 'pk'

    def stories_update(self, serializer):
        instance = serializer.save()

    def stories_destroy(self, instance):
        return super().perform_destroy(instance)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




