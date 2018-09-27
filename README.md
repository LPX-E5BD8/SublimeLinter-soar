# SublimeLinter-soar
=================================================
SublimeLinter plugin for SQL by SOAR.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `SOAR` is installed on your system. To install `SOAR`, do the following:

```
// TODO
```

### Plugin installation
Open Sublim Text and click `Preference -> Package Settings -> SublimeLinter -> Settings`, set the config as following:

```
// SublimeLinter Settings - User
{
	"linters": {
        "soar": {
            "soar_path":"you_soar_path"
        },
    },
}

```

Now, open a sql file and enjoy.
