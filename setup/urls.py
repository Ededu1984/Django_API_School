from django.contrib import admin
from django.urls import path,include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, ListEnrollmentsStudent, ListStudentsEnrollments
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="school",
      default_version='v1',
      description="Store data from a school that provides courses in IT segment",
      terms_of_service="#",
      contact=openapi.Contact(email="edson.costa@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('student/<int:pk>/enrollments/', ListEnrollmentsStudent.as_view() ),
    path('course/<int:pk>/enrollments/', ListStudentsEnrollments.as_view() ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
