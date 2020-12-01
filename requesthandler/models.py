from django.db import models


# from gridfs_storage.storage import GridFSStorage


class MapMetaData(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    plays = models.IntegerField(blank=False, default=0)
    successPlays = models.IntegerField(blank=False, default=0)
    downloads = models.IntegerField(blank=False, default=0)
    mapStorageID = models.IntegerField(blank=False, default=0)
    duration = models.TimeField(blank=False, auto_now=False)
    difficulty = models.IntegerField(blank=False, default=0)

    @classmethod
    def create(cls, title, duration, difficulty, mapStorageID):
        metadataObj = cls(title=title, duration=duration, difficulty=difficulty, mapStorageID=mapStorageID)
        return metadataObj

class MapFile(models.Model):
    file = models.FileField(upload_to="files/")

    @classmethod
    def create(cls, file):
        fileObj = cls(file=file)
        return fileObj
