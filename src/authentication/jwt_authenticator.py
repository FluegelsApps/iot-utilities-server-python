import jwt
from datetime import datetime, timedelta, timezone


class JWTAuthenticator:
    @staticmethod
    def generate_access_token() -> str:
        return jwt.encode(
            {
                "scope": "telemetry",
                "iss": "IoT-Utilities Python Demo Server",
                "iat": datetime.now(tz=timezone.utc),
                "nbf": datetime.now(tz=timezone.utc) - timedelta(minutes=1),
                "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=10)
            },
            "demo_secret",
            algorithm="HS256"
        )

    @staticmethod
    def generate_refresh_token() -> str:
        return jwt.encode(
            {
                "scope": "refresh",
                "iss": "IoT-Utilities Python Demo Server",
                "iat": datetime.now(tz=timezone.utc),
                "nbf": datetime.now(tz=timezone.utc) - timedelta(minutes=1),
                "exp": datetime.now(tz=timezone.utc) + timedelta(days=1)
            },
            "demo_secret",
            algorithm="HS256"
        )

    @staticmethod
    def validate_access_token(token: str) -> bool:
        try:
            decoded_jwt = jwt.decode(token, "demo_secret", algorithms=["HS256"])
            return decoded_jwt["scope"] == "telemetry"
        except jwt.DecodeError:
            return False

    @staticmethod
    def validate_refresh_token(token: str) -> bool:
        try:
            decoded_jwt = jwt.decode(token, "demo_secret", algorithms=["HS256"])
            return decoded_jwt["scope"] == "refresh"
        except jwt.DecodeError:
            return False
