import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdotest.TestUtil import reinstall_module, GDOTestCase, cli_plug, cli_gizmore


class QuoteTestCase(GDOTestCase):

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        Application.init_cli()
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        reinstall_module('quote')
        loader.init_cli()

    def test_01_cli_quote(self):
        giz = cli_gizmore()
        out = cli_plug(giz, '$qtadd <@gizmore>: Code you see is code in use.')
        self.assertIn('has been added', out, "Quote was not created.")
        out = cli_plug(giz, '$qtup --score=3 1')
        self.assertIn('registered', out, "Quote was not voted.")
        self.assertIn('3.0', out, "Quote was not voted.")
        out = cli_plug(giz, '$qts code see')
        self.assertIn('code in use', out, "Quote was not found with $qts.")
        self.assertIn('3.0', out, "Quote score was not found with $qts.")
        out = cli_plug(giz, '$qt 1')
        self.assertIn('code in use', out, "Quote was not found with $qt.")
        self.assertIn('3.0', out, "Quote score was not found with $qt.")
