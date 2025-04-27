from gdo.base.GDO_Module import GDO_Module
from gdo.quote.GDO_Quote import GDO_Quote
from gdo.quote.GDO_QuoteVote import GDO_QuoteVote


class module_quote(GDO_Module):

    def gdo_dependencies(self) -> list:
        return [
            'vote',
        ]

    def gdo_classes(self):
        return [
            GDO_Quote,
            GDO_QuoteVote,
        ]
