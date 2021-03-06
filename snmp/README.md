# nav-add-ons/snmp

## Installation

Copy the [extra code](nav) to the NAV home directory.

Apply the [patches](patches).

Edit the `/etc/nav/ipdevpoll.conf` file:

```ini
[sensors:vendormibs]
...
D_LINK_SYSTEMS_INC =
    DES-1210-08P_BX
    DES-1210-28P_CX
    DGS-1210-10ME-AX
    DGS-1210-10ME-BX
    DGS-1210-10P_CX
    DGS-1210-10PME-AX
    DGS-1210-10PME-BX
    DGS-1210-12TSME-BX
    DGS-1210-20ME-BX
    DGS-1210-28ME-AX
    DGS-1210-28ME-BX
    DGS-1210-28XSME-BX
    DGS-1210-52ME-BX
    DDM-MGMT-MIB
    EQUIPMENT-MIB
EXTREME_NETWORKS =
    EXTREME-SYSTEM-MIB
MIKROTIK =
    MIKROTIK-MIB
NAG_LLC =
    NAG-MIB
TP_LINK_TECHNOLOGY_COLTD =
    TPLINK-POWER-OVER-ETHERNET-MIB
ZAO_LIGHT_COMMUNICATION =
    DKSF-60-4-X-X-X
ZYXEL_COMMUNICATIONS_CORP =
    ZYXEL-ES2024A-MIB
    ZYXEL-MES3528-MIB
...
```

## Metrics matrix

Legend for tables:

- `Yes` - implemented and verified
- `N/A` - implemented but not available on this device
- `X` - not available on this device
- empty cell - work in progress

### D-Link switches

| Device              | MIB  | CPU  | Memory | Power | Fans | Temperatures | DDM  | PoE
| :------------------ | :--- | :--- | :----- | :---- | :--- | :----------- | :--- | :---
| DES-1210-08P/B1     | [DES-1210-08P_BX](doc/D_Link_DES_1210_08P_BX_v3_12_004_mib.tree.txt) | | | | | | |
| DES-1210-28P/C2     | [DES-1210-28P_CX](doc/D_Link_DES_1210_28P_CX_4_12_004_mib.tree.txt) | | | | | | |
| DES-3200-26         | [AGENT-GENERAL-MIB](doc/D_Link_Genmgmt_mib.tree.txt) | Yes | | | X | X | X | X
| DES-3200-28         |      |      |        |       |      |              |      |
| DES-3200-28/C1      | [AGENT-GENERAL-MIB](doc/D_Link_Genmgmt_mib.tree.txt)<br>[DDM-MGMT-MIB](doc/D_Link_DDM_mib.tree.txt)<br>[EQUIPMENT-MIB](doc/EQUIPMENT-MIB) | Yes | | | X | | Yes | X
| DGS-1210-10/ME/A1   | [DGS-1210-10ME-AX](doc/D_Link_DGS_1210_10ME_AX_6_14_001_mib.tree.txt) | | | | | | |
| DGS-1210-10P/C1     | [DGS-1210-10P_CX](doc/D_Link_DGS_1210_10P_CX_4_10_002_mib.tree.txt) | | | | | | |
| DGS-1210-10P/ME/A1  | [DGS-1210-10PME-AX](doc/D_Link_DGS_1210_10PME_AX_6_13_017_mib.tree.txt) | | | | | | |
| DGS-1210-10P/ME/B1  | [DGS-1210-10PME-BX](doc/D_Link_DGS_1210_10PME_BX_7_02_017_mib.tree.txt) | | | | | | |
| DGS-1210-12TS/ME/B1 | [DGS-1210-12TSME-BX](doc/D_Link_DGS_1210_12TSME_BX_7_03_001_mib.tree.txt) | | | | | | |
| DGS-1210-20/ME/B1   | [DGS-1210-20ME-BX](doc/D_Link_DGS_1210_20ME_BX_7_03_001_mib.tree.txt) | | | | | | |
| DGS-1210-28/ME/A2   | [DGS-1210-28ME-AX](doc/D_Link_DGS_1210_28ME_AX_6_14_001_mib.tree.txt) | | | | | | |
| DGS-1210-28/ME/B1   | [DGS-1210-28ME-BX](doc/D_Link_DGS_1210_28ME_BX_7_03_001_mib.tree.txt) | | | | | | |
| DGS-1210-28XS/ME/B1 | [DGS-1210-28XSME-BX](doc/D_Link_DGS_1210_28XSME_BX_7_03_001_mib.tree.txt) | | | | Yes | X | |
| DGS-1210-52/ME/B1   | [DGS-1210-52ME-BX](doc/D_Link_DGS_1210_52ME_BX_7_02_017_mib.tree.txt) | | | | Yes | Yes | |
| DGS-1510-28X/ME     |      |      |        |       |      |              |      |
| DGS-1510-28XS/ME    |      |      |        |       |      |              |      |
| DGS-3000-28XS       |      |      |        |       |      |              |      |
| DGS-3120-24SC       |      |      |        |       |      |              |      |
| DGS-3420-28SC       |      |      |        |       |      |              |      |
| DXS-1210-12SC       |      |      |        |       |      |              |      |

