
def get_rows(resource):

    # Call the People API
    results = resource.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields='names,emailAddresses,birthdays,events').execute()
    connections = results.get('connections', [])

    for person in connections:
        names = person.get('names', [])
        if not names:
            continue

        name = names[0].get('displayName')

        db = None
        dbs = person.get('birthdays', [])
        if dbs:
            db = dbs[0].get('date')

        yield {'name': name, 'db': db}

