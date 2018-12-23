# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
#         'URL': 'http://127.0.0.1:9200/',
#         'INDEX_NAME': 'haystack',
#     },
# }

from django.conf import settings
from requests_aws4auth import AWS4Auth
awsauth = AWS4Auth(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY,'us-east-1','es')


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'https://search-advo-search-tdbbozoee2qmgiowsicqdjyfze.us-east-1.es.amazonaws.com',
        'INDEX_NAME': 'haystack',
        'KWARGS': {
            'port': 443,
            'http_auth': awsauth,
            'use_ssl': True,
            'verify_certs': True,
            'connection_class': elasticsearch.RequestsHttpConnection
        },

    },
}
