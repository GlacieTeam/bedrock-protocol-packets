# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.types.network_position import NetworkBlockPosition
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.enums.level_sound_event import LevelSoundEventType


class LevelSoundEventPacket(Packet):
    sound_type: LevelSoundEventType
    block_position: NetworkBlockPosition
    extra_data: int
    entity_type: str
    baby_mob: bool
    global_sound: bool
    actor_unique_id: int

    def __init__(
        self,
        sound_type: LevelSoundEventType = LevelSoundEventType.Undefined,
        pos: NetworkBlockPosition = NetworkBlockPosition(),
        extra_data: int = 0,
        entity_type: str = "",
        baby_mob: bool = False,
        global_sound: bool = False,
        actor_unique_id: int = 0,
    ):
        super().__init__()
        self.sound_type = sound_type
        self.block_position = pos
        self.extra_data = extra_data
        self.entity_type = entity_type
        self.baby_mob = baby_mob
        self.global_sound = global_sound
        self.actor_unique_id = actor_unique_id

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.LevelSoundEvent

    def get_packet_name(self) -> str:
        return "LevelSoundEventPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_unsigned_varint(self.sound_type)
        self.block_position.write(stream)
        stream.write_unsigned_varint(self.extra_data)
        stream.write_string(self.entity_type)
        stream.write_bool(self.baby_mob)
        stream.write_bool(self.global_sound)
        stream.write_varint64(self.actor_unique_id)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.sound_type = stream.get_unsigned_varint()
        self.block_position = self.block_position.read(stream)
        self.extra_data = stream.get_unsigned_varint()
        self.entity_type = stream.get_string()
        self.baby_mob = stream.get_bool()
        self.global_sound = stream.get_bool()
        self.actor_unique_id = stream.get_varint64()
