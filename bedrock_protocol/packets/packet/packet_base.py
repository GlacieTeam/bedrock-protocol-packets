# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from abc import ABC, abstractmethod


class Packet(ABC):
    """The Packet base class"""

    @abstractmethod
    def get_packet_id(self) -> MinecraftPacketIds:
        pass

    @abstractmethod
    def get_packet_name(self) -> str:
        pass

    @abstractmethod
    def write(self, stream: BinaryStream) -> None:
        pass

    @abstractmethod
    def read(self, stream: ReadOnlyBinaryStream) -> None:
        pass

    def serialize(self) -> bytes:
        """Serialize the packet to bytes"""
        stream = BinaryStream()
        self.write(stream)
        return stream.get_and_release_data()

    def deserialize(self, payload: bytes) -> None:
        """Deserialize the packet from bytes"""
        stream = ReadOnlyBinaryStream(payload)
        self.read(stream)
