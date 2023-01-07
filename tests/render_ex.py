import rich

from mltree.core.reader import read
from mltree.core.render import build
from mltree.utils.paths import tests_dir

formats = ['json', 'yaml', 'toml', 'xml']

for fmt in formats:
    obj = read(tests_dir / f'example.{fmt}')
    rich.print(build(obj))
    
    rich.print(30 * '=')