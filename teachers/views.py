from django.shortcuts import render
from teachers.models import Teacher

def search_teacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher = Teacher.objects.filter(name=teacher_name).first()
        return render(request, 'teachers/teacher_result.html', {'teacher': teacher})
    return render(request, 'teachers/search_teacher.html')

def search_department(request):
    if request.method == 'POST':
        departments = request.POST.getlist('departments')
        teachers = Teacher.objects.filter(department__in=departments)
        return render(request, 'teachers/department_result.html', {'teachers': teachers})
    return render(request, 'teachers/search_department.html')
