# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from typing import List
from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.types.item_data import ItemData


class ItemRegistryPacket(Packet):
    item_registry: List[ItemData]

    def __init__(
        self, item_registry: List[ItemData] = []
    ):  # pylint: disable=dangerous-default-value
        self.item_registry = item_registry

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.ItemRegistryPacket

    def get_packet_name(self) -> str:
        return "ItemRegistryPacket"

    def write(self, stream: BinaryStream) -> None:
        pass

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        pass