### Extreme Networks

| Device              | MIB  | CPU  | Memory | Power | Fans | Temperatures | PoE
| :------------------ | :--- | :--- | :----- | :---- | :--- | :----------- | :---
| X670-48x | [EXTREME-SOFTWARE-MONITOR-MIB](doc/Extreme_Networks_EXTREME_SOFTWARE_MONITOR_MIB_mib.tree.txt)<br>[EXTREME-SYSTEM-MIB](doc/Extreme_Networks_EXTREME_SYSTEM_MIB_mib.tree.txt) | Yes | Yes | Yes | Yes | Yes | X

There are no DDM metrics available via SNMP.

### MikroTik

All `mtxrHealth` sensors as of version 20191210 of [MIKROTIK-MIB](doc/MikroTik_mikrotik_mib.tree.txt) are implemented.

### NAG switches

| Device         | MIB  | CPU | Memory | Power |Fans | Temperatures | DDM  | PoE
| :------------- | :--- |:----| :----- | :---- |:--- | :----------- | :--- | :---
| SNR-S2985G-8T  |      |     |        |       |     |              |      |
| SNR-S2985G-24T | [NAG-MIB](doc/NAG_SNR_SWITCH_private_2_1_80_mib.tree.txt) | Yes | Yes | | N/A | N/A | Yes | N/A

### NetPing

All `npThermo` sensors as of version 20160114 of [DKSF-60-4-X-X-X](doc/NetPing_DKSF_60_5_2_MB_mib.tree.txt) are implemented.

### TP-Link switches

| Device       | MIB  | CPU | Memory | Power |Fans | Temperatures | DDM  | PoE
| :----------- | :--- | :---| :----- | :---- |:--- | :----------- | :--- | :---
| T1500G-10MPS | [TPLINK-SYSMONITOR-MIB](doc/TP_Link_tplink_sysMonitor_mib.tree.txt)<br>[TPLINK-POWER-OVER-ETHERNET-MIB](doc/TP_Link_tplink_powerOverEthernet_mib.tree.txt) | Yes | Yes | X | X | X | X | Yes

### ZyXEL switches

| Device       | MIB  | CPU | Memory | Power |Fans | Temperatures | DDM  | PoE
| :----------- | :--- | :---| :----- | :---- |:--- | :----------- | :--- | :---
| ES-2024A | [ZYXEL-ES2024A-MIB](doc/ZyXEL_390TX3C0_mib.tree.txt) | Yes | Yes | X | X | X | X | X
| MES-3528 | [ZYXEL-MES3528-MIB](doc/ZyXEL_390BHR5C0_mib.tree.txt) | Yes | X | X | X | X | X | X
