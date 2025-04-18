from gdo.vote.GDO_VoteTable import GDO_VoteTable


class GDO_QuoteVote(GDO_VoteTable):

    def gdo_vote_table(self) -> GDO_VoteTable:
        return GDO_Quote.table()
