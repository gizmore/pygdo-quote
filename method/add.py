from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.quote.GDO_Quote import GDO_Quote


class add(MethodForm):
    """
    Add a quote to the database.
    """

    @classmethod
    def gdo_trigger(cls) -> str:
        return "quote.add"

    def gdo_create_form(self, form: GDT_Form) -> None:
        table = GDO_Quote.table()
        text_c = table.column('quote_text')
        form.add_field(
            GDT_RestOfText('text').min(text_c._min).max(text_c._max).not_null(),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        quote = GDO_Quote.blank({
            'quote_text': self.param_value('text'),
        }).insert()
        return self.msg('msg_quote_added', (quote.get_id(), quote.get_vote_min(), quote.get_vote_max()))