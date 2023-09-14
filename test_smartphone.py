import pytest
from smartphone import SmartPhone

class TestSmartPhone:

    @pytest.fixture
    def a_smartphone(self):
        return SmartPhone()

    def test_what_i_am(self, a_smartphone):
        assert a_smartphone.what_i_am() == 'a modern smartphone'

    def test_calling(self, a_smartphone, capsys):
        a_smartphone.calling()
        a_smartphone.handle_sms()
        a_smartphone.use_internet()
        captured = capsys.readouterr()
        assert captured.out == 'anrufen\nsms senden und empfangen\ndas Internet benutzen\n'