from peewee import *

db = SqliteDatabase('ecg_table.db')


class ECG(Model):
    patient_name = TextField()
    graph_x = CharField()
    graph_y = CharField()
    pulse = IntegerField()

    class Meta:
        database = db
