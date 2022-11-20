import asyncio
import websockets
import pathlib
import ssl

import src.proto.aruba_iot_nb_pb2
from src.utils import resolve_mac_address


class IoTEndpointServer:
    """
    Class that represents the IoT Endpoint Server.
    This server is a WebSocket server that receives the Aruba Protobuf data.
    """

    def __init__(self, port, certificate, raw_output):
        """
        Constructor of the instance.

        :param port: Port of the WebSocket server (default 5443).
        :type port: int
        :param certificate: Path of the certificate file of the server (default none).
        :type certificate: str
        :param raw_output: Determines whether raw message output is enabled (default false).
        :type raw_output: bool
        """
        self.__port = port
        self.__certificate = certificate
        self.__raw_output = raw_output

    def start(self):
        """
        Function that starts the WebSocket server.
        """
        asyncio.run(self.__start_internal())

    async def handle(self, websocket):
        """
        Function that handles the incoming messages of the WebSocket server.
        This function parses the Protocol buffer data and prints the data to the console.

        :param websocket: Websocket the data was received by.
        """
        while True:
            # Receive and parse the message
            message = await websocket.recv()
            telemetry = src.proto.aruba_iot_nb_pb2.Telemetry()
            telemetry.ParseFromString(message)

            if self.__raw_output:
                print(telemetry)
            else:
                # Print message and reporter information
                print()
                print(f"Incoming protobuf message with topic: {telemetry.meta.nbTopic}")
                print()
                print(f"--- Reporter ---")
                print(f"Name: {telemetry.reporter.name}")
                print(f"MAC-Address: {resolve_mac_address(telemetry.reporter.mac)}")
                print(f"iPv4-Address: {telemetry.reporter.ipv4}")
                print(f"iPv6-Address: {telemetry.reporter.ipv6}")
                print(f"Hardware Type: {telemetry.reporter.hwType}")
                print(f"Software Version: {telemetry.reporter.swVersion}")
                print(f"Software Build: {telemetry.reporter.swBuild}")

                # Print telemetry information
                if len(telemetry.reported) > 0:
                    print()
                    print(f"--- Telemetry Data ---")

                    for reported in telemetry.reported:
                        print(f"MAC-Address: {resolve_mac_address(reported.mac)}")
                        print(f"Device class: {reported.deviceClass}")
                        print(f"RSSI: {reported.rssi}")
                        print(f"Beacons:\n{reported.beacons}")

    async def __start_internal(self):
        """
        Function that starts the actual WebSocket server.
        This function loads the SSL certificate and context if enabled.
        Finally, the WebSocket server is started with all given parameters.
        """
        # Prepare the SSL context
        if self.__certificate:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            server_pem = pathlib.Path(self.__certificate)
            ssl_context.load_cert_chain(server_pem)
        else:
            ssl_context = None

        # Start the SSL server
        async with websockets.serve(self.handle, "localhost", self.__port, ssl=ssl_context):
            await asyncio.Future()
