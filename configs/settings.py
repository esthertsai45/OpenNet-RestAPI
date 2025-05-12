import logging
from enum import Enum
from typing import Optional

from configs.config import STG, AutomationConfig

logger = logging.getLogger(__name__)


class AutomationEnvEnums(str, Enum):
    STG = "STG"
    PRD = "PRD"


class AutomationSettings:
    env: Optional[AutomationEnvEnums] = None
    config: Optional[AutomationConfig] = None

    @classmethod
    def init(cls, env: AutomationEnvEnums):
        cls.env = env
        cls.config = cls.get_config(env)
        logging.info(f"[AutomationSettings] Initialized with env={env}")

    @classmethod
    def get_config(cls, env: AutomationEnvEnums) -> AutomationConfig:
        env_mapping = {
            AutomationEnvEnums.STG.value: STG
        }
        return AutomationConfig(env_mapping.get(env, STG))
