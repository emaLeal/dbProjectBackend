from rest_framework import serializers
from .models import Classes, Material, Attendance

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = [
            'class_name',
            'room',
            'schedule',
            'date',
            'course_id'
        ]
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = [
            'file_name',
            'file_path',
            'file_type',
            'class_id'
        ]
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'student_code',
            'status',
            'hour',
            'location',
            'class_id'
        ]
