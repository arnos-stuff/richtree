import rich

from iotree.core.io.reader import read
from iotree.core.render.trees import build
from iotree.utils.paths import tests_dir

formats = ['json', 'yaml', 'toml', 'xml']

for fmt in formats:
    obj = read(tests_dir / f'example.{fmt}')
    rich.print(build(obj))
    
    rich.print(30 * '=')