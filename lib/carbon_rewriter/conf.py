from carbon.conf import join,settings,CarbonCacheOptions

settings.update({ "REWRITER_RULES" : "rewriter-rules.conf" })

class CarbonRewriterOptions(CarbonCacheOptions):
    optParameters = [
        ["rewriter-rules", "", None, "Use the given rewriter rules file."]
    ] + CarbonCacheOptions.optParameters

    def postOption(self):
        CarbonCacheOptions.postOptions(self)

        if self["rewriter-rules"] is None:
            self["rewriter-rules"] = join(settings["CONF_DIR"],settings["REWRITER_RULES"])
        settings["rewriter-rules"] = self["rewriter-rules"]


