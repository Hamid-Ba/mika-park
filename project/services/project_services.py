from project import models


class ProjectServices:
    """Service of Project"""

    def __init__(self) -> None:
        self.projects = models.Project.objects.all()

    def get_projects(self):
        return self.projects.order_by("-id")
