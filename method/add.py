from gdo.form.MethodForm import MethodForm


class add(MethodForm):

    def gdo_trigger(cls) -> str:
        return "quote.add"

    def gdo_trig(cls) -> str:
        return "+quote"
