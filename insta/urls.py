import profile
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView, PostDeleteView, ProfileView, AddFollower,RemoveFollower,CommentCreateView

urlpatterns = [
    
    # path('',PostListView.as_view(), name='home'),
    path('',views.index, name='home'),
    path('profile/<int:pk>',ProfileView.as_view(),name = 'profile'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('user_registration/',views.register, name ='user_registration' ),
    path('accounts/login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('post/<int:pk>/comment/',CommentCreateView.as_view(), name='add_comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    

