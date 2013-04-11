Feature: Tower Hanoi
    In order to finish
    As columns
    We'll have the disks

    Scenario: Move the disk from the column 0 to the column 1
        Given that I have "column 0"
        And the column has a "disk" 
		When the "disk" is smaller than the value from the "column 1"
        And I move the "disk" from the "column 0" to the "column 1"
        Then I move the "disk"
