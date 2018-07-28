from enum import Enum, unique


@unique
class Role(Enum):
    ADMIN = "ADMIN"
    PUBLISHER = "PUBLISHER"
    USER = "USER"

    @classmethod
    def get_enum_labels(cls):
        return [i.value for i in cls]


role_dict = {"ADMIN": Role.ADMIN, "PUBLISHER": Role.PUBLISHER, "USER": Role.USER}
