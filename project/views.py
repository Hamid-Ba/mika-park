from rest_framework import mixins, viewsets, views, response, status
from django_filters.rest_framework import DjangoFilterBackend

from project import models, serializers
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

    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = serializers.BlockSerializer

        return self.serializer_class


class ChildChartView(views.APIView):
    """Child API View"""

    def get(self, request, block_id, main_id):
        if not models.ChildChart.objects.filter(main__block=block_id, main=main_id):
            return response.Response(
                {"message": "همجین نموداری وجود ندارد"},
                status=status.HTTP_404_NOT_FOUND,
            )

        childs = models.ChildChart.objects.filter(
            main__block=block_id, main=main_id
        ).all()

        childs_serial = serializers.ChildChartSerializer(instance=childs, many=True)

        return response.Response(childs_serial, status=status.HTTP_200_OK)
