from http.server import HTTPServer
from src.endpoint.iot_endpoint_authentication_handler import IoTEndpointAuthenticationHandler


class IoTEndpointAuthenticationServer:
    """
    Class that represents the IoT Endpoint Authentication Server.
    Thi server is a HTTPS server that handles the client authentication.
    """
    @staticmethod
    def start():
        """
        Function that starts the authentication server.
        """
        with HTTPServer(("", 5444), IoTEndpointAuthenticationHandler) as server:
            server.serve_forever()
