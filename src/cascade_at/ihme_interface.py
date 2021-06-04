from cascade_at.core.db import db_tools as ihme_db_tools
from cascade_at.core.db import db_queries as ihme_db_queries

from cascade_at.core.log import get_loggers

LOG = get_loggers(__name__)

SQL_query_count = 3

def after(i, ex):
    if 'lost connection' in str(ex).lower():
        if i < SQL_query_count-1:
            LOG.warning(f'Query attempt #{i} failed: {str(ex)}')
        else:
            LOG.error(f'Out of query attempts.')
            raise

class _db_tools:
    def DBConfig(*args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_tools.configDBConfig(*args, **kwds)
            except Exception as ex:
                after(i, ex)
        

    def exec_query(*args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_tools.query_tools.exec_query(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def exec(*args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_tools.ezfuncs.query(*args, **kwds)
            except Exception as ex:
                after(i, ex)

class _db_queries:
    # def __init__(self, *args, **kwds):
    #     return super(db_queries, self).__init__(*args, **kwds)

    def get_age_metadata(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_age_metadata(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def get_covariate_estimates(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_covariate_estimates(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def get_demographics(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_demographics(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def get_envelope(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_envelope(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def get_ids(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_ids(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def get_location_metadata(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_location_metadata(*args, **kwds)
            except Exception as ex:
                after(i, ex)

    def get_population(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                return ihme_db_queries.get_population(*args, **kwds)
            except Exception as ex:
                after(i, ex) 

db_tools = _db_tools()
db_queries = _db_queries()

if __name__ == '__main__':
    demographics = db_queries.get_demographics(gbd_team='epi', gbd_round_id=3)
    print (demographics)
