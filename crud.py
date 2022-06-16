import requests
import json
from mixins import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
from settings import settings


class CRUD():
    """ Class containing all CRUD methods. """

    def list_records(self):
        """ List all records in the table. """
        print('Listing records...')
        req = requests.get(settings.get_url + settings.LIST_RECORDS_URL, headers=settings.AUTH_TOKEN_HEADER)
        return req.json()

    def retrieve_record(self, id_):
        """ Get a record by ID. """
        print('Retrieving record...')
        req = requests.get(settings.get_url + f'/{id_}', headers=settings.AUTH_TOKEN_HEADER)
        return req.json()

    def create_record(self):
        """ Create a new record. """
        print('Creating record...')
        obj = json.dumps({'records': [{'fields': {'title': 'SOME TITLE', 'description': 'SOME DESCRIPTION', 'price': '1000'}}]})
        req = requests.post(settings.get_url + settings.CREATE_RECORD_URL, headers=settings.AUTH_TOKEN_HEADER, data=obj)
        return req.json()

    def update_record(self, id_):
        """ Update a record by ID. """
        print('Updating record...')
        obj = requests.get(settings.get_url + f'/{id_}', headers=settings.AUTH_TOKEN_HEADER).json()
        data = {'records': [{'id': id_, 'fields': {'title': 'SOME TITLE', 'description': 'SOME DESCRIPTION', 'price': '1000'}}]}
        req = requests.patch(settings.get_url + f'/{id_}', headers=settings.AUTH_TOKEN_HEADER, data=data)
        return req.json()

    def delete_record(self, id_):
        """ Delete a record by ID. """
        print('Deleting record...')
        req = requests.delete(
            settings.get_url + f'/{id_}', 
            headers=settings.AUTH_TOKEN_HEADER, 
            data=f'records[]={id_}'
            )
        return req.json()


