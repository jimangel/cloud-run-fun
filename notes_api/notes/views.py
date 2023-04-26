from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from .csvresponse import CSVResponse

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def download_notes_csv(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    data = serializer.data

    response = CSVResponse(data=data)
    response['Content-Disposition'] = 'attachment; filename="notes.csv"'
    return response
