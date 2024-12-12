import argparse
import itertools
import string

# Define the function to create the wordlist
def generate_wordlist(min_length, max_length, include_uppercase, include_numbers, include_specials, output_file):
    # Base character set: lowercase letters
    charset = string.ascii_lowercase

    # Extend the character set based on user input
    if include_uppercase:
        charset += string.ascii_uppercase
    if include_numbers:
        charset += string.digits
    if include_specials:
        charset += string.punctuation

    try:
        # Open the output file for writing
        with open(output_file, 'w') as f:
            # Generate words of lengths from min_length to max_length
            for length in range(min_length, max_length + 1):
                for word in itertools.product(charset, repeat=length):
                    # Write each word to the file
                    f.write(''.join(word) + '\n')
        print(f"Wordlist created successfully and saved to {output_file}")
    except IOError as e:
            print(f"Error writing to file: {e}")

# Define the main function for argument parsing
def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(
        description="Generate custom wordlists based on user-defined criteria."
    )

    # Adding arguments
    parser.add_argument('-l', type=int, required=True, help="Minimum length of words (mandatory).")
    parser.add_argument('-L', type=int, required=True, help="Maximum length of words (mandatory).")
    parser.add_argument('-U', action='store_true', help="Include uppercase letters (optional).")
    parser.add_argument('-n', action='store_true', help="Include numbers (optional).")
    parser.add_argument('-s', action='store_true', help="Include special characters (optional).")
    parser.add_argument('-o', type=str, required=True, help="Output file path (mandatory).")

    # Parse arguments
    args = parser.parse_args()

    # Set a threshold for large maximum length
    LENGTH_THRESHOLD = 5
    # Validate length arguments
    if args.l > args.L:
        parser.error("Minimum length (-l) cannot be greater than maximum length (-L).")

    if args.L > LENGTH_THRESHOLD:
        response = input(f"WARNING: The wordlist with the maximum length more than {LENGTH_THRESHOLD} can be time and resource consuming. Do you want to proceed? (yes/no)").strip().lower()
        if response not in ['yes', 'y']:
            print("Operation cancelled by the user.")
            exit()

    # Call the wordlist generation function
    generate_wordlist(
        min_length=args.l,
        max_length=args.L,
        include_uppercase=args.U,
        include_numbers=args.n,
        include_specials=args.s,
        output_file=args.o
    )

if __name__ == "__main__":
    main()
