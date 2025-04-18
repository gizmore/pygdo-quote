from gdo.base.GDO_Module import GDO_Module


class module_quote(GDO_Module):

    def gdo_dependencies(self) -> list:
        return [
            'vote',
        ]

    def gdo_classes(self):
        return [

        ]
