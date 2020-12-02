import datetime
import glob
import os

from django.http import FileResponse
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from requesthandler.models import MapMetaData, MapFile
from requesthandler.serializers import MapMetaDataSerializer

EXTENSION = ".png"  # TODO CHANGE


@api_view(['GET', 'DELETE'])
def meta_list(request):
    if request.method == 'GET':
        metadata = MapMetaData.objects.using('metadata').all()
        title = request.GET.get('title', None)
        if title is not None:
            metadata = metadata.filter(title__icontains=title)
        metadata_serializer = MapMetaDataSerializer(metadata, many=True)
        return JsonResponse(metadata_serializer.data, safe=False)
    elif request.method == 'DELETE':
        files = glob.glob('files/*')  # Select all files in folder
        for f in files:
            os.remove(f)
        MapFile.objects.using('filestorage').all().delete()
        count = MapMetaData.objects.using('metadata').all().delete()
        if count[0] > 0:
            return JsonResponse({'message': '{} map(s) were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'There are already no maps.'},
                                status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def meta_by_pk(request, pk):
    try:
        meta = MapMetaData.objects.using('metadata').get(pk=pk)
        return single_entity_access(request.method, meta)
    except:
        return JsonResponse({'message': 'Map does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE'])
def meta_by_title(request, title):
    try:
        meta = MapMetaData.objects.using('metadata').get(title=title)
        return single_entity_access(request.method, meta)
    except:
        return JsonResponse({'message': 'Map does not exist'}, status=status.HTTP_404_NOT_FOUND)


def single_entity_access(requestMethod, meta):
    if requestMethod == 'GET':
        metadata_serializer = MapMetaDataSerializer(meta)
        return JsonResponse(metadata_serializer.data)
    elif requestMethod == 'DELETE':
        mapFileInstance = MapFile.objects.using('filestorage').get(pk=meta.mapStorageID)
        filepath = mapFileInstance.file.name
        os.remove(filepath)
        mapFileInstance.delete()
        meta.delete()
        return JsonResponse({'message': 'Map was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@parser_classes([FileUploadParser])
def upload(request, filename):
    f = request.data['file']
    newFile = MapFile.create(f)
    newFile.save(using='filestorage')
    print(f"new file with id:{newFile.id} and name:{newFile.file.name} saved.")

    filename = str(filename).split('.')[0]
    duration = request.query_params.get('duration')
    duration = datetime.datetime.strptime(duration, '%M:%S').time()
    difficulty = request.query_params.get('difficulty')
    newMeta = MapMetaData.create(filename, duration, difficulty, newFile.id)
    newMeta.save(using='metadata')

    return Response({'message': 'Map uploaded'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def download(request, pk):
    try:
        meta = MapMetaData.objects.using('metadata').get(mapStorageID=pk)
        meta.downloads += 1
        meta.save()
        mapFileInstance = MapFile.objects.using('filestorage').get(pk=pk)
        fileName = mapFileInstance.file
        return FileResponse(open(str(fileName), 'rb'))
    except:
        return JsonResponse({'message': 'Map does not exist'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def update_by_pk(request, pk):
    try:
        meta = MapMetaData.objects.using('metadata').get(pk=pk)
        success = request.query_params.get('success')
        success = str(success).lower() in ['true', '1', 't', 'yes']
        return update_meta(meta, success)
    except:
        return JsonResponse({'message': 'Map does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_by_title(request, title):
    try:
        meta = MapMetaData.objects.using('metadata').get(title=title)
        success = request.query_params.get('success')
        success = str(success).lower() in ['true', '1', 't', 'yes']
        return update_meta(meta, success)
    except:
        return JsonResponse({'message': 'Map does not exist'}, status=status.HTTP_404_NOT_FOUND)


def update_meta(metadata, success: bool):
    try:
        if success:
            metadata.successPlays += 1
        metadata.plays += 1
        metadata.save(using='metadata')
        metadata_serializer = MapMetaDataSerializer(metadata)
        return JsonResponse(metadata_serializer.data)
    except:
        return JsonResponse({'message': 'Update data failed'}, status=status.HTTP_404_NOT_FOUND)