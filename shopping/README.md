
# Will you buy?
This is a Python implementation of a K-Nearest Neighbors Classification algorithm. It utilizes Scikit-Learn library to categorize shopping data into "positives" and "negatives" based on customer features, in order to determine if a user will or will not conduct a purchase when on a webpage. The program then tests the accuracy of the model, as well as its sensitivity and specificity.

## Data Points Used For Training
* Administrative
* Administrative_Duration
* Informational
* Informational_Duration
* ProductRelated
* ProductRelated_Duration
* BounceRates
* ExitRates
* PageValues
* SpecialDay
* Month (as integer from 0 to 11)
* OperatingSystems
* Browser
* Region
* TrafficType
* VisitorType (0 = not returning; 1 = returning)
* Weekend (0 = false; 1 = true)

## Libraries
This project uses the following libraries:
* csv
* sys
* sklearn
Alternatively, install the libraries with 
`pip3 install -r requirements.txt`

## Usage
The code is used from the terminal, with one parameter, `data`:
`python3 shopping.py data` 