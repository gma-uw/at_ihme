import time
from cascade_at.core.db import db_tools as ihme_db_tools
from cascade_at.core.db import db_queries as ihme_db_queries

from cascade_at.core.log import get_loggers

LOG = get_loggers(__name__)

SQL_query_count = 3


class Timer:    
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

def after(i, ex):
    if 'lost connection' in str(ex).lower():
        if i < SQL_query_count-1:
            LOG.warning(f'Query attempt #{i} failed: {str(ex)}')
        else:
            LOG.error(f'Out of query attempts.')
            raise
def fmt(args, kwds):
    msg = ''
    if args:
        msg = f'args: {args}'
    if kwds:
        if args:
            msg += ', '
        msg += f'kwds: {kwds}'
    return msg

class _db_tools:
    def DBConfig(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.configDBConfig(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.DBConfig ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def exec_query(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.query_tools.exec_query(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.query_tools.exec_query ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def query(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.ezfuncs.query(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.ezfuncs.query ({fmt(args, kwds)}) took %.03f sec.' % t.interval)


    def get_outputs(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.get_outputs(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.get_outputs ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_session(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.ezfuncs.get_session(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.ezfuncs.get_session ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def Infiles(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.loaders.Infiles(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.loaders.Infiles ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def Inserts(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_tools.loaders.Inserts(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_tools.loaders.Inserts ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

class _db_queries:
    # def __init__(self, *args, **kwds):
    #     return super(db_queries, self).__init__(*args, **kwds)

    def get_age_metadata(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_age_metadata(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_queries.get_age_metadata ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_covariate_estimates(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_covariate_estimates(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_queries.get_covariate_estimates ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_demographics(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_demographics(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_queries.get_demographics ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_envelope(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_envelope(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_queries.get_envelope ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_ids(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_ids(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_queries.get_ids ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_location_metadata(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_location_metadata(*args, **kwds)
            except Exception as ex:
                after(i, ex)
            finally:
                print(f'db_queries.get_location_metadata ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

    def get_population(self, *args, **kwds):
        for i in range(SQL_query_count):
            try:
                with Timer() as t:
                    return ihme_db_queries.get_population(*args, **kwds)
            except Exception as ex:
                after(i, ex) 
            finally:
                print(f'db_queries.get_population ({fmt(args, kwds)}) took %.03f sec.' % t.interval)

db_tools = _db_tools()
db_queries = _db_queries()

if __name__ == '__main__':
    demographics = db_queries.get_demographics(gbd_team='epi', gbd_round_id=3)
    print (demographics)
