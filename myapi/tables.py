import django_tables2 as tables
from django_tables2 import SingleTableView
from .models import ChildGrantDate

class ChildGrantDateTable(tables.Table):
    class Meta:
        model = ChildGrantDate
