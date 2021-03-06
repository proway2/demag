import unittest

from demag import MagneticDeclination


class TestWMMOnline(unittest.TestCase):
    """Testing NOAA WMM online"""

    def setUp(self):
        self.md_object = MagneticDeclination()

    def test_incorrect(self):
        """Date is out of WMM model's range"""
        with self.assertRaises(RuntimeError):
            self.md_object.md(year=2000, mon=1, day=25)

    def test_N0_E0(self):
        """WMM 0 0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=0, lat=0, year=2020, mon=10, day=15),
            -4.54,
            delta=0.01,
        )

    def test_N0_W45(self):
        """WMM N0 W45 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=-45.0, lat=0.0, year=2020, mon=10, day=15),
            -20.18,
            delta=0.01,
        )

    def test_N0_W180(self):
        """WMM N0 W180 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=-180.0, lat=0.0, year=2020, mon=10, day=15),
            9.78,
            delta=0.01,
        )

    def test_N0_E90(self):
        """WMM N0 E90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=90.0, lat=0.0, year=2020, mon=10, day=15),
            -1.90,
            delta=0.01,
        )

    def test_N0_E180(self):
        """WMM N0 E180 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=180.0, lat=0.0, year=2020, mon=10, day=15),
            9.78,
            delta=0.01,
        )

    def test_N45_E0(self):
        """WMM N45 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=0.0, lat=45.0, year=2020, mon=10, day=15),
            0.69,
            delta=0.01,
        )

    def test_N90_E0(self):
        """WMM N90 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=0.0, lat=90.0, year=2020, mon=10, day=15),
            5.28,
            delta=0.01,
        )

    def test_S45_E0(self):
        """WMM S45 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=0.0, lat=-45.0, year=2020, mon=10, day=15),
            -21.74,
            delta=0.01,
        )

    def test_S90_E0(self):
        """WMM S90 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=0.0, lat=-90.0, year=2020, mon=10, day=15),
            -30.85,
            delta=0.01,
        )

    def test_N45_E90(self):
        """WMM N45 E90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=90.0, lat=45.0, year=2020, mon=10, day=15),
            2.09,
            delta=0.01,
        )

    def test_N45_W90(self):
        """WMM N45 W90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=-90.0, lat=45.0, year=2020, mon=10, day=15),
            -2.54,
            delta=0.01,
        )

    def test_S45_E90(self):
        """WMM S45 E90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=90.0, lat=-45.0, year=2020, mon=10, day=15),
            -41.08,
            delta=0.01,
        )

    def test_S45_W90(self):
        """WMM S45 W90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(lon=-90.0, lat=-45.0, year=2020, mon=10, day=15),
            21.15,
            delta=0.01,
        )
