from .mixins import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin


class CRUD(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    def __init__(self) -> None:
        super().__init__()