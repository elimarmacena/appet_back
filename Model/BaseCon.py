import os
from peewee import *

class BaseCon(Model):
    class Meta:
        database = PostgresqlDatabase(database='eqvhegcr', user='eqvhegcr', password='uOr1RvzMuCvjqpnSPqvadvOnBwZP5oNd', host='motty.db.elephantsql.com', port='5432')
