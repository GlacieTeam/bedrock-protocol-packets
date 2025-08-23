# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds


class RemoveActorPacket(Packet):
    unique_id: int

    def __init__(self, unique_id: int = 0):
        super().__init__()
        self.unique_id = unique_id

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.RemoveActor

    def get_packet_name(self) -> str:
        return "RemoveActorPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_varint64(self.unique_id)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.unique_id = stream.get_varint64()
