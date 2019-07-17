import requests
import json


class Feed:
    def __init__(self, filter_func=None, call_limit=50, limit_per_call=275):
        """A wrapper object which loads user statuses by making api calls to the facebook-graph api"""
        self.curr_url = ''
        self.filter = filter_func  # data cleaning/processing function which will be applied to each status
        self.call_limit = call_limit  # maximum number of
        self.limit_per_call = limit_per_call  # maximum status limit to request per call
        self.raw_status = []  # list of fb statuses

    def load(self, token):
        """this method will access all data using token and load it as self.raw_status

            Args:
              token: A permission token generated at user login
            Returns:
              list of user statuses
              empty list when error occurred or uesr didn't have any status   
        """ 
        self.curr_url = f'https://graph.facebook.com/me?\
        fields=feed.limit({self.limit_per_call}) &access_token={token}'
        if self.__first_call():
            self.__load_all()
            return self.raw_status
        return []

    def __first_call(self):
        """this private method makes the first call for data, and loads the first data in self.raw_status
        returns True if there are more available pages to load, False otherwise
        """
        content = requests.get(self.curr_url)
        if content.ok:
            obj = json.loads(content.content)
            self.raw_status.extend(obj['feed']['data'])

            # if paging is absent, then we have reached last page so no need to load
            if not obj['feed'].get('paging'):
                return False

            self.curr_url = obj['feed']['paging']['next']
            return True

        # Todo throw custom error for failed connection
        return False

    def __load_all(self):
        """this private method should be called after __first_call method
        it recursively makes api calls to load statuses until
        either call limit is met or all data is loaded
        """
        content = requests.get(self.curr_url)
        i = 1   # already made first call
        while content.ok and i < self.call_limit:
            obj = json.loads(content.content)
            self.raw_status.extend(obj['data'])

            # if paging is absent, then we have reached last page
            if not obj.get('paging'):
                break

            # else continue
            self.curr_url = obj['paging']['next']
            content = requests.get(self.curr_url)
            i += 1
