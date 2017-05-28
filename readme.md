# Humble crawler

Small crawler for humble bundle store: https://www.humblebundle.com/store
With ability to output formatted reddit comments.

## Usage:

    from humble import HumbleDownloader, markdown
    dl = HumbleDownloader('https://www.humblebundle.com/store/promo/spring-sale-encore/')
    games = dl.download_games()
    print(markdown(games))

result example:

| Name   | Discount | Price | Platform |
|:-------|:--------:|:-----:|:---------:|
| [Universe Sandbox ²](https://www.humblebundle.com/store/universe-sandbox-squared) | -75% | 17.24EUR | windows, mac, vive, linux |
| [Tabletop Simulator](https://www.humblebundle.com/store/tabletop-simulator) | -50% | 9.99EUR | windows, mac, vive, linux |
| [Redout](https://www.humblebundle.com/store/redout) | -50% | 15.99EUR | oculus-rift, windows, vive |


## Install:

    pip install git+ssh://github.com/granitosaurus/humblestore-crawler
    # or
    pip install git+https://github.com/granitosaurus/humblestore-crawler

