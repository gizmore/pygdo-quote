from gdo.base.GDO import GDO
from gdo.vote.GDO_VoteTable import GDO_VoteTable


class GDO_QuoteVote(GDO_VoteTable):

    def gdo_votes_table(self) -> GDO_VoteTable:
        return self.table()

    def gdo_vote_object_table(self) -> GDO:
        from gdo.quote.GDO_Quote import GDO_Quote
        return GDO_Quote.table()
