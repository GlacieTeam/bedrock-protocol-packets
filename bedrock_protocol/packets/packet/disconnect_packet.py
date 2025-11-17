from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.minecraft_packet_ids import MinecraftPacketIds
from bedrock_protocol.packets.packet.packet_base import Packet

class DisconnectPacket(Packet):
    def __init__(
        self,
        disconnect_fail_reason: int = 0,
        hide_disconnection_reason: int = 0,
        message: str = "",
        filtered_message: str = "",
    ):
        super().__init__()
        self.disconnect_fail_reason = disconnect_fail_reason
        self.hide_disconnection_reason = hide_disconnection_reason
        self.message = message
        self.filtered_message = filtered_message

    def get_packet_id(self) -> MinecraftPacketIds:
        return MinecraftPacketIds.Disconnect

    def get_packet_name(self) -> str:
        return "DisconnectPacket"

    def write(self, stream: BinaryStream) -> None:
        stream.write_varint64(self.disconnect_fail_reason)
        stream.write_varint(self.hide_disconnection_reason)
        stream.write_string(self.message)
        stream.write_string(self.filtered_message)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.disconnect_fail_reason = stream.get_varint64()
        self.hide_disconnection_reason = stream.get_varint()
        self.message = stream.get_string()
        self.filtered_message = stream.get_string()
