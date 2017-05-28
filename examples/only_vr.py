from humble import HumbleDownloader, markdown

if __name__ == '__main__':
    games = HumbleDownloader('https://www.humblebundle.com/store/promo/spring-sale-encore/').download_games()
    games = [g for g in games if 'vive' in g['platforms'] or 'oculus-rift' in g['platforms']]
    print(markdown(games))
