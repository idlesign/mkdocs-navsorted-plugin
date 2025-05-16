import os
from pathlib import Path
from textwrap import dedent

import pytest

from mkdocs_navsorted.utils import build_docs


@pytest.fixture
def in_tmp_path(tmp_path):
    before = os.getcwd()
    try:
        os.chdir(tmp_path)
        yield tmp_path
    finally:
        os.chdir(before)


@pytest.fixture
def build_documentation(in_tmp_path):

    def build_(fnames: list[str | Path]) -> Path:
        conffile = in_tmp_path / 'mkdocs.yml'

        conffile.write_text(dedent('''
            site_name: mysite        
            plugins:
              - navsorted
            theme:
              name: material
        '''))

        docs_dir = in_tmp_path / 'docs'
        docs_dir.mkdir()

        for fname in fnames:
            target_path = docs_dir / Path(fname)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(f'# Title for {target_path.name.replace(".md", "")}\n\n')

        build_docs(conf=f'{conffile}')

        return in_tmp_path / 'site'

    return build_
