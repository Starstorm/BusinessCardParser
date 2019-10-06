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
To extract the contact info from the first example:
```
python BusinessCardParser.py -f ../examples/example_1.txt
```
Just replace the "1" with "2" or "3" to process the remaining two examples. There is also an optional argument -o, which will have the output go to an output file instead of on the screen.
