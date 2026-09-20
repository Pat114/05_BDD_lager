#noinspection CucumberUndefinedStep
Feature: Lagerhållning

    Scenario: Lägga till
    Given att lagret är tomt
    When när jag lägger dit 10 st äpplen
    Then ska produkten heta Äpplen
    and ska lagret vara 10 st

    Scenario: Ta bort
    Given att lagret innehåller 10 st Äpplen
    When jag tar bort 3 st Äpplen
    Then ska lagret vara 7 st 

    Scenario: Lägga till - bananer
    Given att lagret är tomt
    When jag lägger dit 5 st bananer
    Then ska produkten heta bananer
    and lagret vara 5 st



