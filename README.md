Ratio Calculator
================

A simple Python 3 script to calculate the ratio of two numbers. Such as the dimensions of an image or screen. Now able to output JSON as well!  :-)


Usage
-----

```bash
$ ratio 1280x720

    Ratios:   16:9 (1.777~)
    Divisor:  80
    Pixels:   921,600 or 0.88 MP
    Spec:     720p, HD

$ ratio 3440x1440

    Ratios:   43:18 (2.388~)
    Divisor:  80
    Pixels:   4,953,600 or 4.72 MP
    Spec:     UWQHD
    Close to: 21:9 (2.333~) 'Ultra Wide'

$ ratio 320 320

    Ratios:   1:1 (1.000¯)
    Divisor:  320
    Pixels:   102,400 or 0.10 MP
    Spec:     Square

$ ratio 1280x720 --json
{"ratios": ["16:9", "1.777~"], "divisor": 80, "pixels": [921600, "0.88 MP"], "spec": "720p, HD"}
$ ratio -v
Ratio 1.2.0
$ ratio --help
usage: Ratio [-a] [-h] [-j] [-v] dimensions [dimensions ...]

Ratio: the ratio parser!

positional arguments:
  dimensions            dimensions to process

optional arguments:
  -a, --alternate, /alt
                        Use alternate output format
  -h, --help, /help     Show this help message and exit
  -j, --json, /json     Output as JSON
  -v, --version, /ver   Show program's version number and exit
```


Installation
------------

This installation example assumes you have a directory off of your home directory named `repos`, a local `bin` directory that already exists in your `PATH` and you have already installed Python 3. Adjust appropriately if you have a different location for your cloned repositories or intend to link the script to another executable path.


### Linux, UNIX, etc.

First install Python 3 if it's not already present. I recommend your local package manager `apt-get`, et. al. Or download and install manually from [ActivePython 3 from ActiveState][] or [Download Python for Other Platforms | Python.org][].

```bash
$ cd ~/repos
$ git clone git@github.com:runeimp/ratio.git
$ cd ~/bin
$ ln -s ../repos/ratio/ratio.py ratio
```


### macOS/Darwin

First you must install Python 3 via a package manager such as [Fink][], [Homebrew][], or [The MacPorts Project][]. Or download and install manually from [ActivePython 3 from ActiveState][] or [Python Releases for Mac OS X | Python.org][]. I use Homebrew personally.


#### Homebrew

```bash
$ brew update
...
$ brew install python3
...
```


#### Install

```bash
$ cd ~/repos
$ git clone git@github.com:runeimp/ratio.git
$ cd ~/bin
$ ln -s ../repos/ratio/ratio.py ratio
```


### Windows

Please note that this install method for Windows has NOT been tested in any way. I'm just riffing off the top of my head as a former Windows guy who still uses it for gaming and minor Windows specific projects. O:-)

First you must install Python 3 via download and install manually from [ActivePython 3 from ActiveState][] or [Python Releases for Windows | Python.org][].

```dos
> CD \REPOS
> git clone git@github.com:runeimp/ratio.git
> CD \BIN
> mklink /D \BIN\ratio \REPOS\ratio\ratio.bat
```

Installing in this fashion will allow for easy updating of the repo while maintaining an extensionless executable reference.


[ActivePython 3 from ActiveState]: http://www.activestate.com/activepython-3
[Download Python for Other Platforms | Python.org]: https://www.python.org/download/other/
[Fink]: http://www.finkproject.org/
[Homebrew]: http://brew.sh/
[JSDB]: http://www.jsdb.org/
[Microsoft - Windows Script Host]: https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/wsh_overview.mspx?mfr=true
[Node.js]: https://nodejs.org/en/
[Python Releases for Mac OS X | Python.org]: https://www.python.org/downloads/mac-osx/
[Python Releases for Windows | Python.org]: https://www.python.org/downloads/windows/
[The MacPorts Project]: https://www.macports.org/
