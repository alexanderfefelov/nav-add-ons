from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DGS_1210_10_ME_AX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_10ME_AX_6_14_001_mib')
    GET_DDM_SENSORS = 'get_ddm_sensors'
