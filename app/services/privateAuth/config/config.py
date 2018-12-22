from app.services.privateAuth.libs.addPrivateAuthToken import createToken


class Config(object):
    PRIVATE_HEADER_TOKEN = createToken()
