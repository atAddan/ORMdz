import os
import django
from django.db.models import Q
from company.models import Sotr

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORMdz.settings")
django.setup()
# 1. Получи количество сотрудников с должностью “Менеджер”
query_1 = Sotr.objects.filter(doljnost="Менеджер").count()

# 2. Получи список сотрудников, работающих на четвертых этажах
query_2 = Sotr.objects.filter(otdel__flor=4).values_list("full_name", flat=True)

# 3. Получи список всех сотрудников, работающих в этих двух филиалах, с помощью Q
filial_ids = [1, 2]
query_3 = Sotr.objects.filter(
    Q(otdel__filial_id=filial_ids[0]) | Q(otdel__filial_id=filial_ids[1])
).values_list("full_name", flat=True)

# 4. Получи список сотрудников, работающих в тех же двух филиалах из прошлого вопроса, только вместо Q используй лукап, проверяющий вхождение ID в список
query_4 = Sotr.objects.filter(otdel__filial_id__in=filial_ids).values_list(
    "full_name", flat=True
)

# 5. Получи список ФИО сотрудников, у которых не указан email
query_5 = (
    Sotr.objects.filter(email__isnull=True)
    .values_list("full_name", flat=True)
    .values_list("full_name", flat=True)
)

# 6. Получи список сотрудников, чей год рождения 1990.
query_6 = Sotr.objects.filter(data__year=1990).values_list("full_name", flat=True)

# Для проверки в консоли (уберите, если нужно просто определения запросов)
print(f"Query 1: {query_1}")
print(f"Query 2: {query_2}")
print(f"Query 3: {query_3}")
print(f"Query 4: {query_4}")
print(f"Query 5: {query_5}")
print(f"Query 6: {query_6}")