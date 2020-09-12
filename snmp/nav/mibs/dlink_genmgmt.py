from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
from twisted.internet import defer


class DLinkGenmgmtMib(MibRetriever):
    mib = get_mib('D_Link_Genmgmt_mib')

    @defer.inlineCallbacks
    def get_cpu_loadavg(self):
        utilization1 = yield self.get_next('agentCPUutilizationIn1min')
        utilization5 = yield self.get_next('agentCPUutilizationIn5min')
        if utilization1 or utilization5:
            result = dict(cpu=[
                (1, utilization1),
                (5, utilization5)
            ])
            defer.returnValue(result)

    def get_cpu_utilization(self):
        return defer.succeed(None)
