from src.authentication.client_authentication_request import ClientAuthenticationRequest
import json


class ClientAuthenticationResponse:

    TOKEN_TYPE_DEFAULT = "bearer"
    SCOPE_DEFAULT = "Aruba_IoT_Framework"

    def __init__(self):
        self.access_token = ""
        self.refresh_token = ""
        self.api_url = ""
        self.token_type = ""
        self.expires_in = ""
        self.scope = ""

    @staticmethod
    def from_request(request):
        if request.grant_type == ClientAuthenticationRequest.GRANT_TYPE_PASSWORD:
            return ClientAuthenticationResponse.with_access_token(request)
        elif request.grant_type == ClientAuthenticationRequest.GRANT_TYPE_REFRESH_TOKEN:
            return ClientAuthenticationResponse.with_refresh_token(request)
        else:
            raise Exception(f"Unknown grant type '{request.grant_type}'")

    @staticmethod
    def with_access_token(request):
        default_response = ClientAuthenticationResponse()
        default_response.access_token = "access_token"
        default_response.refresh_token = "refresh_token"
        default_response.expires_in = "600s"
        default_response.token_type = ClientAuthenticationResponse.TOKEN_TYPE_DEFAULT
        default_response.scope = request.scope
        return default_response

    @staticmethod
    def with_refresh_token(request):
        refresh_response = ClientAuthenticationResponse()
        refresh_response.access_token = "access_token"
        refresh_response.expires_in = "600s"
        refresh_response.token_type = ClientAuthenticationResponse.TOKEN_TYPE_DEFAULT
        refresh_response.scope = request.scope
        return refresh_response

    def to_json(self):
        return json.dumps(self)
