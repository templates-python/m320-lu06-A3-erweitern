import pytest
from handy import Handy

class TestHandy:

    @pytest.fixture
    def a_handy(self):
        return Handy()

    def test_what_i_am_handy(self, a_handy):
        assert a_handy.what_i_am() == 'an old handy'

    def test_function_handy(self, a_handy, capsys):
        a_handy.calling()
        a_handy.handle_sms()
        captured = capsys.readouterr()
        assert captured.out == 'anrufen\nsms senden und empfangen\n'