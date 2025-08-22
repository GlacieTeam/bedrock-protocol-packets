# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.types.vec3 import Vec3
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.enums.level_sound_event import LevelSoundEventType


class LevelSoundEventPacket(Packet):
    sound_type: LevelSoundEventType
    position: Vec3
    extra_data: int
    entity_type: str
    is_baby_mob: bool
    is_global_sound: bool
    actor_unique_id: int

    def __init__(
        self,
        sound_type: LevelSoundEventType = LevelSoundEventType.Undefined,
        pos: Vec3 = Vec3(),
        extra_data: int = 0,
        entity_type: str = "",
        baby_mob: bool = False,
        global_sound: bool = False,
        actor_unique_id: int = -1,
    ):
        super().__init__()
        self.sound_type = sound_type
        self.position = pos
        self.extra_data = extra_data
        self.entity_type = entity_type
        self.is_baby_mob = baby_mob
        self.is_global_sound = global_sound
        self.actor_unique_id = actor_unique_id

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.LevelSoundEvent

    def get_packet_name(self) -> str:
        return "LevelSoundEventPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_unsigned_varint(self.sound_type)
        self.position.write(stream)
        stream.write_varint(self.extra_data)
        stream.write_string(self.entity_type)
        stream.write_bool(self.is_baby_mob)
        stream.write_bool(self.is_global_sound)
        stream.write_signed_int64(self.actor_unique_id)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.sound_type = stream.get_unsigned_varint()
        self.position.read(stream)
        self.extra_data = stream.get_varint()
        self.entity_type = stream.get_string()
        self.is_baby_mob = stream.get_bool()
        self.is_global_sound = stream.get_bool()
        self.actor_unique_id = stream.get_signed_int64()
