from django.conf import settings


class Favorites:
    def __init__(self, request):
        self.session = request.session
        favorites = self.session.get(settings.FAVORITES_SESSION_ID)
        if not favorites:
            favorites = self.session[settings.FAVORITES_SESSION_ID] = []
        self.favorites = favorites

    def add(self, product_id):
        if not self.session.get('favorites'):
            self.session['favorites'] = list()
        else:
            self.session['favorites'] = list(self.session['favorites'])
        if product_id not in self.session['favorites']:
            self.session['favorites'].append(product_id)

    def remove(self, product_id):
        for item in self.session['favorites']:
            if item == product_id:
                self.session['favorites'].remove(item)

        while [] in self.session['favorites']:
            self.session['favorites'].remove([])

        if not self.session['favorites']:
            del self.session['favorites']

        self.session.modified = True

    def delete(self):
        if self.session.get('favorites'):
            del self.session['favorites']
