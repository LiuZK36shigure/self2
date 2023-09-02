from django.shortcuts import render
from teachers.models import Teacher

def search_teacher_by_name(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teachers = Teacher.objects.filter(name=teacher_name)
        return render(request, 'results.html', {'teachers': teachers})
    return render(request, 'search.html')

def search_teacher_by_department(request):
    if request.method == 'POST':
        selected_departments = request.POST.getlist('departments')
        teachers = Teacher.objects.filter(department__in=selected_departments)
        return render(request, 'results.html', {'teachers': teachers})
    return render(request, 'search.html')