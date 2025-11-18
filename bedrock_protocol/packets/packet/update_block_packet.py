# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.types.network_position import NetworkBlockPosition


class UpdateBlockPacket(Packet):
    block_position: NetworkBlockPosition
    block_runtime_id: int
    update_flag: int
    block_layer: int

    def __init__(
        self,
        pos: NetworkBlockPosition | None = None,
        runtime_id: int = 0,
        flag: int = 0,
        layer: int = 0,
    ):
        super().__init__()
        self.block_position = pos or NetworkBlockPosition()
        self.block_runtime_id = runtime_id
        self.update_flag = flag
        self.block_layer = layer

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.UpdateBlock

    def get_packet_name(self) -> str:
        return "UpdateBlockPacket"

    def write(self, stream: BinaryStream) -> None:
        self.block_position.write(stream)
        stream.write_unsigned_varint(self.block_runtime_id)
        stream.write_unsigned_varint(self.update_flag)
        stream.write_unsigned_varint(self.block_layer)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.block_position.read(stream)
        self.block_runtime_id = stream.get_unsigned_varint()
        self.update_flag = stream.get_unsigned_varint()
        self.block_layer = stream.get_unsigned_varint()
