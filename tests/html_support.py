import rich
import json
from html.parser import HTMLParser

from typing import Any

from iotree.utils.paths import tests_dir

class HTMLDictBuilder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.root = {}

    def handle_starttag(self, tag, attrs):
        self.stack.append({tag: {}})
        if attrs:
            self.stack[-1][tag].update(attrs)

    def handle_endtag(self, tag):
        if len(self.stack) > 1:
            self.stack[-2][tag].update(self.stack[-1])
            self.stack.pop()
        else:
            self.root.update(self.stack[-1])
            self.stack.pop()

    def handle_data(self, data):
        if not len(self.stack):
            self.stack.append({})
        elif data.strip():
            self.stack[-1].update({data: {}})
        self.stack[-1].update(
            {k: v for k, v in self.stack[-1].items() if k != data}
        )
    
    def handle_startendtag(self, tag, attrs):
        if not len(self.stack):
            self.stack.append({tag: {}})
        elif tag not in self.stack[-1]:
            self.stack[-1][tag] = {}
        else:
            self.stack[-1][tag].update(attrs)
    
    def handle_comment(self, data):
        self.stack[-1].update({data: {}})
    
    def handle_entityref(self, name):
        self.stack[-1].update({name: {}})
    
    def handle_charref(self, name):
        self.stack[-1].update({name: {}})
    
    def handle_decl(self, decl):
        self.stack.append({decl: {}})
    
    def handle_pi(self, data):
        pass
    
    def handle_unknown_decl(self, data):
        pass
    
    def __call__(self, filename, *args: Any, **kwds: Any) -> Any:
        self.feed(open(filename,'r', encoding='cp437').read(), *args, **kwds)
        return self.root
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.root})"
    

    
if __name__ == "__main__":
    builder = HTMLDictBuilder()
    try:
        rich.print(builder(tests_dir/'example-easy.html'))
    except:
        json.dump(builder.root, open(tests_dir / "example-easy.parsed.json", 'w+', encoding='cp437'))