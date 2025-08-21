# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.packets.packet import *
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds


class MinecraftPackets:
    _all_packets_map = {
        MinecraftPacketIds.RemoveActor: RemoveActorPacket,  # 14
        MinecraftPacketIds.UpdateBlock: UpdateBlockPacket,  # 21
        MinecraftPacketIds.ContainerOpen: ContainerOpenPacket,  # 46
        MinecraftPacketIds.ContainerClose: ContainerClosePacket,  # 47
        MinecraftPacketIds.BlockActorData: BlockActorDataPacket,  # 56
        MinecraftPacketIds.LevelSoundEvent: LevelSoundEventPacket,  # 123
    }

    @staticmethod
    def create_packet(packet_id: MinecraftPacketIds) -> Packet:
        packet_class = MinecraftPackets._all_packets_map.get(packet_id)
        if packet_class is not None:
            return packet_class()
        else:
            return UnimplementedPacket(packet_id)
