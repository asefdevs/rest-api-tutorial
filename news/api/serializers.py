from rest_framework import serializers
from news.models import Article,Journalist
from datetime import date,datetime
from django.utils.timesince import timesince



class JournalistSerializer(serializers.ModelSerializer):
    articles=serializers.StringRelatedField(many=True,read_only=True)
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
