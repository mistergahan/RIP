Feature: My first feature file using radish
    In order to test my awesome software
    I need an awesome BDD tool like radish
    to test my software.

    Scenario: Test my function get_price()
        Given I have the component drinks = Composite('Напитки') drinks.add(Leaf('Фруктовый сок', 100)) drinks.add(Leaf('Чай чёрный', 50))
        When I get price from them
        Then I expect the result to be 150
