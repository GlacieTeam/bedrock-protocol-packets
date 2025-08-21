# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.types.network_position import NetworkBlockPosition
from bedrock_protocol.nbt import CompoundTag


class BlockActorDataPacket(Packet):
    block_position: NetworkBlockPosition
    actor_data_tags: CompoundTag

    def __init__(
        self,
        pos: NetworkBlockPosition = NetworkBlockPosition(),
        nbt: CompoundTag = CompoundTag(),
    ):
        super().__init__()
        self.block_position = pos
        self.actor_data_tags = nbt

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.BlockActorData

    def get_packet_name(self) -> str:
        return "BlockActorDataPacket"

    def write(self, stream: BinaryStream) -> None:
        self.block_position.write(stream)
        self.actor_data_tags.write(stream)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.block_position.read(stream)
        self.actor_data_tags.read(stream)
