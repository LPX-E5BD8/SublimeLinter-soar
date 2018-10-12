# SublimeLinter-soar
SublimeLinter plugin for SQL by SOAR.

![soar](https://user-images.githubusercontent.com/39460745/46163054-ad2f5280-c2bc-11e8-9d7b-bb530e162d5d.png)

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `SOAR` is installed on your system.
Please follow the instructions of [`SOAR`](https://github.com/XiaoMi/soar).

### Plugin installation
At the first, you need clone the plugin into package folder.
1. Open Sublime Text and click `Preferences -> Browse Packages...`
1. Clone the repo into folder.
```shell
git clone https://github.com/liipx/SublimeLinter-soar.git
```

Then click `Preferences -> Package Settings -> SublimeLinter -> Settings`, set the config as following:
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
