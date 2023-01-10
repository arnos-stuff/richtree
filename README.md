# A many-in-one tool for managing your Markup Language files.

## What is it?

**iotree** is a tool for managing your Markup Language files. It is capable to write and read files in the following formats:

- JSON
- YAML
- TOML
- XML
- And soon more... :wink:

The basic goal was to have a small package anyone could add to their project and use it to manage their files. It is also possible to use it as a CLI tool.

## Installation

You cannot install the CLI tool separately for now. You can install it with the following command:

```bash
pip install iotree
```

## Usage

### As a CLI tool

To see what the display function can do, you can use the following command:

```bash
iotree demo
```

For example, the following JSON file (displayed in VSCode)

```json
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
```

will be displayed like this:

![JSON file displayed](https://i.imgur.com/tUSyW3L.png)

While the following YAML file (displayed in VSCode)

```yaml	
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

will be displayed like this:

![YAML file displayed](https://i.imgur.com/t3q5yHS.png)

**Note**: The CLI tool is not yet finished. It is still in development.  
If this just looks like a wrapper around [rich trees](https://rich.readthedocs.io/en/stable/tree.html)) to you, it almost because it is. :wink:

As a CLI tool, the key difference I want to bring is the ability to configure *themes* and *styles*.

Just run the following command to interactively create a theme:

```bash
iotree config init
```

But if you're lazy, just use a file:

```bash
iotree config init from-json my_theme.json
```

For example, the following JSON file

```json
{   
    "name": "My super pseudonym",
    "username": "my.username",
    "symbol": "lgpoint",
    "theme": "bright-blue-green"
}
```

will result in the following theme: ... 