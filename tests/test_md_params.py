import unittest

from demag import MagneticDeclination


class TestMDArguments(unittest.TestCase):
    def setUp(self):
        self.md_object = MagneticDeclination()

    def test_no_inputs_wmm(self):
        """No inputs provided"""
        with self.assertRaises(RuntimeError):
            self.md_object.md()

    def test_lat_nan(self):
        """Latitude is NaN"""
        with self.assertRaises(ValueError):
            self.md_object.md(lat="lat")

    def test_lon_nan(self):
        """Longitude is NaN"""
        with self.assertRaises(ValueError):
            self.md_object.md(lat="lon")

    def test_lat_beyond_max(self):
        """Latitude far more than 90.0"""
        with self.assertRaises(ValueError):
            self.md_object.md(lat=100.0)

    def test_lat_beyond_min(self):
        """Latitude far less than -90.0"""
        with self.assertRaises(ValueError):
            self.md_object.md(lat=100.0)

    def test_lon_beyond_max(self):
        """Longitude far more than 180.0"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=300.0)

    def test_lon_beyond_min(self):
        """Longitude far less than -180.0"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=-300.0)

    def test_unknown_provider(self):
        """Unknown provider"""
        with self.assertRaises(ValueError):
            self.md_object.md(
                lon=0, lat=0, year=2015, mon=10, day=15, provider="Unknown"
            )

    def test_not_int_year(self):
        """Years is not int"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=20150.0, mon=10, day=15)

    def test_incorrect_year(self):
        """Years is int, but incorrect"""
        with self.assertRaises(RuntimeError):
            self.md_object.md(lon=0, lat=0, year=20150, mon=10, day=15)

    def test_not_int_mon(self):
        """Mon is not int"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=2015, mon='a', day=15)

    def test_incorrect_mon(self):
        """Mon is int, but incorrect"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=2015, mon=22, day=15)

    def test_not_int_day(self):
        """Day is not int"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=2015, mon=2, day='b')

    def test_incorrect_day_feb(self):
        """Day is int, but incorrect (February <= 29)"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=2015, mon=2, day=30)

    def test_incorrect_day_may(self):
        """Day is int, but incorrect (May <= 31)"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=2015, mon=5, day=32)

    def test_incorrect_day_sep(self):
        """Day is int, but incorrect (Sep) <= 30)"""
        with self.assertRaises(ValueError):
            self.md_object.md(lon=0, lat=0, year=2015, mon=9, day=31)
