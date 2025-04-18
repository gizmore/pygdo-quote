from gdo.base.GDO import GDO
from gdo.base.Render import Mode
from gdo.quote.GDO_Quote import GDO_Quote
from gdo.table.MethodQueryTable import MethodQueryTable


class quotes(MethodQueryTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'quotes'

    def gdo_searched(self) -> bool:
        return True

    def gdo_table(self) -> GDO:
        return GDO_Quote.table()

    def render_gdo(self, gdo: GDO, mode: Mode) -> any:
        return 'X'
