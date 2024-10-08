import os
import sys
import subprocess

def main():
    #number of trials for a model
    nb_test=3

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: {} filename additional_parameter".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    additional_param = sys.argv[2]
    output_dir = "output"

    # Check if the file exists and is readable
    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        print("File '{}' not found or not readable.".format(filename))
        sys.exit(2)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the file line by line and execute each line as a command three times with different numbers
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()  # Remove any leading/trailing whitespace
            j=0       
            with open(additional_param, 'r') as g:
                for prompt in g:
                    j = j+1
            # Skip empty lines
                    if not line:
                        continue

                    print("Executing: ollama run {} '{}'".format(line, additional_param))
            
                    for i in range(1,nb_test+1):
                        output_file = os.path.join(output_dir, "{}_{}_{}.txt".format(line,j,i))

                        try:
                            with open(output_file, 'w') as outf:
                                subprocess.run(['ollama', 'run', line, prompt], stdout=outf, check=True)
                        except subprocess.CalledProcessError:
                            continue  # Continue to the next line even if a command fails
                            
if __name__ == "__main__":
    main()

