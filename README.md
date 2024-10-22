# Grott - Home Assistant with native MQTT integration

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fegguy%2Fgrott-home-assistant-add-on)

An addon to allow running the grott software directly on HA.

This allow to process in local all the data from the growatt datalogger and don't depend on growatt server.

This addon allow you to have all the entities automatically created.


## Add-ons provided by this repository

### &#10003; [Grott Beta branch (2.8)][addon-grott-beta]

![Latest Version][grott-beta-version-shield]
![Supports armhf Architecture][grott-beta-armhf-shield]
![Supports armv7 Architecture][grott-beta-armv7-shield]
![Supports aarch64 Architecture][grott-beta-aarch64-shield]
![Supports amd64 Architecture][grott-beta-amd64-shield]
![Supports i386 Architecture][grott-beta-i386-shield]

The Growatt inverter monitor with current HA plugin integrated

[:books: Grott Beta branch (2.8) add-on documentation][addon-doc-grott-beta]

### &#10003; [Grott stable branch (2.8)][addon-grott]

![Latest Version][grott-version-shield]
![Supports armhf Architecture][grott-armhf-shield]
![Supports armv7 Architecture][grott-armv7-shield]
![Supports aarch64 Architecture][grott-aarch64-shield]
![Supports amd64 Architecture][grott-amd64-shield]
![Supports i386 Architecture][grott-i386-shield]

The Growatt inverter monitor with current HA plugin integrated

[:books: Grott stable branch (2.8) add-on documentation][addon-doc-grott]


## Releases

Releases are based on [Semantic Versioning][semver], and use the format
of ``MAJOR.MINOR.PATCH``. In a nutshell, the version will be incremented
based on the following:

- ``MAJOR``: Incompatible or major changes.
- ``MINOR``: Backwards-compatible new features and enhancements.
- ``PATCH``: Backwards-compatible bugfixes and package updates.

You could also open an issue here on GitHub. Note, we use a separate
GitHub repository for each add-on. Please ensure you are creating the issue
on the correct GitHub repository matching the add-on.

- [Open an issue for the add-on: Grott Beta branch (2.8)][grott-beta-issue]
- [Open an issue for the add-on: Grott stable branch (2.8)][grott-issue]

For a general repository issue or add-on ideas [open an issue here][issue]



[addon-grott-beta]: https://github.com/egguy/addon-grott-beta/tree/v0.1.7
[addon-doc-grott-beta]: https://github.com/egguy/addon-grott-beta/blob/v0.1.7/README.md
[grott-beta-issue]: https://github.com/egguy/addon-grott-beta/issues
[grott-beta-version-shield]: https://img.shields.io/badge/version-v0.1.7-blue.svg
[grott-beta-aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[grott-beta-amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[grott-beta-armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[grott-beta-armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[grott-beta-i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[addon-grott]: https://github.com/egguy/addon-grott/tree/v0.1.12
[addon-doc-grott]: https://github.com/egguy/addon-grott/blob/v0.1.12/README.md
[grott-issue]: https://github.com/egguy/addon-grott/issues
[grott-version-shield]: https://img.shields.io/badge/version-v0.1.12-blue.svg
[grott-aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[grott-amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[grott-armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[grott-armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[grott-i386-shield]: https://img.shields.io/badge/i386-yes-green.svg

## contributors

Thanks for all the contributors:

- [alelio](https://github.com/alelio)
- [perico85](https://github.com/perico85)
- [crazymonster999](https://github.com/crazymonster999) - Alpha tester
- Zigbee2mqtt for the inspiration

[gitlabci-shield]: https://gitlab.com/egguy/grott-home-assistant-add-on/badges/master/pipeline.svg
[gitlabci]: https://gitlab.com/egguy/grott-home-assistant-add-on/pipelines
[issue]: https://github.com/egguy/grott-home-assistant-add-on/issues
[license-shield]: https://img.shields.io/github/license/egguy/grott-home-assistant-add-on.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[semver]: http://semver.org/spec/v2.0.0.html