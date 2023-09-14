from phone import Phone

class Handy(Phone):

    def __init__(self):
        pass

    def handle_sms(self):
        print('sms senden und empfangen')

    def what_i_am(self):
        return('an old handy')

#Test
if __name__ == '__main__':
    h = Handy()
    print(h.what_i_am())
    h.calling()
    h.handle_sms()