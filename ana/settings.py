SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/Ana Rose Trajano/Desktop/a/Store/mystore.db'
DEBUG = True
 
DOMAIN = {
    'users': {
        'item_title': 'user',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods':['GET','PUT', 'PATCH','DELETE']
    },

    'stores': {
        'item_title': 'store',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods':['GET','PUT', 'PATCH','DELETE']
    },

    'mystores': {
        'item_title': 'mystore',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods':['GET','PUT', 'PATCH','DELETE']
    },

     'healthadvisors': {
        'item_title': 'healthadvisor',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods':['GET','PUT', 'PATCH','DELETE']
    }
}