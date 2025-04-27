from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Text import GDT_Text
from gdo.date.GDT_Created import GDT_Created
from gdo.vote.GDT_VoteCount import GDT_VoteCount
from gdo.vote.GDT_VoteOutcome import GDT_VoteOutcome
from gdo.vote.WithVotes import WithVotes


class GDO_Quote(WithVotes, GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('quote_id'),
            GDT_Text('quote_text').minlen(4).maxlen(512).not_null(),
            GDT_Created('quote_created'),
            GDT_Creator('quote_creator'),
            GDT_VoteCount('quote_vote_count'),
            GDT_VoteOutcome('quote_vote_outcome'),
        ]
