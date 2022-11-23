from http.server import BaseHTTPRequestHandler
from src.authentication.client_authentication_request import ClientAuthenticationRequest
from src.authentication.client_authentication_response import ClientAuthenticationResponse
from src.authentication.authentication_exception import AuthenticationException


class IoTEndpointAuthenticationHandler(BaseHTTPRequestHandler):
    """
    Class that handles any incoming requests of the authentication server.
    """

    def do_POST(self):
        """
        Function that handles any incoming POST requests on the authentication server.
        This function processes the request and returns the authentication response.
        """
        try:
            content_length = int(self.headers["Content-Length"])
            json_content = str(self.rfile.read(content_length), "utf-8")
            authentication_request = ClientAuthenticationRequest.parse_from_json(json_content)
            authentication_request.validate()
            authenticated = authentication_request.verify()

            if authenticated:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                authentication_response = ClientAuthenticationResponse.from_request(authentication_request)
                return_message = authentication_response.to_json()
            else:
                self.send_response(401)
                self.end_headers()
                return_message = "Unauthenticated: Invalid credentials"

            self.wfile.write(bytes(return_message, "utf-8"))
        except AuthenticationException as e:
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            error_message = f"{{ \"error\": \"{e}\" }}"
            self.wfile.write(bytes(error_message, "utf-8"))
