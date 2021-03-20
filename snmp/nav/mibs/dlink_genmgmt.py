from nav.mibs.dlink import DLink
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_Genmgmt_Mib(MibRetriever, DLink):
    mib = get_mib('D_Link_Genmgmt_mib')
    GUARD_OID = 'agentGeneralMgmt'
