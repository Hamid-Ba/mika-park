from project import models


class BlockServices:
    """Service of Block"""

    def __init__(self) -> None:
        self.blocks = models.Block.objects.all()

    def get_blocks(self):
        return self.blocks.order_by("-id")
