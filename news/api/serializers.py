from rest_framework import serializers
from news.models import News,Journalist
from datetime import date
from django.utils.timesince import timesince

class NewsSerializer(serializers.ModelSerializer):
    time_since_pub=serializers.SerializerMethodField()
    class Meta:
        model=News
        fields='__all__'

    def get_time_since_pub(self,object):
        time_now=date.now()
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
        pass


class JournalistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=News
        fields='__all__'