import pytest
from phone import Phone

class TestPhone:

    @pytest.fixture
    def a_phone(self):
        return Phone()

    def test_what_i_am(self, a_phone):
        assert a_phone.what_i_am() == 'a simply phone'

    def test_calling(self, a_phone, capsys):
        a_phone.calling()
        captured = capsys.readouterr()
        assert captured.out == 'anrufen\n'