import requests


def get_user(token):
    """this function returns username and id if given token is valid, None otherwise

        Args:
            token: A permission token generated at user login
        Returns:

            returns dict containing name and id values if token is valid then 
            else None
    """ 
    url = f'https://graph.facebook.com/me?access_token={token}'
    response = requests.get(url)
    if response.ok:
        return response.json()
    return None

