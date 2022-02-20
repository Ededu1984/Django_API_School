from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrollmentsStudentSerializer, ListStudentsEnrollmentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """Showing all enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class ListEnrollmentsStudent(generics.ListAPIView):
    """Showing the enrollments of the students"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentsStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListStudentsEnrollments(generics.ListAPIView):
    """Showing the enrollments in a course"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course=self.kwargs['pk'])
        return queryset
 
    serializer_class = ListStudentsEnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


