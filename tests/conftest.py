import sys

import mock
import pytest
from tools import SMBusFakeDevice


@pytest.fixture()
def smbus_not_present():
    sys.modules['smbus2'] = mock.MagicMock()
    yield sys.modules['smbus2']
    del sys.modules['smbus2']


@pytest.fixture()
def smbus():
    sys.modules['smbus2'] = mock.MagicMock()
    sys.modules['smbus2'].SMBus = SMBusFakeDevice
    yield sys.modules['smbus2']
    del sys.modules['smbus2']


@pytest.fixture()
def LSM6DS3():
    import LSM6DS3
    yield LSM6DS3
    del sys.modules['LSM6DS3']
