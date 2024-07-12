# NameChanger

![NameChanger logo](NameChanger.webp)

*NameChanger* is a Python utility for renaming multiple files at a time (can be any file type).

It's a game changer for managing and organizing your files!

## Features

- Recursively renames files in directories and subdirectories.
- Maintains the directory structure in the output directory.
- Allows you to specify the string to replace and the replacement string.
- Logs the renaming process for easy tracking.

## Prerequisites

- Python 3.x

## Usage

1. Adjust the constants in the script according to your needs.
2. Place your files inside the **input** directory.
3. Run the script: `python3 script.py`.
4. All your files will be renamed inside the **output** directory.

## Example

Suppose you have the following directory structure:

```lua
input/
├── dir/
│   └── foo_2.jpg
├── foo_1.txt
```

Running the script with `STRING_TO_REPLACE = 'foo'` and `REPLACEMENT_STRING = 'bar'` will produce:

```lua
input/
├── dir/
│   └── bar_2.jpg
├── bar_1.txt
```

## Contributing

Contributions are welcome! Here are a few ways you can contribute:

- Report bugs or issues
- Suggest new features or enhancements  
- Submit pull requests

## License

This project is licensed under the [MIT License](LICENSE).
