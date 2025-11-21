# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

import base64
import json
from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.enums.login_codes import LoginCodes


class LoginPacket(Packet):
    def __init__(self):
        self.status = LoginCodes.Unknown
        self.status_msg = "Unknown error"
        self.protocol_version: int = 0
        self.tokens_data: bytes = b""
        self.client_data: bytes = b""
        self.identity_data: dict = {}
        self.token: dict = {}
        self.client_data_json: dict = {}

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.Login

    def get_packet_name(self) -> str:
        return "Login"

    def write(self, stream: BinaryStream) -> None:
        stream.write_signed_big_endian_int(self.protocol_version)
        tokens_bytes = self.tokens_raw
        stream.write_unsigned_int(len(tokens_bytes))
        stream.write_raw_bytes(tokens_bytes)
        client_bytes = self.client_data_raw
        stream.write_unsigned_int(len(client_bytes))
        stream.write_raw_bytes(client_bytes)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.protocol_version = stream.get_signed_big_endian_int()
        tokens_len = stream.get_unsigned_varint()
        self.tokens_raw = stream.get_raw_bytes(tokens_len)
        self.tokens_json = json.loads(self.tokens_raw)
        cert_str = self.tokens_json["Certificate"]
        self.certificate_json = json.loads(cert_str)
        identity_jwt = self.certificate_json["chain"][2]
        self.identity_jwt_payload = self.parse_jwt_payload(identity_jwt)
        token_jwt = self.tokens_json["Token"]
        self.token_jwt_payload = self.parse_jwt_payload(token_jwt)
        client_len = stream.get_unsigned_int()
        self.client_data_raw = stream.get_raw_bytes(client_len)
        self.client_data_jwt_payload = self.parse_jwt_payload(
            self.client_data_raw.decode("utf-8")
        )

    def serialize(self) -> bytes:
        """Serialize the packet to bytes"""
        stream = BinaryStream()
        self.write(stream)
        return stream.get_and_release_data()

    def deserialize(self, payload: bytes) -> None:
        """Deserialize the packet from bytes"""
        stream = ReadOnlyBinaryStream(payload)
        self.read(stream)

    def parse_jwt_payload(jwt: str):
        """Decode the payload segment of a JWT (without validation)"""
        dot1 = jwt.find(".")
        dot2 = jwt.find(".", dot1 + 1)
        payload = jwt[dot1 + 1 : dot2]
        padding = "=" * (-len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload + padding)
        return json.loads(decoded.decode("utf-8"))
