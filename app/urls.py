from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('listing/',views.listing,name='listing'),
    path('dashboard/' , views.dashboard, name='dashboard'),
    path('login/' , views.ulogin,name='ulogin'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.ulogout, name='ulogout'),
    path('userlist/',views.userlist,name='userlist'),
    path('<pk_id>/editlist/',views.editlist,name='editlist'),
    path('<pk_id>/deletelist/',views.deletelist,name='deletelist')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)