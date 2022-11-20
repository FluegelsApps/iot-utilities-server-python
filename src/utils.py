def decode_bytes(data: bytes) -> str:
    return data.hex()


def resolve_mac_address(data: bytes) -> str:
    byte_string = decode_bytes(data)
    return ":".join(byte_string[i:i + 2].upper() for i in range(0, 12, 2))
