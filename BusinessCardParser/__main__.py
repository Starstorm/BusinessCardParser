# Execution begins here
if __name__ == '__main__':
    # Import required modules
    import argparse, spacy, re, names_dataset, sys
    
    # Configure ArgumentParser for command line interface
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="Business card text file")
    ap.add_argument("-t", "--text", help="Business card raw text")
    ap.add_argument("-o", "--output", help="Output text for file. If not used, will display to screen.")
    my_args = vars(ap.parse_args())
    
    # Check if either the file or the raw text parameter is set, but not both.
    if (not my_args['text'] and not my_args['file']) or (my_args['text'] and my_args['file']):
        print("[ERROR] Input parameters not set properly. Please use the --help argument for more information on proper usage.")
        sys.exit(0)
        
    # Instantiate BusinessCardParser object
    my_parser = BusinessCardParser()
    
    # Get the business card text
    if my_args['file']:
        with open(my_args['file'],"r") as card_file:
            document = card_file.read()
    else:
        document = my_args['text']
       
    # Generate ContactInfo object
    my_contact_info = my_parser.getContactInfo(document)
    
    # Output results of ContactInfo object
    if my_args['output']:
        with open(my_args['output'], "w") as output_file:
            output_file.write(str(my_contact_info))
    else:
        print(str(my_contact_info))
