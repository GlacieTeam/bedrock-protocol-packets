# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.types.network_position import NetworkBlockPosition
from bedrock_protocol.packets.packet.packet_base import Packet


class ContainerOpenPacket(Packet):
    container_id: int
    container_type: int
    position: NetworkBlockPosition
    target_actor_id: int

    def __init__(
        self,
        container_id: int = 0,
        container_type: int = 0,
        block_position: NetworkBlockPosition | None = None,
        target_actor_id: int = -1,
    ):
        super().__init__()
        self.container_id = container_id
        self.container_type = container_type
        self.position = block_position or NetworkBlockPosition()
        self.target_actor_id = target_actor_id

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.ContainerOpen

    def get_packet_name(self) -> str:
        return "ContainerOpenPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_byte(self.container_id)
        stream.write_byte(self.container_type)
        self.position.write(stream)
        stream.write_varint64(self.target_actor_id)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.container_id = stream.get_byte()
        self.container_type = stream.get_byte()
        self.position.read(stream)
        self.target_actor_id = stream.get_varint64()
