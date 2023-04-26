from django.urls import path
from . import views

urlpatterns = [
    path('api/notes/', views.NoteList.as_view(), name="note_list_create"),
    path('api/notes/<int:pk>/', views.NoteDetail.as_view(), name="note_detail"),
    path('api/notes/download/', views.download_notes_csv, name='download_notes_csv'),
]
