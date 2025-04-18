import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdotest.TestUtil import reinstall_module, GDOTestCase, cli_plug, cli_gizmore


class QuoteTestCase(GDOTestCase):

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        reinstall_module('quote')
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()
        Application.init_cli()

    def test_01_cli_quote(self):
        giz = cli_gizmore()
        out = cli_plug(giz, '$quote.add giz|work{3}: Code you see is code in use.')
        self.assertIn('created', out, "Quote was not created.")
        out = cli_plug(giz, '$quote.vote --score=3 1')
        self.assertIn('registered', out, "Quote was not voted.")
