# Website Blocker

## About

This is a website blocker made in Python. Get long needed peace from common distracting websites and others you find distracting with this easy to configure website blocker!

## Prerequisites

- `sv_ttk` - `pip install sv_ttk`
- `pywinstyles` - `pip install pywinstyles` (THIS MODULE IS ONLY REQUIRED FOR WINDOWS)
- `darkdetect` - `pip install darkdetect`


## Run Program

Windows:

```
python website_blocker.py
```

Mac & Linux:

```
python3 website_blocker.py
```

## Additional Notes

Please comment out the following lines if you are **not** running this program on Windows:

```
import pywinstyles
```
(Line 6)

```
if platform.system() == "Windows":

    if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:

        if sv_ttk.get_theme() == "dark":

            pywinstyles.change_header_color(root, "#000000")
```
(Lines 74 - 80)
