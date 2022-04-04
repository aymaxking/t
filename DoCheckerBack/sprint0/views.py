from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

# Create your views here.
from sprint0.documents import ClientDocument, TypeDocument
from sprint0.serializers import ClientDocumentSerializer, TypeDocumentSerializer


class GetAllClientsView(DocumentViewSet):
    document = ClientDocument
    serializer_class = ClientDocumentSerializer
    filter_backends = [SearchFilterBackend]


class GetAllypesView(DocumentViewSet):
    document = TypeDocument
    serializer_class = TypeDocumentSerializer
    filter_backends = [SearchFilterBackend]
