from rest_framework import response, status, generics, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from project import models, serializers, services
from project.services import project_services
from config import pagination

project_service = project_services.ProjectServices()


class ProjectViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Project View Set"""

    queryset = project_service.get_projects()
    serializer_class = serializers.ProjectListSerializer
    pagination_class = pagination.StandardPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["type"]