class Phone:
    '''
      Stellt ein einfaches, altes Telefon dar, mit dem man nur anrufen kann.
      '''

    def __init__(self):
        pass

    def calling(self):
        print('anrufen')

    def what_i_am(self):
        return('a simply phone')


#Test
if __name__ == '__main__':
    p = Phone()
    print(p.what_i_am())
    p.calling()