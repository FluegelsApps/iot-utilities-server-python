# iot-utilities-server-python
Python WebSocket Server implementation that works like the IoT-Utilities Android App.

## Usage

- Download or clone the source code
- Use your terminal to navigate into the folder of the project
- Install the dependencies

```
pip3 install -r requirements.txt
```

- Make sure python 3 is installed, start the server:

```
python3 -m bin.main
```

The server implementation contains both an authentication server (default on port 5444) and a WebSocket server (default on port 5443).

## Authentication Configuration

For security reasons, the authentication credentials of the server have to be configured seperately.
Therefore, edit the "config.json" file and enter the desired credentials for the server.

- auth_username: Username required when using grant type "password"
- auth_password: Password required when using grant type "password"
- auth_secret: Secret required when using grant type "client_credentials"
- jwt_signature_secret: Secret used to sign and verify the JWT access tokens

Example:

```json
{
  "auth_username": "<place_your_username_here>",
  "auth_password": "<place_your_password_here>",
  "auth_secret": "<place_your_secret_here>",
  "jwt_signature_secret": "<place_your_secret_here>"
}
```

## Command line arguments

All command line arguments and explanations can be listed using the --help argument.

--port: Port of the WebSocket server  
--authport: Port of the Authentication server  
--certificate: Path to the certificate PEM file  
--raw: Prints the messages in JSON format if present

> Note: The server supports both HTTP/WS and HTTPS/WSS connections. In order to encrypt the connection, a SSL certificate file (PEM format) needs to be provided using the --certificate command line argument. Example: python3 -m bin.main --certificate "test.pem"