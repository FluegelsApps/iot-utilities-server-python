from src.endpoint.iot_endpoint_server import IoTEndpointServer
import argparse


def main():
    parser = argparse.ArgumentParser(description="IoT-Utilities Python Example Server")
    parser.add_argument("--port", action="store", type=int)
    arguments = parser.parse_args()

    server = IoTEndpointServer(arguments.port if arguments.port else 5443)
    server.start()


if __name__ == "__main__":
    main()
