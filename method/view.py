from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Object import GDT_Object
from gdo.quote.GDO_Quote import GDO_Quote
from gdo.ui.GDT_Card import GDT_Card


class view(Method):

    @classmethod
    def gdo_trig(cls) -> str:
        return "qt"

    @classmethod
    def gdo_trigger(cls) -> str:
        return "quote"

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Object('id').table(GDO_Quote.table()).not_null().default_random(),
        ]

    def get_quote(self) -> GDO_Quote:
        return self.param_value('id')

    def gdo_execute(self) -> GDT:
        quote = self.get_quote()
        card = GDT_Card().gdo(quote).creator_header()
        card.get_content().add_field(
            quote.column('quote_text'),
            quote.column('quote_vote_count'),
            quote.column('quote_vote_score'),
        )
        return card
