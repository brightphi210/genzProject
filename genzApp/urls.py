

from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.enpoint, name="enpoint"),

    # ==================== User ==================================
    path('api/user', views.UserGetCreate.as_view(), name="api"),
    path('api/user/<str:pk>', views.UserGetUpdateDelete.as_view(), name="user_update"),

    path('api/userprofiles', views.UserProfileGet.as_view(), name="user_profile"),
    path('api/userprofile/update/<str:pk>', views.UserProfileGetUpdate.as_view(), name="user_profile_single"),

    path('api/change_password', views.ChangePasswordView.as_view(), name="change_password"),
    path('api/reset_password_email', views.ResetEmailView.as_view(), name="reset_password_email"),
    path('api/reset_password', views.PasswordResetView.as_view(), name="reset_password"),


    # ==================== Email Verify ==================================
    path('api/confirm-email/<int:user_id>/', views.confirm_email, name="confirm_email"),


    # ==================== Author ==================================
    path('api/author', views.AuthorGetCreate.as_view(), name="api"),
    path('api/author/<str:pk>', views.AuthorGetUpdateDelete.as_view(), name="user_update"),
    path('api/authorprofile/update/<str:pk>', views.AuthorProfileGetUpdate.as_view(), name="user_profile"),


    # ==================== Admin ==================================
    path('api/admin', views.AdminGetCreate.as_view(), name="api"),
    path('api/admin/<str:pk>', views.AdminGetUpdateDelete.as_view(), name="user_update"),
    path('api/adminprofile/update/<str:pk>', views.AdminProfileGetUpdate.as_view(), name="user_profile"),


    # =========================== NEWS ==============================
    path('api/newsLetter', views.NewsLetterView.as_view(), name="newsLetter"),

        # =========================== NEWS ==============================
    path('api/notifications', views.NotificationGetCreate.as_view(), name="notification"),
    path('api/notificationsread', views.NotificationReadGetCreate.as_view(), name="notificationread"),
    
    path('api/news', views.NewsGet.as_view(), name="news"),

    path('api/stories', views.StoryGet.as_view(), name="stories"),
    path('api/story/update/<str:pk>', views.StoryGetUpdateDelete.as_view(), name="stories"),

    path('api/magazineStories', views.MagazineStoryGet.as_view(), name="stories"),
    path('api/story/magazineStory/<str:pk>', views.MagazineStoryGetUpdateDelete.as_view(), name="stories"),

    path('api/magazines', views.MagazineGetCreate.as_view(), name="magazines"),
    path('api/magazine/update/<str:pk>', views.MagazineGetUpdateDelete.as_view(), name="magazine_update"),



    # ======================== subsribe =================================
    path('api/subMonthly', views.BasicSubscriptionPlanViewSet.as_view(), name="subBasic"),
    path('api/subYearly', views.BasicSubscriptionPlanViewSet.as_view(), name="subBasic"),
    path('api/subYealyPrint', views.BasicSubscriptionPlanViewSet.as_view(), name="subBasic"),
]

