import logging

import pytest

from configs.settings import AutomationSettings, AutomationEnvEnums

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="setup environment; STG, PRD",
        default="STG",
    )


@pytest.fixture(scope="session", autouse=True)
def default_setup(request: pytest.FixtureRequest):
    env_str = request.config.getoption("--env", default="STG").upper()
    AutomationSettings.init(AutomationEnvEnums[env_str])
    yield AutomationSettings
