import functools
import typing
import xml.etree.ElementTree as ET

import requests


class MagneticDeclination:
    def __init__(self):
        self.__providers = {
            "NOAA_WMM": functools.partial(self.__noaa_provider, "WMM"),
            "NOAA_IGRF": functools.partial(self.__noaa_provider, "IGRF"),
            "BGS_WMM": functools.partial(self.__bgs_provider, "WMM"),
        }

    def md(
        self,
        lat=0.0,
        lon=0.0,
        elev=0.0,
        year=2000,
        mon=1,
        day=1,
        provider="NOAA_WMM",
    ) -> typing.Optional[float]:
        """
        Returns magnetic declination for certain lat/lon and date.
        """

        self.__check__all_args(lat, lon, elev, year, mon, day, provider)

        provider_method = self.__provider_factory(provider)
        return provider_method(lat, lon, elev, year, mon, day)

    def __check__all_args(
        self, lat, lon, elev, year, mon, day, provider
    ) -> typing.Optional[bool]:
        """
        Check whether all conditions are met before starting getting MD from
        the provider. Returns True if all conditions are met,
        throws exception otherwise.
        """

        lat = float(lat)
        lon = float(lon)
        elev = float(elev)
        if any((lat > 90.0, lat < -90.0, lon > 180.0, lon < -180.0)):
            raise ValueError(
                f"Lat and/or Lon beyond limits lat:{lat} lon:{lon}"
            )
        if not self.__is_date_correct(year, mon, day):
            raise ValueError(f"Incorrect date! {year}-{mon}-{day}")
        if not self.__is_provider_registered(provider):
            raise ValueError(f"Unregistered provider {provider}")
        return True

    def __all_ints(self, *args) -> bool:
        """Checks whether all args are integeres"""

        return all(map(lambda x: isinstance(x, int), args)) if args else None

    def __is_provider_registered(self, provider_name) -> bool:
        """
        Returns True if the provider is registered and a callable object is
        assigned to that provider. Otherwise False returned.
        """

        return provider_name in self.__providers and callable(
            self.__providers[provider_name]
        )

    def __is_date_correct(self, year, mon, day) -> bool:
        """Checks whether date is correct"""
        return self.__all_ints(year, mon, day) and (
            (mon in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32))
            or (mon == 2 and day in range(1, 30))
            or (mon in (4, 6, 9, 11) and day in range(1, 31))
        )

    def __provider_factory(self, provider_name: str) -> bool:
        """Returns callable according to the provider's name"""

        return self.__providers[provider_name]

    def __noaa_provider(self, model, lat, lon, elev, year, mon, date) -> float:
        """
        Retrieves magnetic declination based on
        National Centers for Environmental Information
        National Oceanic and Atmospheric Administration.
        Based on either WMM or IGRF model.
        Different models lead to DIFFERENT RESULTS!!!
        In case of error raises exception.
        https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml
        """

        BASE_URL_NOAA = (
            "https://www.ngdc.noaa.gov/geomag-web/"
            "calculators/calculateDeclination?"
            "lat1={lat:f}&lon1={lon:f}&startYear={year:d}&"
            "startMonth={mon:02d}&startDay={day:02d}&resultFormat={form}&"
            "model={model}"
        )

        FORMAT_NOAA = "xml"

        md_request = requests.get(
            BASE_URL_NOAA.format(
                lat=lat,
                lon=lon,
                year=year,
                mon=mon,
                day=date,
                form=FORMAT_NOAA,
                model=model,
            )
        )

        if md_request.status_code != requests.codes.ok:
            raise RuntimeError(f"Unknown result")

        try:
            md_xml_tree = ET.fromstring(md_request.text)
            md = float(
                md_xml_tree.find("./result/declination").text.strip("\n")
            )
        except Exception as err:
            raise

        return md

    def __bgs_provider(self, model, lat, lon, elev, year, mon, day) -> float:
        """
        Calculates magnetic declination based on
        British Geological Survey World Magnetic Model 2015 calculator.
        Based on WMM model ONLY!
        http://www.geomag.bgs.ac.uk/data_service/models_compass/wmm_calc.html
        """

        BASE_URL_BGS = (
            "http://geomag.bgs.ac.uk/web_service/GMModels/wmm/2015v2/?"
            "latitude={lat:f}&longitude={lon:f}&altitude={elev:f}"
            "&date={date:s}&format={form}"
        )
        FORMAT_BGS = "json"

        date = "{0}-{1}-{2}".format(year, mon, day)

        md_request = requests.get(
            BASE_URL_BGS.format(
                lat=lat, lon=lon, elev=elev, date=date, form=FORMAT_BGS
            )
        )

        if md_request.status_code != requests.codes.ok:
            raise RuntimeError(f"Unknown result")

        try:
            md = float(
                md_request.json()["geomagnetic-field-model-result"][
                    "field-value"
                ]["declination"]["value"]
            )
        except Exception as err:
            raise

        # все ОК, возвращаем результат
        return md
