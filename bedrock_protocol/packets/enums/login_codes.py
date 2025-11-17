from enum import IntEnum

class LoginCodes(IntEnum):
    Success = 0
    Unknown = 1
    Overflow = 2
    NoCertificate = 3
    OfflineClient = 4
    MalformedChainData = 5
    NoExtraData = 6
    NoToken = 7
    MalformedToken = 8
    ChainDataParseError = 9
    ClientDataParseError = 10
    MalformedAuthType = 11