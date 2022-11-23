import jwt
from datetime import datetime, timedelta, timezone
from src.configuration import config


class JWTAuthenticator:
    """
    Class that handles the authentication with JWT tokens.
    """

    @staticmethod
    def generate_access_token() -> str:
        """
        Function that generates a new JWT access token.
        This access token contains various claims that are verified during authentication and message processing.
        By default, the token expires after 10 minutes.
        Furthermore, the token is encoded using a HS256 secret.

        :return: Returns the generated access token.
        """
        return jwt.encode(
            {
                "scope": "telemetry",
                "iss": "IoT-Utilities Python Demo Server",
                "iat": datetime.now(tz=timezone.utc),
                "nbf": datetime.now(tz=timezone.utc) - timedelta(minutes=1),
                "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=10)
            },
            config.jwt_signature_secret,
            algorithm="HS256"
        )

    @staticmethod
    def generate_refresh_token() -> str:
        """
        Function that generates a new JWT refresh token.
        This refresh token contains various claims that are verified during authentication and message processing.
        By default, the token expires after 1 day.
        Furthermore, the token is encoded using a HS256 secret.

        :return: Returns the generated refresh token.
        """
        return jwt.encode(
            {
                "scope": "refresh",
                "iss": "IoT-Utilities Python Demo Server",
                "iat": datetime.now(tz=timezone.utc),
                "nbf": datetime.now(tz=timezone.utc) - timedelta(minutes=1),
                "exp": datetime.now(tz=timezone.utc) + timedelta(days=1)
            },
            config.jwt_signature_secret,
            algorithm="HS256"
        )

    @staticmethod
    def validate_access_token(token: str) -> bool:
        """
        Function that validates a given JWT access token.
        This function verifies the signature of the token and checks whether the scope claim is included.

        :param token: Access token that should be validated.
        :type token: str

        :return: Returns whether the access token is valid.
        """
        try:
            decoded_jwt = jwt.decode(token, config.jwt_signature_secret, algorithms=["HS256"])
            return decoded_jwt["scope"] == "telemetry"
        except jwt.DecodeError:
            return False

    @staticmethod
    def validate_refresh_token(token: str) -> bool:
        """
        Function that validates a given JWT refresh token.
        This function verifies the signature of the token and checks whether the scope claim is included.

        :param token: Refresh token that should be validated.
        :type token: str

        :return: Returns whether the access token is valid.
        """
        try:
            decoded_jwt = jwt.decode(token, config.jwt_signature_secret, algorithms=["HS256"])
            return decoded_jwt["scope"] == "refresh"
        except jwt.DecodeError:
            return False
