# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.packet.packet_base import Packet
from bedrock_protocol.packets.enums.disconnect_fail_reason import DisconnectFailReason


class DisconnectPacket(Packet):
    disconnect_fail_reason: DisconnectFailReason
    skip_message: bool
    message: str
    filtered_message: str

    def __init__(
        self,
        message: str = "",
        disconnect_fail_reason: DisconnectFailReason = DisconnectFailReason.DISCONNECTED,
        skip_message: bool = False,
        filtered_message: str = "",
    ):
        super().__init__()
        self.disconnect_fail_reason = disconnect_fail_reason
        self.skip_message = skip_message
        self.message = message
        self.filtered_message = filtered_message

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.Disconnect

    def get_packet_name(self) -> str:
        return "DisconnectPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_varint(self.disconnect_fail_reason)
        stream.write_bool(self.skip_message)
        if not self.skip_message:
            stream.write_string(self.message)
            stream.write_string(self.filtered_message)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.disconnect_fail_reason = stream.get_varint()
        self.skip_message = stream.get_bool()
        if not self.skip_message:
            self.message = stream.get_string()
            self.filtered_message = stream.get_string()
