# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.packets.packet import *  # pylint: disable=wildcard-import,unused-wildcard-import
from bedrock_protocol.packets.types import *  # pylint: disable=wildcard-import,unused-wildcard-import
from bedrock_protocol.packets import *  # pylint: disable=wildcard-import,unused-wildcard-import


def test1():
    packet_write = UpdateBlockPacket(NetworkBlockPosition(11, 45, 14), 2537812, 3, 0)
    payload = packet_write.serialize()
    print(f"{payload.hex()} | {payload.hex()=='162d1cd4f29a010300'}")

    packet_read = UpdateBlockPacket()
    packet_read.deserialize(bytes.fromhex("162d1cd4f29a010300"))
    print(f"{packet_read.block_position.x} | {packet_read.block_position.x==11}")
    print(f"{packet_read.block_position.y} | {packet_read.block_position.y==45}")
    print(f"{packet_read.block_position.z} | {packet_read.block_position.z==14}")
    print(f"{packet_read.block_runtime_id} | {packet_read.block_runtime_id==2537812}")
    print(f"{packet_read.update_flag} | {packet_read.update_flag==3}")
    print(f"{packet_read.block_layer} | {packet_read.block_layer==0}")


def test2():
    """Test default constructor"""
    for packet_id in MinecraftPacketIds:
        packet = MinecraftPackets.create_packet(packet_id)
        if packet.get_packet_name() != "UnimplementedPacket":
            print(packet.get_packet_name())
        packet.serialize()
        packet.deserialize(b"")
    print("All packets default constructor test pass")  # if no exception


if __name__ == "__main__":
    print("-" * 25, "Test1", "-" * 25)
    test1()
    print("-" * 25, "Test2", "-" * 25)
    test2()
    print("-" * 25, "END", "-" * 25)
