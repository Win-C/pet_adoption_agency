import requests

GET_TOKEN_URL = https://api.petfinder.com/v2/oauth2/token
ANIMAL_LIST_URL = https://api.petfinder.com/v2/animals?limit=100


def get_oauth_token(api_key, api_secret):
    """ Use API Key and Secret to authenticate with the api to 
        get an Oauth token. 
        Takes in: API key and API secret for client credentials
        Return: token_type and access_token as a list of strings
        """

    resp = requests.post(
        GET_TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": api_key,
            "client_secret": api_secret
        }
    )

    # Need a way to handle errors if request fails!

    access_token = resp.json()['access_token']

    return access_token


def get_pet_list(access_token):
    """ Using token_type and access_token, get a list of pets
        from the Petfinder API.
        Return:
        """

    animal_list = requests.get(
        ANIMAL_LIST_URL, 
        headers={'Authorization': f"Bearer {access_token}"}
    )

    # Need a way to handle errors if request fails!
    # TBU

    return animal_list


def get_random_pet():
    """ Get a random pet. """

    # TBU
