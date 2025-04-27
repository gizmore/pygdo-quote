from gdo.base.GDO import GDO
from gdo.vote.GDO_VoteTable import GDO_VoteTable
from gdo.vote.WithVotes import WithVotes


class WithQuoteVotes(WithVotes):

    def gdo_votes_table(self) -> GDO_VoteTable:
        from gdo.quote.GDO_QuoteVote import GDO_QuoteVote
        return GDO_QuoteVote.table()

    def gdo_vote_object_table(self) -> GDO:
        from gdo.quote.GDO_Quote import GDO_Quote
        return GDO_Quote.table()
