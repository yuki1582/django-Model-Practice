import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

print(Students.objects.all())

# 件数
# print(Students.objects.count())
# print(Students.objects.filter(name='太郎').count())

# 件数、最大値、最小値、平均値、合計
from django.db.models import Count, Max, Min, Avg, Sum
# print(Students.objects.aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')))
# aggreggate_students = Students.objects.aggregate(Count('pk'), Max('pk'), min_pk=Min('pk'), avg_pk=Avg('pk'), sum_age=Sum('age'))

# print(aggreggate_students['pk__avg'])
# print(Students.objects.aggregate(counted=Count('pk'), mix_pk=Max('pk'), min_pk=Min('pk'), avg_pk=Avg('pk'), sum_age=Sum('age')))
# print(Students.objects.aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')))

# GROUP BY:ある特定のカラムで集計して、合計、最大などを求める
print(Students.objects.values('name').annotate(
    Max('pk'), Min('pk')
))

print(Students.objects.values('name', 'age').annotate(
    Max('pk'), Min('pk')
))

for student in Students.objects.values('name', 'age').annotate(
    max_id=Max('pk'), min_id=Min('pk')
):
    print(student['max_id'])