# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.binarystream import BinaryStream, ReadOnlyBinaryStream


class UUID:
    most_significant_bits: int
    least_significant_bits: int

    def __init__(self, high: int = 0, low: int = 0):
        self.most_significant_bits = high
        self.least_significant_bits = low

    def write(self, stream: BinaryStream):
        stream.write_unsigned_int64(self.most_significant_bits)
        stream.write_unsigned_int64(self.least_significant_bits)

    def read(self, stream: ReadOnlyBinaryStream):
        self.most_significant_bits = stream.get_unsigned_int64()
        self.least_significant_bits = stream.get_unsigned_int64()
