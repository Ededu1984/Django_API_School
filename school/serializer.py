from rest_framework import serializers
from school.models import Student, Course, Enrollment
from school.validators import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'rg', 'cpf', 'birth_date', 'cell_phone', 'status']

    def validate(self, data):
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError("The CPF must have 11 digits")
        if not valid_name(data['name']):
            raise serializers.ValidationError("Don't include numbers in this field")
        if not valid_rg(data['rg']):
            raise serializers.ValidationError("The RG must have 9 digits")
        return data

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []

class ListEnrollmentsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'period']
    def get_period(self, obj):
        return obj.get_period_display()

class ListStudentsEnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']