from urllib.parse import urljoin

from humble.downloader import HumbleDownloader, BASE_URL


def reddit(games):
    header = [
        '| Name   | Discount | Price | Platform |',
        '|:-------|:--------:|:-----:|:---------:|'
    ]
    lines = []
    for game in games:
        item = dict()
        item['discount'] = '-{}%'.format(round(game['current_price'][0] * 100 / game['full_price'][0]))
        item['price'] = ''.join([str(v) for v in game['current_price']])
        item['platform'] = ', '.join(game['platforms'])
        item['name'] = "[{}]({})".format(game['human_name'], urljoin(BASE_URL, game['human_url']))
        lines.append('| {name} | {discount} | {price} | {platform} |'.format(**item))
    lines = sorted(lines, reverse=True)
    return '  \n'.join(header + lines)


def reddit_vr(games):
    lines = reddit(games).split('  \n')
    headers = lines[:2]
    lines = [l for l in lines if 'vive' in l or 'oculus-rift' in l]
    return '  \n'.join(headers + lines)


