from http.server import BaseHTTPRequestHandler


class IoTEndpointAuthenticationHandler(BaseHTTPRequestHandler):
    """
    Class that handles any incoming requests of the authentication server.
    """

    def do_POST(self):
        """
        Function that handles any incoming POST requests on the authentication server.
        This function processes the request and returns the authentication response.
        """
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        message = "Return"
        self.wfile.write(bytes(message, "utf-8"))
