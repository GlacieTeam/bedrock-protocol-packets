# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bstream import BinaryStream, ReadOnlyBinaryStream


class UUID:
    high: int
    low: int

    def __init__(self, high: int = 0, low: int = 0):
        self.high = high & 0xFFFFFFFFFFFFFFFF
        self.low = low & 0xFFFFFFFFFFFFFFFF

    def write(self, stream: BinaryStream) -> None:
        stream.write_unsigned_int64(self.high)
        stream.write_unsigned_int64(self.low)

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        self.high = stream.get_unsigned_int64()
        self.low = stream.get_unsigned_int64()

    def to_string(self) -> str:
        high_hex = format(self.high, "016x")
        low_hex = format(self.low, "016x")
        return f"{high_hex[0:8]}-{high_hex[8:12]}-{high_hex[12:16]}-{low_hex[0:4]}-{low_hex[4:16]}"

    @staticmethod
    def from_string(uuid: str) -> "UUID":
        hex_str = "".join(c for c in uuid if c in "0123456789abcdefABCDEF")
        if len(hex_str) != 32:
            raise ValueError(f"Invalid UUID string: {uuid}")
        hex_str = hex_str.lower()
        return UUID(int(hex_str[0:16], 16), int(hex_str[16:32], 16))
