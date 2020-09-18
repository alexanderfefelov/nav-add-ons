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
from nav.mibs.dlink_genmgmt import DLinkGenmgmtMib
...
from nav.enterprise.ids import (...
                                VENDOR_ID_D_LINK_SYSTEMS_INC,
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
    ...
}
...
```

or apply appropriate [patch](patches).
