from django.urls import path
from scores import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('add_score/<int:student_id>/', views.add_score, name='add_score'),
    path('view_scores/<int:student_id>/', views.view_scores, name='view_scores'),
    path('subject_scores/', views.subject_scores, name='subject_scores'),
    path('delete_score/<int:score_id>/', views.delete_score, name='delete_score'),  # 削除URLを追加
]
