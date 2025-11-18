# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream
from rapidnbt import CompoundTag


class ItemData:
    item_name: str
    item_id: int
    is_component_based: bool
    item_version: int
    component_data: CompoundTag

    def __init__(
        self,
        item_name: str = "",
        item_id: int = 0,
        is_component_based: bool = False,
        item_version: int = 0,
        component_data: CompoundTag | None = None,
    ):
        self.item_name = item_name
        self.item_id = item_id
        self.is_component_based = is_component_based
        self.item_version = item_version
        self.component_data = component_data or CompoundTag()

    def write(self, stream: BinaryStream) -> None:
        stream.write_string(self.item_name)
        stream.write_signed_short(self.item_id)
        stream.write_bool(self.is_component_based)
        stream.write_varint(self.item_version)
        self.component_data.serialize(stream)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.item_name = stream.get_string()
        self.item_id = stream.get_signed_short()
        self.is_component_based = stream.get_bool()
        self.item_version = stream.get_varint()
        self.component_data.deserialize(stream)
