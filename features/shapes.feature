Feature: Creation of a blank scene

  Scenario: Program startup
     Given the program is loaded
      When the program starts
      Then a blank scene of size 40x20 is created