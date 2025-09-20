
☕ Coffee Machine Project
📌 Overview

This is a simple Object-Oriented Programming (OOP) project in Python that simulates a coffee vending machine.
It uses four main classes:

Menu – stores available drinks.

MenuItem – represents a single drink item (name, ingredients, cost).

CoffeeMaker – handles machine resources (water, milk, coffee).

MoneyMachine – processes coins and handles payments.

⚙️ Features

Show a menu of available drinks (espresso, latte, cappuccino).

Check if enough resources are available to make the drink.

Process coins and payments.

Deduct ingredients after making a drink.

Print a report of machine status (resources & money).

Option to turn the machine off.

📂 Project Structure
coffee_machine_project/
│
├── coffee_maker.py     # CoffeeMaker class (handles resources & making coffee)
├── money_machine.py    # MoneyMachine class (handles money & transactions)
├── menu.py             # Menu & MenuItem classes
├── main.py             # Main program (runs the machine loop)
└── README.md           # Project documentation

▶️ How to Run

Clone/download the project into your system.

Open it in PyCharm (or any IDE).

Run the file:

python main.py


Follow the prompts in the terminal:

What would you like? (espresso/latte/cappuccino):

🛠 Example Usage
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 2
How many dimes?: 1
How many nickels?: 0
How many pennies?: 0
Here is your latte ☕️. Enjoy!

💡 Learning Objectives

Understand Object-Oriented Programming in Python.

Learn how to break a big project into smaller classes and modules.

Practice imports, loops, and conditionals in Python.

Boss ⚡ chaahti ho main tumhare liye ek short README (1–2 paragraph) bhi bana dun jo sirf quick overview aur run instructions cover kare?