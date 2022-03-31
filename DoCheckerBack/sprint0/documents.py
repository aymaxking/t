from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from sprint0.models import Client, Type


@registry.register_document
class ClientDocument(Document):
    class Index:
        name = 'clients'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Client
        fields = [
            'fullname', 'email', 'phone'
        ]


@registry.register_document
class TypeDocument(Document):
    class Index:
        name = 'types'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Type
        fields = [
            'title'
        ]
