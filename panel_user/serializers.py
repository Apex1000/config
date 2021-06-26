from rest_framework import serializers
from panel_user.models import PanelUserProfile

class ProfileFilterSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = PanelUserProfile
        fields = (
            'id',
            'username',
        )
    
    def get_username(self, obj):
        try:
            value = obj.user.username
        except:
            value = None
        return value

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    
    class Meta:
        model = PanelUserProfile
        fields = (
            'id',
            'username',
            'email',
            'user_type'
        )
    
    def get_username(self, obj):
        try:
            value = obj.user.username
        except:
            value = None
        return value

    def get_email(self, obj):
        try:
            value = obj.user.email
        except:
            value = None
        return value
    
    def get_user_type(self, obj):
        try:
            value = obj.user_type.name
        except:
            value = None
        return value