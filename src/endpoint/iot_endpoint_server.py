import asyncio
import websockets

import src.proto.aruba_iot_nb_pb2


class IoTEndpointServer:
    def __init__(self, port):
        self.__port = port

    def start(self):
        asyncio.run(self.__start_internal())

    @staticmethod
    async def handle(websocket):
        while True:
            message = await websocket.recv()
            telemetry = src.proto.aruba_iot_nb_pb2.Telemetry()
            telemetry.ParseFromString(message)
            print(telemetry)

    async def __start_internal(self):
        async with websockets.serve(self.handle, "localhost", self.__port):
            await asyncio.Future()
