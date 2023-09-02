import csv
import os
from django.core.management.base import BaseCommand
from teachers.models import Teacher

class Command(BaseCommand):
    help = 'Load teachers data from CSV file'
    def handle(self, *args, **options):
        csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'teachers_data.csv')

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                department, name, title, photo = row
                teacher = Teacher(department=department, name=name, title=title, photo=photo)
                teacher.save()

        self.stdout.write(self.style.SUCCESS('Teachers data loaded successfully'))