import unittest

from demag import MagneticDeclination


class TestBGSWMMOnline(unittest.TestCase):
    """Testing BGS WMM online"""

    def setUp(self):
        self.md_object = MagneticDeclination()

    def test_incorrect(self):
        """Date is out of WMM model's range"""
        with self.assertRaises(RuntimeError):
            self.md_object.md(year=2000, mon=1, day=25, provider="BGS_WMM")

    def test_N0_E0(self):
        """WMM 0 0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0, lat=0, year=2020, mon=10, day=15, provider="BGS_WMM"
            ),
            -4.54,
            delta=0.01,
        )

    def test_N0_W45(self):
        """WMM N0 W45 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-45.0,
                lat=0.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            -20.186,
            delta=0.01,
        )

    def test_N0_W180(self):
        """WMM N0 W180 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-180.0,
                lat=0.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            9.781,
            delta=0.01,
        )

    def test_N0_E90(self):
        """WMM N0 E90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=90.0,
                lat=0.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            -1.909,
            delta=0.01,
        )

    def test_N0_E180(self):
        """WMM N0 E180 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=180.0,
                lat=0.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            9.78,
            delta=0.01,
        )

    def test_N45_E0(self):
        """WMM N45 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=45.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            0.69,
            delta=0.01,
        )

    def test_N90_E0(self):
        """WMM N90 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=90.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            5.286,
            delta=0.01,
        )

    def test_S45_E0(self):
        """WMM S45 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=-45.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            -21.743,
            delta=0.01,
        )

    def test_S90_E0(self):
        """WMM S90 E0 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=0.0,
                lat=-90.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            -30.852,
            delta=0.01,
        )

    def test_N45_E90(self):
        """WMM N45 E90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=90.0,
                lat=45.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            2.089,
            delta=0.01,
        )

    def test_N45_W90(self):
        """WMM N45 W90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=45.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            -2.545,
            delta=0.01,
        )

    def test_S45_E90(self):
        """WMM S45 E90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=90.0,
                lat=-45.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            -41.083,
            delta=0.01,
        )

    def test_S45_W90(self):
        """WMM S45 W90 2020-10-15"""
        self.assertAlmostEqual(
            self.md_object.md(
                lon=-90.0,
                lat=-45.0,
                year=2020,
                mon=10,
                day=15,
                provider="BGS_WMM",
            ),
            21.145,
            delta=0.01,
        )
