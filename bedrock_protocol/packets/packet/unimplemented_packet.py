# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds


class UnimplementedPacket(Packet):
    packet_id: MinecraftPacketIds
    payload: bytes

    def __init__(self, packet_id: int, payload: bytes = b""):
        super().__init__()
        self.packet_id = packet_id
        self.payload = payload

    def get_packet_id(self) -> MinecraftPacketIds:
        return self.packet_id

    def get_packet_name(self) -> str:
        return "UnimplementedPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_raw_bytes(self.payload)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.payload = stream.get_left_buffer()
