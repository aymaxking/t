from rest_framework import serializers

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from sprint0.documents import ClientDocument, TypeDocument


class ClientDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ClientDocument
        fields = [
            'fullname',
            'email',
            'phone'
        ]


class TypeDocumentSerializer(DocumentSerializer):
    class Meta:
        document = TypeDocument
        fields = [
            'title',
        ]
