from rest_framework import serializers
from requesthandler.models import MapFile, MapMetaData


class MapMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapMetaData
        fields = ('id',
                  'title',
                  'plays',
                  'successPlays',
                  'downloads',
                  'mapStorageID',
                  'duration',
                  'difficulty'
                  )

    def create(self, validated_data):
        instance = MapMetaData.objects.db_manager('metadata').create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        try:
            instance.title = validated_data.get('title', instance.title)
            instance.mapStorageID = validated_data.get('mapStorageID', instance.mapStorageID)
            instance.plays = validated_data.get('plays', instance.plays)
            instance.successPlays = validated_data.get('successPlays', instance.successPlays)
            instance.downloads = validated_data.get('downloads', instance.downloads)
            instance.id = validated_data.get('id', instance.id)
            instance.duration = validated_data.get('duration', instance.duration)
            instance.difficulty = validated_data.get('difficulty', instance.difficulty)
            instance.save(using='metadata')
        except Exception:
            instance.save(using='metadata')
            return instance
        return instance

