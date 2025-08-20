# bedrock-protocol-packets
Part of Bedrock Protocol Library. Minecraft Bedrock Packets Codec Library.

## Install
```bash
pip install bedrock-protocol-packets
```

## Usage
```Python
from bedrock_protocol.packets import UpdateBlockPacket

# Serialize Packet
packet_write = UpdateBlockPacket(NetworkBlockPosition(11, 45, 14), 2537812, 3, 0)
payload = packet_write.serialize()

# Deserialize Packet
packet_read = UpdateBlockPacket()
packet_read.deserialize(bytes.fromhex("162d1cadd9010301"))
```

## License
This project is licensed under the **Mozilla Public License 2.0 (MPL-2.0)**.  

### Key Requirements:
- **Modifications to this project's files** must be released under MPL-2.0.  
- **Using this library in closed-source projects** is allowed (no requirement to disclose your own code).  
- **Patent protection** is explicitly granted to all users.  

For the full license text, see [LICENSE](LICENSE) file or visit [MPL 2.0 Official Page](https://www.mozilla.org/en-US/MPL/2.0/).  

---


### Copyright © 2025 GlacieTeam. All rights reserved.