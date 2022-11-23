import json
from src.authentication.authentication_exception import AuthenticationException
from src.authentication.jwt_authenticator import JWTAuthenticator
from src.configuration import config


class ClientAuthenticationRequest:
    """
    Class that represents a single authentication request.
    """

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
        """
        Constructor of the instance.

        :param grant_type: Type of authentication used during the procedure.
        :type grant_type: str
        :param client_id: Identifier of the authenticating client.
        :type client_id: str
        :param client_secret: Secret phrase used when authenticating with grant type "client-secret".
        :type client_secret: str
        :param username: Username used when authenticating with grant type "password".
        :type username: str
        :param password: Password used when authenticating with grant type "password".
        :type password: str
        :param refresh_token: Refresh token used when authenticating with grant type "refresh_token".
        :type refresh_token: str
        :param scope: Scope used by the client, e.g. Aruba.
        :type scope: str
        """
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.refresh_token = refresh_token
        self.scope = scope

    @staticmethod
    def parse_from_json(json_string: str):
        """
        Function that parses an instance from a JSON string.

        :param json_string: JSON string the instance should be parsed from.
        :type json_string: str

        :return: Returns the created instance.
        """
        loads = json.loads(json_string)
        return ClientAuthenticationRequest(**loads)

    def validate(self):
        """
        Method that validates the parsed authentication data.
        Depending on the grant type, the authentication requires additional field:
        password: requires the fields username and password.
        refresh_token: requires the field refresh_token.
        client_credentials: requires the field client_secret.

        The remaining fields are optional: client_id, scope.
        """
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
        """
        Function that verifies the authentication credentials.
        Depending on the authentication type, the credentials are verified.

        :return: Returns whether the provided credentials are valid.
        """
        if self.grant_type == self.GRANT_TYPE_PASSWORD:
            return self.username == config.auth_username and self.password == config.auth_password
        elif self.grant_type == self.GRANT_TYPE_REFRESH_TOKEN:
            return JWTAuthenticator.validate_refresh_token(self.refresh_token)
        elif self.grant_type == self.GRANT_TYPE_CLIENT_CREDENTIALS:
            return self.client_secret == config.auth_secret
        else:
            raise AuthenticationException(f"Unknown grant type '{self.grant_type}'")
