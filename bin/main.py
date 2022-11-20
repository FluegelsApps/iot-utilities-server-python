from src.endpoint.iot_endpoint_server import IoTEndpointServer
from src.endpoint.iot_endpoint_authentication_server import IoTEndpointAuthenticationServer
import argparse
from threading import Thread


def main():
    """
    Main function of the program.
    This function parses all arguments and starts the WebSocket server.
    """
    # Parse all CLI arguments
    parser = argparse.ArgumentParser(description="IoT-Utilities Python Example Server")
    parser.add_argument("--port", action="store", type=int, help="Port of the WebSocket server")
    parser.add_argument("--certificate", action="store", type=str, help="Path of the SSL certificate file")
    parser.add_argument("--raw", action="store_true", help="Enables/disables raw protobuf message output")
    arguments = parser.parse_args()

    # Configure the WebSocket server
    server = IoTEndpointServer(
        arguments.port if arguments.port else 5443,
        arguments.certificate,
        arguments.raw
    )

    # Configure the authentication server
    authentication_server = IoTEndpointAuthenticationServer()

    # Start the threads for the servers
    https_thread = Thread(target=authentication_server.start)
    https_thread.start()

    wss_thread = Thread(target=server.start)
    wss_thread.start()

    # Join the threads to the main thread
    wss_thread.join()
    https_thread.join()


if __name__ == "__main__":
    main()
