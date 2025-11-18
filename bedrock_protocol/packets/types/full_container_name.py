# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from typing import Optional
from bstream import BinaryStream, ReadOnlyBinaryStream


class FullContainerName:
    container_enum: int
    dynamic_slot: Optional[int]

    def __init__(self, container_enum: int = 0, dynamic_slot: Optional[int] = None):
        self.container_enum = container_enum
        self.dynamic_slot = dynamic_slot

    def write(self, stream: BinaryStream) -> None:
        stream.write_byte(self.container_enum)
        stream.write_bool(self.dynamic_slot is None)
        if self.dynamic_slot is not None:
            stream.write_unsigned_int(self.dynamic_slot)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.container_enum = stream.get_byte()
        if stream.get_bool() is True:
            self.dynamic_slot = stream.get_unsigned_int()
