# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.packet.packet_base import Packet


class ContainerClosePacket(Packet):
    window_id: int
    window_type: int
    server: bool

    def __init__(self, window_id: int = 0, window_type: int = 0, server: bool = False):
        super().__init__()
        self.window_id = window_id
        self.window_type = window_type
        self.server = server

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.ContainerClose

    def get_packet_name(self) -> str:
        return "ContainerClosePacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_varint(self.window_id)
        stream.write_varint(self.window_type)
        stream.write_bool(self.server)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.window_id = stream.get_varint()
        self.window_type = stream.get_varint()
        self.server = stream.get_bool()
