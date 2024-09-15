import sys

def count_lines(file):
    return sum(1 for _ in file)

def count_words(file):
    return sum(len(line.split()) for line in file)

def count_chars(file):
    return sum(len(line) for line in file)

# Function to count the number of bytes in the file
def count_bytes(file):
    return sum(len(line.encode('utf-8')) for line in file)

def wc(file, count_lines_flag, count_words_flag, count_chars_flag, count_bytes_flag):
    lines = words = chars = bytes_count = 0
    if count_lines_flag:
        lines = count_lines(file)
        file.seek(0)
    if count_words_flag:
        words = count_words(file)
        file.seek(0)
    if count_chars_flag:
        chars = count_chars(file)
        file.seek(0)
    if count_bytes_flag:
        bytes_count = count_bytes(file)
        file.seek(0)
    return lines, words, chars, bytes_count

def print_help():
    help_text = """
    Usage: python my_wc.py [options] [file]

    Options:
    -l      Count lines
    -w      Count words
    -m      Count characters
    -c      Count bytes
    -help   Display this help message

    If no file is specified, the program reads from standard input.
    If no options are specified, the default behavior is to count lines, words, and bytes.
    """
    print(help_text)

def main():
    if '-help' in sys.argv:
        print_help()
        return
    
    # Check for flags in command-line arguments
    count_lines_flag = '-l' in sys.argv
    count_words_flag = '-w' in sys.argv
    count_chars_flag = '-c' in sys.argv
    count_bytes_flag = '-m' in sys.argv
    
    # Default behavior if no flags are provided
    if not (count_bytes_flag or count_chars_flag or count_lines_flag or count_words_flag):
        print("Usage: pywc [-lwc] [file ...]")
        sys.exit(1)
    
    if len(sys.argv) > 1 and not sys.argv[-1].startswith('-'):
        filename = sys.argv[-1]
        with open(filename, 'r', encoding='utf-8') as file:
            lines, words, chars, bytes_count = wc(file, count_lines_flag, count_words_flag, count_chars_flag, count_bytes_flag)
    else:
        print("Usage: pywc [-lwc] [file ...]")
        sys.exit(1)
        
    if count_lines_flag:
        print(f"Lines: {lines}")
    if count_words_flag:
        print(f"Words: {words}")
    if count_chars_flag:
        print(f"Chars: {chars}")
    if count_bytes_flag:
        print(f"Bytes: {bytes_count}")

if __name__ == '__main__':
    main()