from phone import Phone
from handy import Handy
from smartphone import SmartPhone


if __name__ == '__main__':
    phone = Phone()
    print('ich bin: ' + phone.what_i_am() + ' und kann')
    phone.calling()
    print('------------------')
    handy = Handy()
    print('ich bin: ' + handy.what_i_am() + ' und kann')
    handy.calling()
    handy.handle_sms()
    print('------------------')
    smart_phone = SmartPhone()
    print('ich bin: ' + smart_phone.what_i_am() + ' und kann')
    smart_phone.calling()
    smart_phone.handle_sms()
    smart_phone.use_internet()
    print('------------------')
