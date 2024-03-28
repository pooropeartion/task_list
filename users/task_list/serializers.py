from rest_framework import serializers
from .models import Task
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model
User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
#   password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('email', 'user_name', 'password')
    extra_kwargs = {
      'user_name': {'required': False}
    }
  def create(self, validated_data):
    user = User.objects.create(
      user_name=validated_data['user_name'],
      email=validated_data['email'],
      # first_name=validated_data['first_name'],
      # last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class Post_list(serializers.ModelSerializer):
    class Meta:
      model = Task
      fields = ['title', 'description', 'priority']
