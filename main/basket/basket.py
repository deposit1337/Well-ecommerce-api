class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, item, qty):
        item_id = item.id
        if item_id not in self.basket:
            self.basket[item_id] = {'price': item.price, 'qty': qty}

        self.session.pop('_auth_user_id', None)
        self.session.pop('_auth_user_backend', None)
        self.session.pop('_auth_user_hash', None)

        self.session.modified = True

    def __len__(self):
        '''
        Get basket data and count qty of items
        '''
        return sum(item['qty'] for item in self.basket.values())
