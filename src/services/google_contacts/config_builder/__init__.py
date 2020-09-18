import json
import pathlib


def get_config(config_path, original_config):
    credentials_json = pathlib.Path(config_path) / 'credentials.json'

    if pathlib.Path(credentials_json).exists():
        with open(credentials_json, 'r') as json_file:
            return json.load(json_file)

    return {
        'installed':
            {
                'client_id': original_config.client_id,
                'client_secret': original_config.client_secret,
                'project_id': original_config.project_id,
                'auth_uri': original_config.auth_uri,
                'token_uri': original_config.token_uri,
                'auth_provider_x509_cert_url': original_config.auth_provider_x509_cert_url,
                'redirect_uris': original_config.redirect_uris,
            }
    }
