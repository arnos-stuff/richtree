import rich

from mltree.core.reader import read_file
from mltree.utils.paths import tests_dir


class TestTOML:
    
    obj = read_file(tests_dir / 'example.toml')

    base_keys = [
        "title",
        "owner",
        "database",
        "servers",
        "clients",
    ]
    
    def test_keys(self):
        assert set(self.obj.keys()) == set(self.base_keys)

    def test_text_fields(self):
        assert self.obj["title"] == "TOML Example"        
        assert self.obj["owner"]["name"] == "Tom Preston-Werner"
        assert self.obj["database"]["server"] == "192.168.1.1"
        
    def test_int_fields(self):
        assert self.obj["database"]["ports"] == [8000, 8001, 8002]
        assert self.obj["database"]["connection_max"] == 5000
    
    def test_bool_fields(self):
        assert self.obj["database"]["enabled"] is True
        
    def test_list_fields(self):
        assert isinstance(self.obj["database"]["ports"], list)
        assert isinstance(self.obj["clients"]["data"], list)
        
    def test_dict_fields(self):
        assert isinstance(self.obj["servers"], dict)
        assert isinstance(self.obj["clients"], dict)
        
        
def recurse_keys(obj):
    curr = obj
    while isinstance(curr, dict):
        for key in curr.keys():
            yield key
            yield from recurse_keys(curr[key])
        break

class TestJSON:
    
    obj = read_file(tests_dir / 'example.json')

    recursed_keys = {
        'glossary', 'title',
        'GlossDiv', 'title',
        'GlossList', 'GlossEntry',
        'ID', 'SortAs', 'GlossTerm',
        'Acronym', 'Abbrev', 'GlossDef',
        'para', 'GlossSeeAlso', 'GlossSee'
    }
    
    def test_keys(self):
        assert self.recursed_keys == set(recurse_keys(self.obj))

    def test_text_fields(self):
        assert self.obj["glossary"]["title"] == "example glossary"     
        assert self.obj["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossTerm"] == "Standard Generalized Markup Language"
        assert self.obj["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["para"] == "A meta-markup language, used to create markup languages such as DocBook."
        
        
        
class TestYAML:
        obj = read_file(tests_dir / 'example.yaml')
    
        base_keys = [
            "doe",
            "ray",
            "pi",
            "xmas",
            "calling-birds",
            "french-hens",
            "xmas-fifth-day",
        ]
        
        def test_keys(self):
            assert set(self.obj.keys()) == set(self.base_keys)
            
        def test_text_fields(self):
            assert self.obj["doe"] == "a deer, a female deer"
            assert self.obj["ray"] == "a drop of golden sun"
            
        def test_float_fields(self):
            assert self.obj["pi"] == 3.14159
        
        def test_list_fields(self):
            assert isinstance(self.obj["calling-birds"], list)
        
        def test_dict_fields(self):
            assert isinstance(self.obj["xmas-fifth-day"], dict)
            assert isinstance(self.obj["xmas-fifth-day"]["partridges"], dict)