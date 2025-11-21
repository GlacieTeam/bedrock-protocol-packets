# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.types.connection_request import ConnectionRequest


class LoginPacket(Packet):
    client_protocol_version: int
    connection_request: ConnectionRequest

    def __init__(
        self,
        client_protocol_version: int = 0,
        connection_request: ConnectionRequest = None,
    ):
        self.client_protocol_version = client_protocol_version
        self.connection_request = connection_request or ConnectionRequest()

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.Login

    def get_packet_name(self) -> str:
        return "LoginPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_signed_big_endian_int(self.client_protocol_version)
        self.connection_request.write(stream)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.client_protocol_version = stream.get_signed_big_endian_int()
        self.connection_request.read(stream)
