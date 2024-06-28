from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from project import serializers
from project.services import project_services, block_services
from config import pagination

project_service = project_services.ProjectServices()
block_service = block_services.BlockServices()


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

    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = serializers.ProjectSerializer

        return self.serializer_class


class BlockViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Block View Set"""

    queryset = block_service.get_blocks()
    serializer_class = serializers.BlockListSerializer
