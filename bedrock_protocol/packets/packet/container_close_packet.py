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
    container_id: int
    container_type: int
    is_server_side: bool

    def __init__(
        self, container_id: int = 0, container_type: int = 0, server_side: bool = False
    ):
        super().__init__()
        self.container_id = container_id
        self.container_type = container_type
        self.is_server_side = server_side

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.ContainerClose

    def get_packet_name(self) -> str:
        return "ContainerClosePacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_byte(self.container_id)
        stream.write_byte(self.container_type)
        stream.write_bool(self.is_server_side)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.container_id = stream.get_byte()
        self.container_type = stream.get_byte()
        self.is_server_side = stream.get_bool()
