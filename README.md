# NameChanger

![NameChanger logo](NameChanger.webp)

*NameChanger* is a Python utility for renaming multiple files at a time (can be any file type).

It's a game changer for managing your files!

## Features

- Recursively renames files in directories and subdirectories.
- Maintains the directory structure in the output directory.
- Allows you to specify the string to replace and the replacement string.
- Logs the renaming process for easy tracking.

## Prerequisites

- Python 3.x

## Usage

1. Place your files inside the **input** directory.
2. Run the script: `python3 script.py [string_to_replace] [replacement_string]`.
3. The renamed files and their total number will be logged in the terminal.

> All files are copied inside the **output** directory even if they are not renamed, keeping the input and output files consistency.

## Example

Suppose you have the following directory structure:

```lua
input/
├── directory
│   ├── foo_image.jpg
│   └── FOO.txt
└── foo.txt
```

Running `python3 script.py "foo" "bar"` will produce:

```lua
output/
└── directory
    ├── bar_image.jpg
    └── FOO.txt
├── bar.txt
```

> Note that the renaming is case-sensitive. That's why "FOO.txt" is not renamed here, neither would be "Foo.txt".

## Contributing

Contributions are welcome! Here are a few ways you can contribute:

- Report bugs or issues
- Suggest new features or enhancements  
- Submit pull requests

## License

This project is licensed under the [MIT License](LICENSE).
