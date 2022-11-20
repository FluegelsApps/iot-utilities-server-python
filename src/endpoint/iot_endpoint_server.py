import asyncio
import websockets
import pathlib
import ssl

import src.proto.aruba_iot_nb_pb2
from src.utils import resolve_mac_address


class IoTEndpointServer:
    """
    Class that represents the IoT Endpoint Server.
    This server is a WebSocket server that receives the Aruba
    """
    def __init__(self, port, certificate, raw_output):
        self.__port = port
        self.__certificate = certificate
        self.__raw_output = raw_output

    def start(self):
        asyncio.run(self.__start_internal())

    async def handle(self, websocket):
        while True:
            message = await websocket.recv()
            telemetry = src.proto.aruba_iot_nb_pb2.Telemetry()
            telemetry.ParseFromString(message)

            if self.__raw_output:
                print(telemetry)
            else:
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

    async def __start_internal(self):
        if self.__certificate:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            server_pem = pathlib.Path(self.__certificate)
            ssl_context.load_cert_chain(server_pem)
        else:
            ssl_context = None

        async with websockets.serve(self.handle, "localhost", self.__port, ssl=ssl_context):
            await asyncio.Future()
