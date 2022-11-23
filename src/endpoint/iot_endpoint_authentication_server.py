from http.server import HTTPServer
from src.endpoint.iot_endpoint_authentication_handler import IoTEndpointAuthenticationHandler
import ssl


class IoTEndpointAuthenticationServer:
    """
    Class that represents the IoT Endpoint Authentication Server.
    Thi server is a HTTPS server that handles the client authentication.
    """

    def __init__(self, certificate):
        """
        Constructor of the instance.

        :param certificate: Certificate path used for TLS (optional).
        :type certificate: str
        """
        self.__certificate = certificate

    def start(self):
        """
        Function that starts the authentication server.
        """
        with HTTPServer(("", 5444), IoTEndpointAuthenticationHandler) as server:
            if self.__certificate is not None:
                server.socket = ssl.wrap_socket(server.socket,
                                                server_side=True,
                                                certfile=self.__certificate,
                                                ssl_version=ssl.PROTOCOL_TLSv1_2)

            server.serve_forever()
