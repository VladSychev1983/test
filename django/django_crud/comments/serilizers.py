from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id','user','text','created_at']

    def validate_text(self, value):
        if 'text' in value:
            raise ValidationError('Вы использовали запрещенное слово!')
        return value
    
    #если нужно проверить валидировать данные user c id 2 или hello в тексте
    def validate(self, attrs):
        if 'hello' in attrs['text'] or attrs['user'].id == 2:
            raise ValidationError("Что-то пошло не так!")
        return super().validate(attrs)
    
    # если нужно переопределить объекты при создании или обновлении
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
