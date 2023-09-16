from rest_framework import serializers
from news.models import Article,Journalist,Profile,Comment
from datetime import date,datetime
from django.utils.timesince import timesince
from django.contrib.auth.models import User



class JournalistSerializer(serializers.ModelSerializer):
    articles=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='journalist-detail')
    class Meta:
        model=Journalist
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    time_since_pub=serializers.SerializerMethodField()
    # author=serializers.SerializerMethodField()
    # author=serializers.StringRelatedField()


    class Meta:
        model=Article
        fields='__all__'
        read_only_fields=['id','creation_date','last_updated_date']


    def get_time_since_pub(self,object):
        time_now=datetime.now()
        pub_date=object.publication_date
        if object.active:
            time_delta=timesince(pub_date,time_now)
            return time_delta
        else:
            return 'Not active'
    def validate_publication_date(self, pub_date):
        now=date.today()
        if pub_date>now:
            raise serializers.ValidationError('Publication date cannot be higher than now')
        else:
            return pub_date

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields='__all__'


class ProfilePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields=['image']

class CommentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=Comment
        fields='__all__'
        read_only_fields=['id','user','creation_date','last_updated_date','article']


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','password_confirmation')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match.")

        return data
    def validate_email(self, value):
        user=User.objects.filter(email=value)
        if user.exists():
            raise serializers.ValidationError('Email already exists')
        return value