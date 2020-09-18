import pathlib
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

PEOPLE = 'people'


def get_resource(config, scopes, cache_dir: str):
    """Returns configured resource for connection to api
    """
    creds = None
    token_file = pathlib.Path(cache_dir) / 'token.pickle'

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if pathlib.Path(token_file).exists():
        with token_file.open('rb') as token:
            creds = pickle.load(token)

    if creds.scopes != scopes:
        creds = None

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(config, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with token_file.open('wb') as token:
            pickle.dump(creds, token)

    return build(PEOPLE, 'v1', credentials=creds)
