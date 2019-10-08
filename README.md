# BusinessCardParser

This BusinessCardParser command line utility parses the results of an optical character recognition (OCR) component in order to extract the name, phone number, and email address from the processed business card image.

## Usage Instructions:

### Basic Installation & Setup
```
git clone https://github.com/Starstorm/BusinessCardParser.git
cd BusinessCardParser
python setup.py install
cd BusinessCardParser
```
### Usage Guide
To extract the contact info from the three examples provided:
```
python BusinessCardParser.py -f ../examples/example_1.txt
python BusinessCardParser.py -f ../examples/example_2.txt
python BusinessCardParser.py -f ../examples/example_3.txt
```
If you'd prefer to manually enter your text, you can do that as well:
```
python BusinessCardParser.py -t "Business Cart Text...."
```
However, please note that the name parser can get confused without newline characters.

You can send the output to a file rather tha on-screen, if you prefer:
```
python BusinessCardParser.py -f ../examples/example_1.txt -o output_card_data.txt
```

### Testing
There is a basic unit test in the folder "tests". To utilize it, first go to the "tests" directory instead of the BusinessCardParser directory. Once there, enter the following command:
```
python -m unittest testing.py
```
If it gives you an error that ends with "ModuleNotFoundError: No module named 'testing'" it means that you are not in the correct directory.

### Josh's Notes
So there were a few points to bring up.
First and foremost, I was restricted by the interface requirements in terms of making this card reader better. My selection method for name/phone/email is inherently imperfect: it only finds the "top" element if there are multiple matches because there is no specification as to what the preference would be if there are two or more matches. Were the interface to allow it, a superior approach would be to have "Name_1", "Name_2", "Home Phone", "Cell Phone", "Home Email", "Work Email", etc. 

Also, I added an extra capability - not only can the command line tool accept raw text, it'll also read text from a file. This should allow it an easier time functioning with newline characters especially.
