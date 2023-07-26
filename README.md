# Specification

- I work for a school report company
- We help teachers find out how their student perform on tests
- We get a string of csvs for the test results and we would like you to generate a simple report on top of that

- The test results are red, green, amber

## Inputs

The results should be processed in a case insensitive way as case could change

An incorret spelling of a colour would be an invalid grade, likewise a different colour or word
In which case, add an additional category named 'uncounted'

## Outputs

A string in the following format:
    `"Green: 3\nAmber: 1\nRed: 1"`

(And always in this order)

A colour that is not present in the input should not be present in the output

## Test Cases

Input:
    `"Green, Green, Amber, Red, Green"`
    Output =>  `"Green: 3\nAmber: 1\nRed: 1"`

Input:
    `"Green,Dave,Whimsy,Red"`	
    Output => `"Green: 1\nRed: 1\nUncounted: 2"`

## Alogirithm

- Split the given input into an list based on commas as the separator
- Assign this list to a variable named `results_list`

- Initialise a tuple `grades` containing the possible grades `Green`, `Amber`, `Red`
  
- Initialise a dictionary, `result_counts` 
- For each grade in `grades` add grade as a key to `result_counts` with the value 0
- Add `Uncounted` with a value of 0 to `result_counts`

- Iterate over `results_list` and for each result
  - Iterate over `grades` and compare an uppercase version of each grade with with an uppercase version of the result
  - If equal, increment that counter by 1
  - Else, increment Uncounted by 1

- Initialise an `output` variable to an empty string
  
- For key  in `result_counts`
    - if `result_counts[key]` > 0
        - concatenate `output` with `f'{key}: #{result_counts[key]}\n`
  
- Return `output`

## Cloning repo and running tests

`git clone https://github.com/tomcarmichael/makers-school-report-review-python.git`

`source venv/bin/activate`

`pytest`
