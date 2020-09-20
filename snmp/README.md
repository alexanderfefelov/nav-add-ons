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

Change the `nav/ipdevpoll/plugins/statsystem.py` file manually:

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

### D-Link switches

| Device              | CPU  | Memory | Fans | Temperatures | DDM  | PoE
| :------------------ | :--- | :----- | :--- | :----------- | :--- | :---
| DES-3200-26         |      |        |      |              |      |
| DES-3200-28         |      |        |      |              |      |
| DES-1210-08P        |      |        |      |              |      |
| DES-1210-28P        |      |        |      |              |      |
| DES-3200-28/C1      |      |        |      |              |      |
| DGS-1210-10P/C1     |      |        |      |              |      |
| DGS-1210-10P/ME/A1  |      |        |      |              |      |
| DGS-1210-10P/ME/B1  |      |        |      |              |      |
| DGS-1210-28/ME/B1   |      |        |      |              |      |
| DGS-1210-28XS/ME/B1 |      |        |      |              |      |
| DGS-1210-52/ME/B1   |      |        |      |              |      |
| DGS-1210-52/ME/B1   |      |        |      |              |      |
| DGS-1210-52/ME/B1   |      |        |      |              |      |
| DGS-1510-28X/ME     |      |        |      |              |      |
| DGS-1510-28XS/ME    |      |        |      |              |      |
| DGS-3000-28XS       |      |        |      |              |      |
| DGS-3120-24SC       |      |        |      |              |      |
| DGS-3420-28SC       |      |        |      |              |      |
| DXS-1210-12SC       |      |        |      |              |      |

Legend:

- `Yes` - implemented
- `N/A` - implemented but not available on this device
- empty cell - work in progress

### MikroTik

All health sensors as of version 20191210 of MIKROTIK-MIB are implemented.

### NAG switches

| Device         | CPU  | Memory | Fans | Temperatures | DDM  | PoE
| :--------------| :----| :----- | :--- | :----------- | :--- | :---
| SNR-S2985G-8T  |      |        |      |              |      |    
| SNR-S2985G-24T | Yes  | Yes    | N/A  | N/A          | Yes  | N/A

Legend:

- `Yes` - implemented
- `N/A` - implemented but not available on this device
- empty cell - work in progress

### TP-Link switches

| Device       | CPU  | Memory | Fans | Temperatures | DDM  | PoE
| :------------| :----| :----- | :--- | :----------- | :--- | :---
| T1500G-10MPS |      |        |      |              |      |     

Legend:

- `Yes` - implemented
- `N/A` - implemented but not available on this device
- empty cell - work in progress
