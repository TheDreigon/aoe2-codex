# aoe2-codex
A historical rework of the Age of Empires II civilizations and tech tree, shown in your web browser.

This is a fan project built on top of [aoe2techtree](https://github.com/SiegeEngineers/aoe2techtree)
(the code behind [aoe2techtree.net](https://aoe2techtree.net)). The original game data is kept as it is;
the reworked civilizations, the design rules and our own history texts live in [`codex/`](codex/).
Start with the project rules in [`codex/RULES.md`](codex/RULES.md).

Age of Empires II © Microsoft Corporation.
**aoe2-codex** and **aoe2techtree** were created under Microsoft's "[Game Content Usage Rules](https://www.xbox.com/en-us/developers/rules)" using assets from Age of Empires II,
and they are not endorsed by or affiliated with Microsoft. This is a non-commercial fan project.

## Development

To run the website locally, either open `index.html` in Firefox
or execute one of the following commands in this directory and
open [localhost:8000](http://localhost:8000) in any browser:

 - `php -S localhost:8000`
 - `python3 -m http.server`
 - `python2 -m SimpleHTTPServer`

## Used libraries

 - [svgjs](https://svgjs.dev/)

## Authors

[TheDreigon](https://github.com/TheDreigon) - aoe2-codex (historical rework)

### aoe2techtree

[HSZemi](https://github.com/hszemi) - Original Author

[ides315](https://github.com/ides315) - Plugged in the Return of Rome tech tree
