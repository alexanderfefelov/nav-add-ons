# nav-add-ons/snmp

## Installation

Edit the `/etc/nav/ipdevpoll.conf` file:

```ini
[sensors:vendormibs]
...
D_LINK_SYSTEMS_INC =
    DLink_DES_1210_08_P_BX_Mib
    DLink_DES_1210_28_P_CX_Mib
    DLink_DGS_1210_10_ME_AX_Mib
    DLink_DGS_1210_10_ME_BX_Mib
    DLink_DGS_1210_10_P_CX_Mib
    DLink_DGS_1210_10_P_ME_AX_Mib
    DLink_DGS_1210_10_P_ME_BX_Mib
    DLink_DGS_1210_12_TS_ME_BX_Mib
    DLink_DGS_1210_28_ME_AX_Mib
    DLink_DGS_1210_28_ME_BX_Mib
    DLink_DGS_1210_28_XS_ME_BX_Mib
    DLink_DGS_1210_52_ME_BX_Mib
    DLink_Ddm_Mib
    DLink_Equipment_Mib
MIKROTIK = MikroTik_Mikrotik_Mib
NAG_LLC = Nag_Nag_Mib
...
```

Change the `nav/ipdevpoll/plugins/statsystem.py` file:

```python
...
from nav.mibs.dlink_dgs_1210_10_me_ax import DLink_DGS_1210_10_ME_AX_Mib
from nav.mibs.dlink_dgs_1210_10_me_bx import DLink_DGS_1210_10_ME_BX_Mib
from nav.mibs.dlink_dgs_1210_10_p_cx import DLink_DGS_1210_10_P_CX_Mib
from nav.mibs.dlink_dgs_1210_10_p_me_ax import DLink_DGS_1210_10_P_ME_AX_Mib
from nav.mibs.dlink_dgs_1210_10_p_me_bx import DLink_DGS_1210_10_P_ME_BX_Mib
from nav.mibs.dlink_dgs_1210_12_ts_me_bx import DLink_DGS_1210_12_TS_ME_BX_Mib
from nav.mibs.dlink_dgs_1210_28_me_ax import DLink_DGS_1210_28_ME_AX_Mib
from nav.mibs.dlink_dgs_1210_28_me_bx import DLink_DGS_1210_28_ME_BX_Mib
from nav.mibs.dlink_dgs_1210_28_xs_me_bx import DLink_DGS_1210_28_XS_ME_BX_Mib
from nav.mibs.dlink_dgs_1210_52_me_bx import DLink_DGS_1210_52_ME_BX_Mib
from nav.mibs.dlink_genmgmt import DLink_Genmgmt_Mib
from nav.mibs.nag_nag import Nag_Nag_Mib
...
from nav.enterprise.ids import (...
                                VENDOR_ID_D_LINK_SYSTEMS_INC,
                                VENDOR_ID_NAG_LLC,
                                ...)
...
CPU_MIBS = {
    ...
    VENDOR_ID_D_LINK_SYSTEMS_INC: [
        DLink_DGS_1210_10_ME_AX_Mib,
        DLink_DGS_1210_10_ME_BX_Mib,
        DLink_DGS_1210_10_P_CX_Mib,
        DLink_DGS_1210_10_P_ME_AX_Mib,
        DLink_DGS_1210_10_P_ME_BX_Mib,
        DLink_DGS_1210_12_TS_ME_BX_Mib,
        DLink_DGS_1210_28_ME_AX_Mib,
        DLink_DGS_1210_28_ME_BX_Mib,
        DLink_DGS_1210_28_XS_ME_BX_Mib,
        DLink_DGS_1210_52_ME_BX_Mib,
        DLink_Genmgmt_Mib
    ],
    VENDOR_ID_NAG_LLC: [
        Nag_Nag_Mib
    ],
    ...
}
...
MEMORY_MIBS = {
    ...
    VENDOR_ID_NAG_LLC: [
        Nag_Nag_Mib
    ],
    ...
}

```

## Metrics matrix

Legend for tables:

- `Yes` - implemented and verified
- `N/A` - implemented but not available on this device
- `X` - not available on this device
- empty cell - work in progress

### D-Link switches

| Device              | MIB  | CPU  | Memory | Fans | Temperatures | DDM  | PoE
| :------------------ | :--- | :--- | :----- | :--- | :----------- | :--- | :---
| DES-1210-08P/B1     | [DES-1210-08P_BX](doc/D_Link_DES_1210_08P_BX_v3_12_004_mib.tree.txt) | | | | | |
| DES-1210-28P/C2     | [DES-1210-28P_CX](doc/D_Link_DES_1210_28P_CX_4_12_004_mib.tree.txt) | | | | | |
| DES-3200-26         |      |      |        |      |              |      |
| DES-3200-28         |      |      |        |      |              |      |
| DES-3200-28/C1      |      |      |        |      |              |      |
| DGS-1210-10P/C1     | [DGS-1210-10P_CX](doc/D_Link_DGS_1210_10P_CX_4_10_002_mib.tree.txt) | | | | | |
| DGS-1210-10P/ME/A1  | [DGS-1210-10PME-AX](doc/D_Link_DGS_1210_10PME_AX_6_13_017_mib.tree.txt) | | | | | |
| DGS-1210-10P/ME/B1  | [DGS-1210-10PME-BX](doc/D_Link_DGS_1210_10PME_BX_7_02_017_mib.tree.txt) | | | | | |
| DGS-1210-28/ME/B1   | [DGS-1210-28ME-BX](doc/D_Link_DGS_1210_28ME_BX_7_03_001_mib.tree.txt) | | | | | |
| DGS-1210-28XS/ME/B1 | [DGS-1210-28XSME-BX](doc/D_Link_DGS_1210_28XSME_BX_7_03_001_mib.tree.txt) | | | Yes | X | |
| DGS-1210-52/ME/B1   | [DGS-1210-52ME-BX](doc/D_Link_DGS_1210_52ME_BX_7_02_017_mib.tree.txt) | | | Yes | Yes | |
| DGS-1510-28X/ME     |      |      |        |      |              |      |
| DGS-1510-28XS/ME    |      |      |        |      |              |      |
| DGS-3000-28XS       |      |      |        |      |              |      |
| DGS-3120-24SC       |      |      |        |      |              |      |
| DGS-3420-28SC       |      |      |        |      |              |      |
| DXS-1210-12SC       |      |      |        |      |              |      |

### MikroTik

All health sensors as of version 20191210 of [MIKROTIK-MIB](doc/MikroTik_mikrotik_mib.tree.txt) are implemented.

### NAG switches

| Device         | MIB  | CPU | Memory | Fans | Temperatures | DDM  | PoE
| :--------------| :--- |:----| :----- | :--- | :----------- | :--- | :---
| SNR-S2985G-8T  |      |     |        |      |              |      |    
| SNR-S2985G-24T | [NAG-MIB](doc/NAG_SNR_SWITCH_private_2_1_80_mib.tree.txt) | Yes | Yes | N/A | N/A | Yes | N/A

### TP-Link switches

| Device       | MIB  | CPU | Memory | Fans | Temperatures | DDM  | PoE
| :------------| :--- | :---| :----- | :--- | :----------- | :--- | :---
| T1500G-10MPS |      |     |        |      |              |      |     
