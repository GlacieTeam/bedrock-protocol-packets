# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream


class Vec3:
    x: float
    y: float
    z: float

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def write(self, stream: BinaryStream) -> None:
        stream.write_float(self.x)
        stream.write_float(self.y)
        stream.write_float(self.z)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.x = stream.get_float()
        self.y = stream.get_float()
        self.z = stream.get_float()
