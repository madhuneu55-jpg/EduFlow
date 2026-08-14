from rest_framework.serializers import ModelSerializer
from base.models import Room
from django.contrib.auth.models import User
from base.models import Message



class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
    
        fields = '__all__'
        

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
        
class createSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
class updateSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
class deleteserializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user