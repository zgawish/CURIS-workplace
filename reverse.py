import sys

def reverse_file(filename):
    with open(filename, 'r') as input_file:
        for line in input_file.readlines():
            words = line.split()
            new = ''
            for i in range(len(words) - 1, -1, -1):
                new += words[i] + " "
            print(new)

def main():
    filename = sys.argv[1]
    reverse_file(filename)

if __name__ == "__main__":
    main()