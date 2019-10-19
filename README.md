[![Build Status](https://travis-ci.org/proway2/demag.svg?branch=master)](https://travis-ci.org/proway2/demag)

# DEMAG

Calculates magnetic declination based on available online calculators. Before use read the usage rules of appropriate service.    
**Under active development!**

## Features

### NOAA
- web version [NOAA](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml)
- API and usage rules are described [here](https://www.ngdc.noaa.gov/geomag/calculators/help/declinationHelp.html)
- API version example https://www.ngdc.noaa.gov/geomag-web/calculators/calculateDeclination?lat1=60&lon1=40&startYear=2018&startMonth=06&startDay=02&resultFormat=xml
- API HTTP GET result:
```xml
<maggridresult>
    <version>0.5.1.0</version>
    <model>wmm2015v2</model>
    <result>
        <date>2018.41644</date>
        <latitude units = "degree">60.00000</latitude>
        <longitude units="degree">40.00000</longitude>
        <elevation units="km">0.00000</elevation>
        <declination units="degree">14.05269</declination>
        <declination_sv units="degree">0.16844</declination_sv>
        <declination_uncertainty units="degree">0.44237</declination_uncertainty>
    </result>
</maggridresult>
```

### BGS
- web version [BGS WMM](http://geomag.bgs.ac.uk/data_service/models_compass/wmm_calc.html)
- API usage and rules described [here]()
- API version example http://geomag.bgs.ac.uk/web_service/GMModels/wmm/2015v2/?latitude=-80&longitude=240&altitude=0&date=2017-07-02&format=xml
- Altitude is in *kilometers above MSL!*
- API HTTP GET result:
```xml
<geomagnetic-field-model-result>
    <model revision="2015v2">wmm</model>
    <date>2017-07-02</date>
    <coordinates>
        <latitude units="deg (north)">-80</latitude>
        <longitude units="deg (east)">240</longitude>
        <altitude units="km">0.00</altitude>
    </coordinates>
    <field-value>
        <total-intensity units="nT">55325</total-intensity>
        <declination units="deg (east)">69.594</declination>
        <inclination units="deg (down)">-72.301</inclination>
        <north-intensity units="nT">5865</north-intensity>
        <east-intensity units="nT">15764</east-intensity>
        <vertical-intensity units="nT">-52706</vertical-intensity>
        <horizontal-intensity units="nT">16820</horizontal-intensity>
    </field-value>
    <secular-variation>
        <total-intensity units="nT/y">-80.7</total-intensity>
        <declination units="arcmin/y (east)">-5.1</declination>
        <inclination units="arcmin/y (down)">2.3</inclination>
        <north-intensity units="nT/y">27.3</north-intensity>
        <east-intensity units="nT/y">2.0</east-intensity>
        <vertical-intensity units="nT/y">88.4</vertical-intensity>
        <horizontal-intensity units="nT/y">11.4</horizontal-intensity>
    </secular-variation>
</geomagnetic-field-model-result>
```

## Installation
- Python 3.6+ required

## Usage

## Tests
python3 -m unittest tests/test_*.py

## License
GPL v3
