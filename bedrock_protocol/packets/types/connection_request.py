# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

import json
import base64
from typing import Any, Dict, List
from bstream import BinaryStream, ReadOnlyBinaryStream
from bedrock_protocol.packets.enums.authentication_type import AuthenticationType


class ConnectionRequest:
    login_type: AuthenticationType
    certificate: str
    token: str
    client_properties: str

    def __init__(
        self,
        login_type: AuthenticationType = AuthenticationType.FULL,
        chains: str = "",
        token: str = "",
        client_properties: str = "",
    ):
        self.login_type = login_type
        self.certificate = chains
        self.token = token
        self.client_properties = client_properties

    def write(self, stream: BinaryStream) -> None:
        auth_json = {
            "AuthenticationType": self.login_type,
            "Certificate": self.certificate,
            "Token": self.token,
        }
        request_stream = BinaryStream()
        request_stream.write_long_string(json.dumps(auth_json, separators=(",", ":")))
        request_stream.write_long_string(self.client_properties)
        stream.write_bytes(request_stream.get_and_release_data())

    def read(self, stream: ReadOnlyBinaryStream) -> None:
        request_stream = ReadOnlyBinaryStream(stream.get_bytes())
        try:
            auth_json = json.loads(request_stream.get_long_string())
            self.login_type = auth_json["AuthenticationType"]
            self.certificate = auth_json["Certificate"]
            self.token = auth_json["Token"]
        except:  # pylint:disable=bare-except
            pass
        self.client_properties = request_stream.get_long_string()

    def get_login_chains(self) -> List[str]:
        try:
            chain_json = json.loads(self.certificate)
            result = chain_json["chain"]
            if isinstance(result, list):
                return result
            return []
        except:  # pylint:disable=bare-except
            return []

    def get_client_properties_json(self) -> Dict[str, Any]:
        parts = self.client_properties.split(".")
        if len(parts) == 3:
            payload = parts[1]
            padding = "=" * ((4 - len(payload) % 4) % 4)
            try:
                return json.loads(base64.urlsafe_b64decode(payload + padding))
            except:  # pylint:disable=bare-except
                return {}
        return {}
