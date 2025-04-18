from gdo.form.MethodForm import MethodForm


class add(MethodForm):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "quote.add"
