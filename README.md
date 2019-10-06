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

### Josh's Notes
So there were a few points I thought worthy of bringing up.
First and foremost, I felt very restricted by the interface requirements. Were I not restricted by the interface, I could have done a better job. My selection method for name/phone/email is inherently imperfect - it only finds the "top" element if there are multiple matches because there is no specification as to what the preference would be if there are two or more matches. A superior approach would be to have "Name_1", "Name_2", "Home Phone", "Cell Phone", etc. for each element. In short, I fear the interface as designed underestimates the variations that can occur on business cards - I have seen business cards where there are two people listed such as when a couple owns a business jointly. Additionally, I have seen multiple email addresses and multiple phone numbers - what if the home number and the cell number is provided? Ignoring the cell number because the interface mandates a string be returned and not a list is highly limiting.
Second, I added an extra capability - not only can the command line tool accept raw text, it'll also read text from a file.
