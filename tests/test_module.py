import re
from pathlib import Path


def test_smoke(build_documentation):

    dir_dogs = Path('20_dogs')
    dir_cats = Path('30_cats')
    dir_other = Path('other')

    docs_dir = build_documentation([
        '01_index.md',
        '10_another.md',
        dir_dogs / '01_bulldog.md',
        dir_dogs / '02_afgan.md',
        dir_dogs / 'dachshund.md',
        dir_dogs / 'index.md',
        dir_cats / '01_asian.md',
        dir_cats / '02_birman.md',
        dir_cats / '03_aegean.md',
        '40_add.md',
        dir_other / 'index.md',
        dir_other / 'file.md',
    ])
    index_html = (docs_dir / 'index' / 'index.html').read_text()
    found = [
        item.strip()
        for item in
        re.findall(r'<span class="md-ellipsis">([^<]+)<', index_html, re.MULTILINE)
    ]

    assert found == [
        'mysite',
        'Title for 01_index',
        'Title for 01_index',
        'Title for 10_another',
        'Dogs',
        'Title for 01_bulldog',
        'Title for 02_afgan',
        'Title for index',
        'Title for dachshund',
        'Cats',
        'Title for 01_asian',
        'Title for 02_birman',
        'Title for 03_aegean',
        'Title for 40_add',
        'Other',
        'Title for index',
        'Title for file',
    ]
