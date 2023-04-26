from django.core.management.base import BaseCommand
from core.models import Course, Module


class Command(BaseCommand):
    help = 'Load Courses and Modules'

    def handle(self, *args, **kwargs):
        Module.objects.all().delete()
        course_names = [
            'Computer Science', 'Mathematics'
        ]

        if not Course.objects.count():
            for course_name in course_names:
                    Course.objects.create(name=course_name)
        #CS
        cs = Course.objects.get(name='Computer Science')
        compsci_modules = [
             'AI',
             'Machine Learning',
             'Web Development',
             'Software Engineering',
             'NoSQL Databases'
        ]
        
        for module in compsci_modules:
             Module.objects.create(name=module, course=cs)
        
        #Maths
        math = Course.objects.get(name="Mathematics")
        math_modules = [
             'Linear Algebra',
             'Differential Equations',
             'Graph Theory',
             'Topology',
             'Number Theory'
        ]
        for module in math_modules:
             Module.objects.create(name=module, course=math)
        
        
        
        #Physics and so on



        