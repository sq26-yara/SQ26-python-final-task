# Wordlist Generator
The idea for this project was inspired by the need to test different tools and systems in the cybersecurity field. Wordlists are crucial for tasks 
such as penetration testing, password cracking, and security assessments, making this tool essential for cybersecurity professionals and enthusiasts.

## Description

This Python script generates a wordlist file based on user-provided input. The user can specify the minimum and maximum length of words, 
as well as optionally include uppercase letters, numbers, and special characters. 
The generated wordlist is saved to a file at the user-provided path.

## Features

- **Min and Max Length**: Specify the minimum and maximum length of words in the wordlist.
- **Uppercase Letters**: Optionally include uppercase letters in the wordlist.
- **Numbers**: Optionally include numbers in the wordlist.
- **Special Characters**: Optionally include special characters in the wordlist.
- **Output Path**: Specify the file path where the wordlist will be saved.

## Usage
wordlist-generator.py [-h] -l l -L L [-U] [-n] [-s] -o O

Generate custom wordlists based on user-defined criteria.

options:
  -h, --help  show this help message and exit
  -l l        Minimum length of words (mandatory).
  -L L        Maximum length of words (mandatory).
  -U          Include uppercase letters (optional).
  -n          Include numbers (optional).
  -s          Include special characters (optional).
  -o O        Output file path (mandatory).
  
## Exapmle
python3 wordlist-generator.py -l 3 -L 6 -n -o wordlist_3-6.txt

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the Unlicense license. See the [LICENSE](LICENSE) file for details.
