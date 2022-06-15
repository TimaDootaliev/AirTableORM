class Settings:
    """A class to store all settings for AirTable."""
    AUTH_TOKEN='Bearer keydGwz8zs6pfYQEo'
    TABLE_NAME='FirstTable'
    BASE_TOKEN='appDtMoTVRSTN916B'

    @property
    def get_url(self):
        """Returns the URL for the API."""
        return f'https://api.airtable.com/v0/{self.BASE_TOKEN}/{self.TABLE_NAME}'
    


settings = Settings()