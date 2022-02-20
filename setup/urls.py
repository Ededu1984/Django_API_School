from django.contrib import admin
from django.urls import path,include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, ListEnrollmentsStudent, ListStudentsEnrollments
from rest_framework import routers
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')


urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    # Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Other endpoints
    path('', include(router.urls) ),
    path('student/<int:pk>/enrollments/', ListEnrollmentsStudent.as_view() ),
    path('course/<int:pk>/enrollments/', ListStudentsEnrollments.as_view() ),
    # Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
