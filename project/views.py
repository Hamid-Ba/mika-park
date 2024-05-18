from rest_framework import response, status, generics, mixins, viewsets

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

    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = serializers.ProjectSerializer

        return self.serializer_class
