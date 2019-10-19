import unittest

from demag import MagneticDeclination


class TestIGRFOnline(unittest.TestCase):
    """Testing NOAA IGRF online"""

    def setUp(self):
        self.md_object = MagneticDeclination()

    def test_incorrect(self):
        """Date is out of IGRF model"""
        with self.assertRaises(RuntimeError):
            self.md_object.md(year=100, mon=1, day=25, provider="NOAA_IGRF")

    def test_N0_E0(self):
        """IGRF 0 0 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0, lat=0, year=2015, mon=10, day=15, provider="NOAA_IGRF"
            ),
            -5.338,
            delta=0.01,
        )

    def test_N0_W45(self):
        """IGRF N0 W45 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-45.0,
                lat=0.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -20.34,
            delta=0.01,
        )

    def test_N0_W180(self):
        """IGRF N0 W180 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-180.0,
                lat=0.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            9.58,
            delta=0.01,
        )

    def test_N0_E90(self):
        """IGRF N0 E90 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=90.0,
                lat=0.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -2.03,
            delta=0.01,
        )

    def test_N0_E180(self):
        """IGRF N0 E180 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=180.0,
                lat=0.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            9.58,
            delta=0.01,
        )

    def test_N45_E0(self):
        """IGRF N45 E0 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=45.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -0.15,
            delta=0.01,
        )

    def test_N90_E0(self):
        """IGRF N90 E0 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=90.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -4.55,
            delta=0.01,
        )

    def test_S45_E0(self):
        """IGRF S45 E0 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=-45.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -22.21,
            delta=0.01,
        )

    def test_S90_E0(self):
        """IGRF S90 E0 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=-90.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -30.14,
            delta=0.01,
        )

    def test_N45_E90(self):
        """IGRF N45 E90 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=90.0,
                lat=45.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            2.36,
            delta=0.01,
        )

    def test_N45_W90(self):
        """IGRF N45 W90 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=45.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -2.36,
            delta=0.01,
        )

    def test_S45_E90(self):
        """IGRF S45 E90 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=90.0,
                lat=-45.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -41.67,
            delta=0.01,
        )

    def test_S45_W90(self):
        """IGRF S45 W90 2015-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=-45.0,
                year=2015,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            21.46,
            delta=0.01,
        )

    def test_S45_W90_1590(self):
        """IGRF S45 W90 1590-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=-45.0,
                year=1590,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            -0.24,
            delta=0.01,
        )

    def test_S45_W90_1790(self):
        """IGRF S45 W90 1790-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=-45.0,
                year=1790,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            13.84,
            delta=0.01,
        )

    def test_S45_W90_1990(self):
        """IGRF S45 W90 1990-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=-45.0,
                year=1990,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            22.36,
            delta=0.01,
        )

    def test_S45_W90_2007(self):
        """IGRF S45 W90 2007-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=-45.0,
                year=2007,
                mon=10,
                day=15,
                provider="NOAA_IGRF",
            ),
            21.80,
            delta=0.01,
        )
