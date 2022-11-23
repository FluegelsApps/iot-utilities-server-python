from src.authentication.client_authentication_request import ClientAuthenticationRequest
from src.authentication.jwt_authenticator import JWTAuthenticator
import json


class ClientAuthenticationResponse:
    """
    Class that represents a single authentication response containing the following fields:
    - access_token: Access token the client should include in future messages.
    - refresh_token: Additional token used to obtain a new access token after expiration.
    - api_url: URL of the websocket endpoint that receives the data.
    - token_type: Type of the access token (default: bearer).
    - expires_in: Time in seconds, when the access token will expire.
    - scope: Scope of the authentication (yielded from request).
    """

    TOKEN_TYPE_DEFAULT = "bearer"
    SCOPE_DEFAULT = "Aruba_IoT_Framework"

    def __init__(self):
        """
        Constructor of the instance.
        The constructor initializes all fields with empty strings.
        """
        self.access_token = ""
        self.refresh_token = ""
        self.api_url = ""
        self.token_type = ""
        self.expires_in = ""
        self.scope = ""

    @staticmethod
    def from_request(request):
        """
        Utility function that creates a response instance from the incoming request.

        :param request: Request the instance should be created from.
        :type request: ClientAuthenticationRequest

        :return: Returns the created response.
        """
        if request.grant_type == ClientAuthenticationRequest.GRANT_TYPE_PASSWORD:
            return ClientAuthenticationResponse.with_access_token(request)
        elif request.grant_type == ClientAuthenticationRequest.GRANT_TYPE_REFRESH_TOKEN:
            return ClientAuthenticationResponse.with_refresh_token(request)
        else:
            raise Exception(f"Unknown grant type '{request.grant_type}'")

    @staticmethod
    def with_access_token(request):
        """
        Utility function that creates a response instance from an access token.

        :param request: Request the instance should be created from.
        :type request: ClientAuthenticationRequest

        :return: Returns the created response.
        """
        default_response = ClientAuthenticationResponse()
        default_response.access_token = JWTAuthenticator.generate_access_token()
        default_response.refresh_token = JWTAuthenticator.generate_refresh_token()
        default_response.expires_in = "600s"
        default_response.token_type = ClientAuthenticationResponse.TOKEN_TYPE_DEFAULT
        default_response.scope = request.scope
        return default_response

    @staticmethod
    def with_refresh_token(request):
        """
        Utility function that creates a response instance from the refresh token.

        :param request: Request the instance should be created from.
        :type request: ClientAuthenticationRequest

        :return: Returns the created response.
        """
        refresh_response = ClientAuthenticationResponse()
        refresh_response.access_token = JWTAuthenticator.generate_access_token()
        refresh_response.expires_in = "600s"
        refresh_response.token_type = ClientAuthenticationResponse.TOKEN_TYPE_DEFAULT
        refresh_response.scope = request.scope
        return refresh_response

    def to_json(self):
        """
        Function that serializes the instance to a JSON string.

        :return: Returns the serialized JSON string.
        """
        return json.dumps(self, default=lambda o: o.__dict__)
