from rest_framework import serializers
from .models import User, Specialization, Skill

    
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__' 


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    specializations = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(),
        many=True,
        required=False
    )
    skills = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        required=False
    )
    class Meta:
        model = User
        ref_name = 'CustomUser'
        fields = (
            'id', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number', 'city', 'sex', 'birth_date',
            'grade', 'work_experience', 'is_devrel', 'password', 'specializations', 'skills'
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        specializations = validated_data.pop('specializations', [])
        skills = validated_data.pop('skills', [])

        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        
        instance.specializations.set(specializations)
        instance.skills.set(skills)

        return instance