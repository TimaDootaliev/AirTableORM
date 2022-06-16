class Settings:
    """A class to store all settings for AirTable."""
    AUTH_TOKEN_HEADER: dict = {'Authorization': 'Bearer keydGwz8zs6pfYQEo'} # Your API key. You can get it from https://airtable.com/account/
    TABLE_NAME: str = 'FirstTable' # Your table name
    BASE_ID: str = 'appDtMoTVRSTN916B' # Your base ID

    LIST_RECORDS_URL: str = f'?maxRecords=3&view=Grid%20view' # Your list records URL
    CREATE_RECORD_URL: str = f'/{BASE_ID}/{TABLE_NAME}'


    @property
    def get_url(self):
        """Returns the URL for the API."""
        return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}'
    


settings = Settings()