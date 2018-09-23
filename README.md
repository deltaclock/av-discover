# av-discover

A simple tool to parse the system drivers and proccess in order to determine if and what AV solution the target has.

## Usage

Supply both current processes file and drivers file.

```shell
$ python search.py tests/tasklist.txt tests/drivers.txt 
Scanning tasklist for av exe..
Found MsMpEng.exe
Found msseces.exe
Scanning drivers for av solutions..
Possible Antivirus solutions found by drivers search: None!
```

> You can later search for the found exe online

The tasklist file is created just by running `tasklist` or similar command which outputs a list of running processes.

The drivers file is generated just by running `dir` in the directory `C:\windows\System32\drivers` if the system is x64, else `C:\windows\sysnative\drivers`.

### Notes

This tool is meant to aid in the discovery of the AV a target might have when other ways dont work and access to powershell is limited.

With even a cmd shell you can check for AV before running any big payloads.

Supports both Python2 and 3.

#### Credits

This tool this majorely based on the https://github.com/harleyQu1nn/AggressorScripts project
