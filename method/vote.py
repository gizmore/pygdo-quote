from gdo.base.GDO import GDO
from gdo.quote.GDO_Quote import GDO_Quote
from gdo.quote.GDO_QuoteVote import GDO_QuoteVote
from gdo.vote.GDO_VoteTable import GDO_VoteTable
from gdo.vote.MethodVote import MethodVote


class vote(MethodVote):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'quote.up'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'qtup'

    def gdo_votes_table(self) -> GDO_VoteTable:
        return GDO_QuoteVote.table()

    def gdo_vote_object_table(self) -> GDO:
        return GDO_Quote.table()
