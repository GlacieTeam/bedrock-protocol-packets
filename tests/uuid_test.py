# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from bedrock_protocol.packets.types import UUID

if __name__ == "__main__":
    # Test example 550e8432-e29b-41d4-a716-1c45261af03b
    uuid = UUID.from_string("550e8432-e29b-41d4-a716-1c45261af03b")
    print(
        f"{uuid.to_string()} | {uuid.to_string()=='550e8432-e29b-41d4-a716-1c45261af03b'}"
    )
