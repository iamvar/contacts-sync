import transliterate
from dynaconf import settings
from text_unidecode import unidecode

import src.services.google_contacts.people_api.resource as api
from src.services.google_contacts.people_api import people
from src.services.google_contacts.config_builder import get_config

google_contacts_config = settings.get('google_contacts')
cache_dir = str(settings.get('app.cache_dir'))

api_config = get_config(
    settings.get('app.config_dir'),
    google_contacts_config
)

resource = api.get_resource(api_config, google_contacts_config.scopes, cache_dir)
rows = people.get_rows(resource)
for r in rows:
    name = r.get('name')
    name = unidecode(name)

