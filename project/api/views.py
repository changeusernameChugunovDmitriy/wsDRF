from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookGet(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return Response('Пост удален')

@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("No valid")
    return Response(serializer.data)

@api_view(['PUT'])
def bookPut(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(data=request.data, instance=book)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


