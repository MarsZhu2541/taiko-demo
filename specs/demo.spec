# Feature: Taiko Demo

Tags: TeamPanda


## Test local Admintool
Given
* Open admintool
* Login with username "testadmin1" and password "test"
When
* Search VIN "WVWZZZ1JZXW000010" in Vehicle Monitoring
Then
* Assert Model Year equals "0"
* Logout admintool

## Test local Admintool Bad Case
Given
* Open admintool
* Login with username "testadmin1" and password "test"
When
* Search VIN "WVWZZZ1JZXW000010" in Vehicle Monitoring
Then
* Assert Model Year equals "2023"
* Logout admintool