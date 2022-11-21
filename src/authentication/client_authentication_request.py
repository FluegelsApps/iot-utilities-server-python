import json
from src.authentication.authentication_exception import AuthenticationException


class ClientAuthenticationRequest:

    GRANT_TYPE_PASSWORD = "password"
    GRANT_TYPE_REFRESH_TOKEN = "refresh_token"
    GRANT_TYPE_CLIENT_CREDENTIALS = "client_credentials"

    def __init__(
            self,
            grant_type=None,
            client_id=None,
            client_secret=None,
            username=None,
            password=None,
            refresh_token=None,
            scope=None):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.refresh_token = refresh_token
        self.scope = scope

    @staticmethod
    def parse_from_json(json_string: str):
        loads = json.loads(json_string)
        return ClientAuthenticationRequest(**loads)

    def validate(self):
        if not self.grant_type:
            raise AuthenticationException("Parameter 'grant_type' missing")

        if self.grant_type == self.GRANT_TYPE_PASSWORD:
            if not self.username or not self.password:
                raise AuthenticationException("Parameter 'username' or 'password' missing")
        elif self.grant_type == self.GRANT_TYPE_REFRESH_TOKEN:
            if not self.refresh_token:
                raise AuthenticationException("Parameter 'refresh_token' missing")
        elif self.grant_type == self.GRANT_TYPE_CLIENT_CREDENTIALS:
            if not self.client_secret:
                raise AuthenticationException("Parameter 'client_secret' missing")
        else:
            raise AuthenticationException(f"Unknown grant type '{self.grant_type}'")

    def verify(self) -> bool:
        if self.grant_type == self.GRANT_TYPE_PASSWORD:
            return self.password == "password"
        elif self.grant_type == self.GRANT_TYPE_REFRESH_TOKEN:
            return self.refresh_token == "refresh_token"
        elif self.grant_type == self.GRANT_TYPE_CLIENT_CREDENTIALS:
            return self.client_secret == "client_secret"
        else:
            raise AuthenticationException(f"Unknown grant type '{self.grant_type}'")
