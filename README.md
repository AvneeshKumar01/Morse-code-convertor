# Morse Code Converter

`morse.py` is a Python script that provides functionality to encode text into Morse code and decode Morse code back into text. It is a simple, command-line tool for working with Morse code.

## Features

- Convert English text to Morse code.
- Decode Morse code into English text.
- Supports alphanumeric characters, common punctuation, and spaces.
- Handles invalid input gracefully with error messages.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone or download this repository to your local machine.
2. Ensure Python is installed by running:

   ```bash
   python --version
   ```

3. Place `morse.py` in your desired working directory.

## Usage

To use the script, open a terminal and navigate to the directory containing `morse.py`. Run the script with the following command:

```bash
python morse.py
```

### Options

Upon running, the script may provide options to:

1. Encode text to Morse code.
2. Decode Morse code to text.
3. Exit the program.

Follow the on-screen prompts to input the text or Morse code.

### Example

#### Encoding:

Input:
```
Hello World
```

Output:
```
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

#### Decoding:

Input:
```
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Output:
```
HELLO WORLD
```

## Supported Characters

The script supports:

- English letters (A-Z, a-z)
- Numbers (0-9)
- Common punctuation: `.,?'!/()&:;=+-_"@$`
- Space (represented as `/` in Morse code)

## Customization

To customize the script (e.g., adding more characters or modifying behavior):

1. Open `morse.py` in any text editor.
2. Update the dictionary mappings for Morse code as needed.

## Contributing

Contributions are welcome! If you have ideas to improve this script, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- The Morse code standard is based on ITU recommendations.
- Thanks to all open-source contributors for inspiration.

---

Feel free to modify this `README.md` file to suit your specific use case or add more details about your implementation.
