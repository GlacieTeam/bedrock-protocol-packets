# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from typing import List, Optional
from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.types.full_container_name import FullContainerName
from bedrock_protocol.packets.enums.item_stack_request_action_type import (
    ItemStackRequestActionType,
)


class ItemStackRequestSlotInfo:
    container: FullContainerName
    slot: int
    net_id: int

    def __init__(
        self,
        container: FullContainerName = FullContainerName(),
        slot: int = 0,
        net_id: int = 0,
    ):
        self.container = container
        self.slot = slot
        self.net_id = net_id

    def write(self, stream: BinaryStream) -> None:
        self.container.write(stream)
        stream.write_byte(self.slot)
        stream.write_varint(self.net_id)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.container.read(stream)
        self.slot = stream.get_byte()
        self.net_id = stream.get_varint()


class ItemStackRequestActionTransferBase:
    amount: int
    source: ItemStackRequestSlotInfo
    distination: ItemStackRequestSlotInfo

    def __init__(
        self,
        amount: int = 0,
        source: ItemStackRequestSlotInfo = ItemStackRequestSlotInfo(),
        distination: ItemStackRequestSlotInfo = ItemStackRequestSlotInfo(),
    ):
        self.amount = amount
        self.source = source
        self.distination = distination

    def write(self, stream: BinaryStream) -> None:
        stream.write_byte(self.amount)
        self.source.write(stream)
        self.distination.write(stream)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.amount = stream.get_byte()
        self.source.read(stream)
        self.distination.read(stream)


class ItemStackRequestAction:
    action_type: ItemStackRequestActionType
    action_data: Optional[ItemStackRequestActionTransferBase]

    def __init__(
        self,
        action_type: ItemStackRequestActionType = ItemStackRequestActionType.Invalid,
        action_data: Optional[ItemStackRequestActionTransferBase] = None,
    ):
        self.action_type = action_type
        self.action_data = action_data

    def write(self, stream: BinaryStream) -> None:
        if self.action_data is not None:
            stream.write_byte(self.action_type)
            self.action_data.write(stream)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.action_type = stream.get_byte()
        if self.action_type in (
            ItemStackRequestActionType.Take,
            ItemStackRequestActionType.Place,
        ):
            data = ItemStackRequestActionTransferBase()
            data.read(stream)
            self.action_data = data


class ItemStackRequestData:
    client_request_id: int
    strings_to_filter: List[bytes]
    strings_to_filter_origin: int
    request_actions: List[ItemStackRequestAction]
    first_action_type: ItemStackRequestActionType
    request_buffer: bytes
    read_position: int

    def __init__(
        self,
        client_request_id: int = 0,
        strings_to_filter: List[bytes] = [],
        strings_to_filter_origin: int = 0,
        request_actions: List[ItemStackRequestAction] = [],
        is_parsable_action: bool = False,
        request_buffer: bytes = b"",
        read_position: int = 0,
    ):  # pylint: disable=dangerous-default-value
        self.client_request_id = client_request_id
        self.strings_to_filter = strings_to_filter
        self.strings_to_filter_origin = strings_to_filter_origin
        self.request_actions = request_actions
        self.is_parsable_action = is_parsable_action
        self.request_buffer = request_buffer
        self.read_position = read_position

    def write(self, stream: BinaryStream) -> None:
        if self.is_parsable_action is True:
            stream.write_varint(self.client_request_id)
            stream.write_unsigned_varint(len(self.request_actions))
            for action in self.request_actions:
                action.write(stream)
            stream.write_unsigned_varint(len(self.strings_to_filter))
            for stf in self.strings_to_filter:
                stream.write_bytes(stf)
            stream.write_signed_int(self.strings_to_filter_origin)
        else:
            stream.write_raw_bytes(self.request_buffer)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.is_parsable_action = True
        self.read_position = stream.get_position()
        self.client_request_id = stream.get_varint()
        actions_len = stream.get_unsigned_varint()
        for _ in range(actions_len):
            action = ItemStackRequestAction()
            action.read(stream)
            if action.action_data is not None:
                self.request_actions.append(action)
            else:
                self.is_parsable_action = False
                break
        if self.is_parsable_action is True:
            stf_len = stream.get_unsigned_varint()
            for _ in range(stf_len):
                self.strings_to_filter.append(stream.get_bytes())
            self.strings_to_filter_origin = stream.get_signed_int()
        else:
            stream.set_position(self.read_position)
            self.request_buffer = stream.get_left_buffer()


class ItemStackRequest:
    request_data: List[ItemStackRequestData]

    def __init__(
        self, request_data: List[ItemStackRequestData] = []
    ):  # pylint: disable=dangerous-default-value
        self.request_data = request_data

    def write(self, stream: BinaryStream) -> None:
        stream.write_unsigned_varint(len(self.request_data))
        for request in self.request_data:
            request.write(stream)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        length = stream.get_unsigned_varint()
        for _ in range(length):
            data = ItemStackRequestData()
            data.read(stream)
            self.request_data.append(data)
