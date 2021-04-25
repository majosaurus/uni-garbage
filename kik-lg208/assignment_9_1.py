"""The program asks for input file, output files, and threshold. Then it 
goes line by line in the input file, sorting lines according to length. If
the length of the line is shorter than threshold, the line is written into
the first output file. If the length of the line is equal to or longer than
the threshold, it is written into second output file."""

def count_length(input_file, short_file, long_file, threshold):
    """The function counts the length of the lines and sorts them accordingly."""

    i_file = open(input_file, "r")
    s_file = open(short_file, "w")
    l_file = open(long_file, "w")
    
    for lines in i_file:
        if len(lines) -1 >= threshold:
            l_file.write(lines)
            
        else:
            s_file.write(lines)
            
    i_file.close()
    s_file.close()
    l_file.close()

    return 0


def main():
    """The main function asks for input file, output files, and threshold.
    If the user enters the files and threshold incorrectly, the program keeps
    asking."""

    while True: # using for repetitive asking
        try:
            in_file = input("What is your file? ")
            short_file = input("What is your output file for short lines? ")
            long_file = input("What is your output file for long lines? ")
            threshold = int(input("What is your length threshold value? "))

            if (in_file[-4:] or short_file[-4:] or long_file[-4:]) != ".txt": # if the file is not .txt
                print("NotTextFileError: File is not .txt file.")
                continue # skip following code and ask for the input again

            count_length(in_file, short_file, long_file, threshold)

            print("Reading", in_file)
            print("Writing all lines shorter than", threshold, "into", short_file)
            print("Writing all lines longer or equal to", threshold, "into", long_file)
            break # end program

        except ValueError:
            print("ValueError: Threshold value not int.")
        except FileNotFoundError:
            print("FileNotFoundError: The file does not exist.")


main()
