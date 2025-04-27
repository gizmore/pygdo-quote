from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Object import GDT_Object
from gdo.message.GDT_Paragraph import GDT_Paragraph
from gdo.quote.GDO_Quote import GDO_Quote
from gdo.ui.GDT_Card import GDT_Card


class view(Method):

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Object('id').table(GDO_Quote.table()).not_null().default_random(),
        ]

    def get_quote(self) -> GDO_Quote:
        return self.param_value('id')

    def gdo_execute(self) -> GDT:
        quote = self.get_quote()
        card = GDT_Card().gdo(quote).creator_header()
        card.get_content().add_field(
            quote.column('quote_text')
        )
        return card
