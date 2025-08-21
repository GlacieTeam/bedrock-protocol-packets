# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.packets.packet import *
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds


class MinecraftPackets:
    @staticmethod
    def create_packet(packet_id: MinecraftPacketIds) -> Packet:
        match packet_id:  ## match requires Python 3.10+
            case MinecraftPacketIds.RemoveActor:  # 14
                return RemoveActorPacket()
            case MinecraftPacketIds.UpdateBlock:  # 21
                return UpdateBlockPacket()
            case MinecraftPacketIds.ContainerOpen:  # 46
                return ContainerOpenPacket()
            case MinecraftPacketIds.ContainerClose:  # 47
                return ContainerClosePacket()
            case MinecraftPacketIds.BlockActorData:  # 56
                return BlockActorDataPacket()
            case MinecraftPacketIds.LevelSoundEvent:  # 123
                return LevelSoundEventPacket()
            case _:
                return UnimplementedPacket(packet_id)
