from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DGS_1210_28_ME_BX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_28ME_BX_7_03_001_mib')
    GUARD_OID = 'dgs-1210-28mebx'
    GET_DDM_SENSORS = 'get_ddm_sensors'
