def decode_bytes(data: bytes) -> str:
    """
    Function that decodes the bytes of a protobuf field to a string.
    This function decodes the data to a hex string.

    :param data: Raw data that should be decoded.
    :type data: bytes

    :return: Returns the decoded string.
    """
    return data.hex()


def resolve_mac_address(data: bytes) -> str:
    """
    Function that resolves the MAC-Address from a protobuf byte field to a string.
    This function converts the data to a hex string and inserts the colons between the octets.

    :param data: Raw data used to resolve the MAC-Address:
    :type data: bytes

    :return: Returns the resolved MAC-Address
    """
    byte_string = decode_bytes(data)
    return ":".join(byte_string[i:i + 2].upper() for i in range(0, 12, 2))
