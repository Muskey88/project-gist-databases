from .models import Gist

def op_to_use(op):
    return {
        'gt': '>',
        'gte': '>=',
        'lt': '<',
        'lte': '<=',
    }[op]

def search_gists(db_connection, **kwargs):
    basic = 'SELECT * FROM gists'
    results = []
    filters = []
    params = {}
    if kwargs:
        for name, value in kwargs.items():
            if 'created_at' in kwargs and '__' not in kwargs:
                filters.append('datetime(%s) == datetime(:%s)' % (name, name))
                params[name] = value

            elif '__' in name:
                att, operator = name.split('__')
                params[att] = value
                op = op_to_use(operator)
                filters.append('datetime(%s) %s datetime(:%s)' % (att, op, att))

            else:
                filters.append('%s = :%s' % (name, name))
                params[name] = value

        basic +=' WHERE '
        basic += ' AND '.join(filters)
        cursor = db_connection.execute(basic, params)
    else:
        cursor = db_connection.execute(basic)
    
    for gist in cursor:
        results.append(Gist(gist))
        
    return results