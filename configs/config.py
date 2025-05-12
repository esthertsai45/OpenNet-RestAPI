import logging
import dataclasses

logger = logging.getLogger(__name__)

@dataclasses.dataclass
class AutomationEnvConfigs:
    disify_domain: str
    


class AutomationConfig:
    def __init__(self, env: AutomationEnvConfigs):
        self._disify_domain = env.disify_domain


    @property
    def disify_domain(self) -> str:
        return self._disify_domain


STG = AutomationEnvConfigs(
    disify_domain="https://disify.com/",
)
