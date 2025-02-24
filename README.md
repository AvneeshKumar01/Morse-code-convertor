# Morse Code Translator

This is a Python program that translates English text to Morse code and vice versa. It also plays sound for Morse code symbols using `pygame`.

## Features
- Convert English text to Morse code
- Convert Morse code to English text
- Play sound for Morse code symbols (`dot.wav` and `dash.wav`)

## Requirements
Make sure you have Python and the following dependencies installed:

```bash
pip install pygame
```

## How to Use
1. Run the script:
   ```bash
   python morse.py
   ```
2. Choose an option:
   - **1**: Convert English to Morse code
   - **2**: Convert Morse code to English
3. Enter your text and see the translation.
4. If converting to Morse code, you will hear sounds for dots and dashes.

## File Structure
```
├── morse.py          # Main script
├── sound.py          # Sound handling module
├── dot.wav          # Sound for dot
├── dash.wav         # Sound for dash
├── README.md        # Documentation
```

## Example
### English to Morse
```
Input: SOS
Output: ... --- ... (With sound playback)
```

### Morse to English
```
Input: ... --- ...
Output: SOS
```

## Notes
- Ensure `dot.wav` and `dash.wav` exist in the same directory as `morse.py`.
- The script ignores unsupported characters.

## License
This project is open-source and free to use.

