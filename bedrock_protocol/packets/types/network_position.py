# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from ctypes import c_uint32, c_int32
from bstream import BinaryStream, ReadOnlyBinaryStream


class NetworkBlockPosition:
    x: int
    y: int
    z: int

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def write(self, stream: BinaryStream) -> None:
        stream.write_varint(self.x)
        stream.write_unsigned_varint(c_uint32(self.y).value)
        stream.write_varint(self.z)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.x = stream.get_varint()
        self.y = c_int32(stream.get_unsigned_varint()).value
        self.z = stream.get_varint()
