# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from enum import IntEnum


# pylint: disable=invalid-name
class ItemStackRequestActionType(IntEnum):
    Invalid = -1
    Take = 0
    Place = 1
    Swap = 2
    Drop = 3
    Destroy = 4
    Consume = 5
    Create = 6
    PlaceInItemContainerDeprecated = 7
    TakeFromItemContainerDeprecated = 8
    LabTableCombine = 9
    BeaconPayment = 10
    MineBlock = 11
    CraftRecipe = 12
    CraftRecipeAuto = 13
    CraftCreative = 14
    CraftRecipeOptional = 15
    CraftGrindStone = 16
    CraftLoom = 17
    CraftNonImplemented = 18
    CraftResults = 19
