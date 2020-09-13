# nav-add-ons/snmp

`/etc/nav/ipdevpoll.conf`:

```ini
[sensors:vendormibs]
...
D_LINK_SYSTEMS_INC = DLinkSensorsMib
MIKROTIK = MikroTikMikrotikMib
...
```

`nav/ipdevpoll/plugins/statsystem.py`:

```python
...
from nav.mibs.dlink_dgs_1210_xx import (
    DLink_DGS_1210_10_ME_AX_Mib,
    DLink_DGS_1210_10_ME_BX_Mib,
    DLink_DGS_1210_10_P_CX_Mib,
    DLink_DGS_1210_10_P_ME_AX_Mib,
    DLink_DGS_1210_10_P_ME_BX_Mib,
    DLink_DGS_1210_12_TS_ME_BX_Mib,
    DLink_DGS_1210_28_ME_AX_Mib,
    DLink_DGS_1210_28_ME_BX_Mib,
    DLink_DGS_1210_28_XS_ME_BX_Mib,
    DLink_DGS_1210_52_ME_BX_Mib
)
from nav.mibs.dlink_genmgmt import DLinkGenmgmtMib
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
        DLinkGenmgmtMib
    ],
    ...
}
...
```
