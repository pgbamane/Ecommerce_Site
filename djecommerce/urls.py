from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users_app import views
from allauth.account.views import LoginView
# from allauth.socialaccount.views import S
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from allauth.socialaccount.providers.google.provider import GoogleProvider

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    path('', include('core.urls')),

    # User management
    # path('users_app/', include('users_app.urls')),
    path('accounts/signup/', views.SignupView.as_view(), name="account_signup"),
    path('accounts/login/', LoginView.as_view(), name="account_login"),
    path('accounts/', include(default_urlpatterns(GoogleProvider))),
    # path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
