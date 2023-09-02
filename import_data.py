import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "query_system.settings")
django.setup()

from teachers.models import Teacher

def import_teachers_data():
    # 在这里编写读取数据文件和导入数据的逻辑
    with open('teachers_data.txt', 'r') as f:
        lines = f.readlines()
        teachers = []
        for line in lines:
            data = line.strip().split(',')
            department = data[0]
            name = data[1]
            title = data[2]
            photo = data[3]
            teacher = Teacher(department=department, name=name, title=title, photo=photo)
            teachers.append(teacher)
        
        Teacher.objects.bulk_create(teachers)