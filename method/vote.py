from gdo.vote.GDO_VoteTable import GDO_VoteTable
from gdo.vote.MethodVote import MethodVote


class vote(MethodVote):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'quoteup'

    def gdo_vote_table(self) -> GDO_VoteTable:
        return GDO_VoteTable.table()
