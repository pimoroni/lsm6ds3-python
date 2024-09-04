TEST_STEP_COUNT = 1365


def test_get_steps(smbus, LSM6DS3):
    dev = smbus.SMBus(1)

    dev.regs[0x4B] = TEST_STEP_COUNT & 0xFF  # STEP_COUNTER_L
    dev.regs[0x4C] = (TEST_STEP_COUNT >> 8) & 0xFF  # STEP_COUNTER_H

    sensor = LSM6DS3.LSM6DS3(dev)

    s = sensor.get_step_count()

    assert s == TEST_STEP_COUNT


def test_single_tap(smbus, LSM6DS3):
    dev = smbus.SMBus(1)

    dev.regs[0x1C] = (1 << 5)

    sensor = LSM6DS3.LSM6DS3(dev)

    assert sensor.single_tap_detected() == 1


def test_double_tap(smbus, LSM6DS3):
    dev = smbus.SMBus(1)

    dev.regs[0x1C] = (1 << 4)

    sensor = LSM6DS3.LSM6DS3(dev)

    assert sensor.double_tap_detected() == 1


def test_free_fall(smbus, LSM6DS3):
    dev = smbus.SMBus(1)

    dev.regs[0x1B] = (1 << 5)

    sensor = LSM6DS3.LSM6DS3(dev)

    assert sensor.freefall_detected() == 1


def test_tilt(smbus, LSM6DS3):
    dev = smbus.SMBus(1)

    dev.regs[0x53] = (1 << 5)

    sensor = LSM6DS3.LSM6DS3(dev)

    assert sensor.tilt_detected() == 1


def test_sig_motion(smbus, LSM6DS3):
    dev = smbus.SMBus(1)

    dev.regs[0x53] = (1 << 6)

    sensor = LSM6DS3.LSM6DS3(dev)

    assert sensor.sig_motion_detected() == 1
