# 3G-Huawei-Propagation-Delay-Tool-Google-Earth
This is a python tool to generate KML files for each propagation delay from Huawei 3G Wireless Equipment


# To use this tool, you need: #

* Download data from Huawei U2000/U2020 equipment with counters mentioned in the template file. If some counters are disabled (like RSCP or ECNO per TP), you ned to put 0 in those columns since the format of the file should remain unchanged.

* Process the data to keep only 1 cell per row

* Generate an EPT (Engineering parameter file) with th same cells from previous point. It is important the cells has the exact same name (Case sensitive)

* By running the tool the final result will be a KMZ file to be opened with Google Earth.

![picture alt](https://github.com/joch182/3G-Huawei-Propagation-Delay-Tool-Google-Earth/blob/master/assets/picture.jpg "3G Propagation Delay")
