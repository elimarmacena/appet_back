import os
from peewee import *

class BaseCon(Model):
    class Meta:
        database = None
        if 'HEROKU' in os.environ:
            import urlparse, psycopg2
            urlparse.uses_netloc.append('postgres')
            url = urlparse.urlparse(os.environ["postgres://eqvhegcr:uOr1RvzMuCvjqpnSPqvadvOnBwZP5oNd@motty.db.elephantsql.com:5432/eqvhegcr"])
            db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
        else:
            database = PostgresqlDatabase('eqvhegcr',user='eqvhegcr',password='uOr1RvzMuCvjqpnSPqvadvOnBwZP5oNd',host='motty.db.elephantsql.com', port=5432)
