from django.contrib import admin
from .models import *
tables = [
    Univeristy,
    Achivement,
    WorkFlow,
    Service,
    Category,
    Levels,
    Courses,
    Lessons,
    CourseOutcomes,
    CoursesDetails,
    CourseInstructor,
    Statistics,
    Events,
    Testimonials,
    News,
    Subscribe,
    Gallery,
    FAQ,
    Contact,
    MemberShips,
    WhyUs,
]

for table in tables:
    admin.site.register(table)

