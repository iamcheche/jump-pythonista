# -*- coding: utf-8 -*-

SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/khim/Desktop/hov2/final/records.db'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
PUBLIC_METHODS = ['POST']

DEBUG = True

DOMAIN = {
    'membercode': {
        'item_title':'membership_codes',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE']
        # 'item_resource': ['GET', 'PUT', 'PATCH', 'DELETE']
    },

    'users' : {
	'item_title':'user',
	'additional_lookup': {
		'url':'[0-9]+',
		'field':'_id'
	},
	'cache_control':'max-age=10, must-revalidate',
	'cache_expires': 10,
	'resource_methods':['GET', 'POST', 'DELETE'],
	'item_methods': ['GET', 'PUT','PATCH', 'DELETE']
    },

    'preregistration': {
        'item_title':'preregi',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH','DELETE']
    },

    'questions': {
        'item_title':'question',
        'additional_lookup': {
            'url': '[0-9]+',
            'field': '_id'
        },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH','DELETE']
    }
}
