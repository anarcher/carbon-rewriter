from zope.interface import implements

from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker

from carbon_rewriter import service
from carbon_rewriter import conf

class CarbonRewriterServiceMaker(object):
    implements(IServiceMaker,IPlugin)
    tapname="carbon-rewriter"
    description="Metric name rewriter for graphite."
    options = conf.CarbonRewriterOptions

    def makeService(self,options):
        return service.createRewriterService(options)


serviceMaker = CarbonRewriterServiceMaker()


