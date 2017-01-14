## Requirements

* A local instance of https://github.com/buildit/acceptance-testing
* A Saucelabs account & active tunnel OR a local Firefox installation (Tested on 50.1.0)

## Usage

**Saucelabs Configuration**

To execute the tests across Saucelabs, set the following environment variables

* EXECUTION_ENVIRONMENT='saucelabs'
* SAUCELABS_USERNAME=*Your Saucelabs Username*
* SAUCELABS_KEY=*Your Saucelabs Key*
* SAUCELABS_TUNNEL_NAME=*Your Saucelabs Tunnel Name*
* TARGET_URL=*URL of hosted application*

Note that to access your local machine through Saucelabs you'll need to use the fully qualified domain name of the machine (e.g. http://albeeins01m.corp.mozilla.local:3000)

**Local Configuration**

To execute the tests locally, set the following environment variable

* EXECUTION_ENVIRONMENT='local' 
* TARGET_URL=*URL of hosted application*

**Execution**

Setup a virtual environment and `pip install -r requirements.txt`
Run `python app.py` from root context

## Caveats

To reduce complexity & dependencies I've created a minimum-code test parallelization execution framework specifically for this exercise.
 It is not meant to be a demonstration of a first choice framework for a large scale automation effort.  
 No attempt has been made to implement any of the features required by production level automation such as 
 release platform integration, reporting, categorization, BDD front end (e.g. Behave) or mobile support (among others).
 
## Model 
 
The model is split into /pages and /controls.  Elements (e.g. maximum temperature) are exposed as properties, while 
operations (e.g. click) are exposed as functions.
 
 
## Scenarios

    Scenario: The forecast page is responsive
    Given I navigate to the weather page
    Then the weather page is displayed
    
    Scenario: The default forecast is for Glasgow
    Given I navigate to the weather page
    Then a forecast for 'Glasgow' is displayed
    
    Scenario: Five daily forecasts are displayed by default
    Given I navigate to the weather page
    Then 5 daily forecasts are 'displayed'
    
    Scenario: Specifying a correct City value displays 5 daily forecasts
    Given I load the weather page
    When I enter a 'correct' city name
    Then 5 daily forecasts are 'displayed'
    
    Scenario: Selecting a daily forecast causes the hourly forecasts to be displayed
    Given I load the weather page
    When I select the 'first' day
    Then hourly forecasts are 'displayed'
    
    Scenario: Deselecting a daily forecast causes the hourly forecasts to be hidden
    Given I load the weather page
    And I select the 'first' day
    And I deselect the 'first' day
    Then hourly forecasts are 'hidden'

    Scenario: Each daily forecast should display the expected datapoints
    Given I load the weather page
    Then each daily forecast should display 'condition'
    And each daily forecast should display 'wind speed and direction'
    And each daily forecast should display 'aggregate rainfall'
    And each daily forecast should display 'minimum and maximum temperatures'

    Scenario: Specifying an unknown city should display a standard error message
    Given I load the weather page
    When I specify an unknown city value
    Then the standard error message is displayed

## Application issues

### Mobile Web

This application does not handle common responsive design breakpoints for mobile (e.g. IPad, Iphone6).  The City input 
is pushed below the 'Five day weather forecast' text.

### Accessibility

The city input form control has no label.

*Why It Matters*
If a form control does not have a properly associated text label, the function or purpose of that form control 
may not be presented to screen reader users. Form labels also provide visible descriptions and larger clickable 
targets for form controls.

*How to Fix It*
If a text label for a form control is visible, use the element to associate it with its respective form control. 
If there is no visible label, either provide an associated label, add a descriptive title attribute to the form 
control, or reference the label(s) using aria-labelledby. Labels are not required for image, submit, reset, button, 
or hidden form controls.