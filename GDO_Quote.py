from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Render import Mode
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Text import GDT_Text
from gdo.date.GDT_Created import GDT_Created
from gdo.date.Time import Time
from gdo.quote.WithQuoteVotes import WithQuoteVotes
from gdo.ui.GDT_Card import GDT_Card
from gdo.vote.GDT_VoteCount import GDT_VoteCount
from gdo.vote.GDT_VoteOutcome import GDT_VoteOutcome


class GDO_Quote(WithQuoteVotes, GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('quote_id'),
            GDT_Text('quote_text').minlen(4).maxlen(512).not_null(),
            GDT_Created('quote_created').date_format(Time.FMT_DAY),
            GDT_Creator('quote_creator'),
            GDT_VoteCount('quote_vote_count'),
            GDT_VoteOutcome('quote_vote_score'),
        ]

    def get_user(self) -> GDO_User:
        return self.gdo_value('quote_creator')

    def render(self, mode: Mode = Mode.render_html):
        card = GDT_Card().gdo(self)
        card.creator_header()
        card.get_content().add_fields(
            self.column('quote_text'),
            self.column('quote_vote_count'),
            self.column('quote_vote_score'),
        )
        return card.render(mode)
