from django.shortcuts import render, redirect, get_object_or_404
from django.db import models 
from .models import Student, Score
from .forms import StudentForm, ScoreForm

# 学生一覧
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

# 学生登録
def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})

# 得点入力
def add_score(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.student = student
            score.save()
            return redirect('view_scores', student_id=student.id)
    else:
        form = ScoreForm()
    return render(request, 'add_score.html', {'form': form, 'student': student})


# 得点削除
def delete_score(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    student_id = score.student.id  # 削除後に元の学生ページにリダイレクトするために学生IDを取得
    score.delete()
    return redirect('view_scores', student_id=student_id)

# 学生の得点確認
def view_scores(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    scores = student.scores.all()
    return render(request, 'view_scores.html', {'student': student, 'scores': scores})

# 科目ごとの得点確認
def subject_scores(request):
    subjects = Score.objects.values('subject').distinct()
    subject_scores = {}
    for subject in subjects:
        subject_name = subject['subject']
        avg_score = Score.objects.filter(subject=subject_name).aggregate(models.Avg('score'))['score__avg']
        subject_scores[subject_name] = avg_score
    return render(request, 'subject_scores.html', {'subject_scores': subject_scores})
