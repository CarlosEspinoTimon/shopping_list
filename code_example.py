#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


# FAKE articles
FAKE_ARTICLES = [
    {'name': 'Bananas', 'price': 0.80},
    {'name': 'Cookies', 'price': 2.50},
    {'name': 'Spinachs', 'price': 1.10},
    {'name': 'Chocolate', 'price': 3.50},
    {'name': 'Almonds', 'price': 7.80}
]

TOTAL_SUPERMARKETS = 5


class Article:
    """
    Article class.
    """

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        """
        Returns the string representation of the article.
        """
        return "Article: {0},\t Price: {1:.2f}€".format(self.name, self.price)


class Supermarket:
    """
    Supermarket Class.
    """

    def __init__(self, name):
        self.name = name
        self.articles = {}

    def add(self, article):
        """
        Add an article to the Supermarket. If the article is already
        in the supermarket, it overwrites it.
        """
        self.articles[article.name] = article

    def __str__(self):
        """
        Returns the string representation of all the articles from
        the Supermarket.
        """
        res = ['\n{}:\n'.format(self.name)]
        for article in self.articles.values():
            res.append('{}\n'.format(article))
        return ''.join(res)


class ShoppingList:
    """
    Shopping list class.
    """

    def __init__(self, name, articles, supermarkets, max_to_visit):
        self.name = name
        self.articles = articles
        self.combinations = self._get_combinations(supermarkets, max_to_visit)
        self.all_lists = map(
            lambda c: self._list_for_combination(c, self.articles),
            self.combinations)
        self.best_list = self._get_cheapest_list()

    def _get_cheapest(self, supermarkets, article_name):
        """
        Function the cheapest supermarket where to buy the article comparting
        between the given supermarkets.
        """
        articles = [(article, supermarket) for supermarket in supermarkets
                    for name, article in supermarket.articles.items()
                    if name == article_name]

        return min(articles, key=lambda x: x[0].price)

    def _list_for_combination(self, supermarkets, to_buy):
        """
        Function that generates the cheapest shopping list for the combination
        of supermarkets.
        """
        return [self._get_cheapest(supermarkets, art) for art in to_buy]

    def _get_cheapest_list(self):
        """
        Function that returns the cheapest combination of lists.
        """
        return min(self.all_lists,
                   key=lambda x: sum([article.price for article, _ in x]))

    def _get_combinations(self, supermarkets, total_to_visit):
        combinations = []
        for index, supermarket in enumerate(supermarkets):
            if total_to_visit == 1:
                combinations.append([supermarket])
            else:
                for result in self._get_combinations(supermarkets[index + 1:],
                                                     total_to_visit - 1):
                    combination = [supermarket]
                    combination.extend(result)
                    combinations.append(combination)

        return combinations

    def __str__(self):
        """
        Returns the string representation of all the articles within the list,
        the supermarket where to buy each article, and the total price of the
        list.
        """
        res = ["\n**********************************************"]
        res.append("\nShopping List: {}".format(self.name))
        res.append("\n**********************************************")
        res.append("\n__________________________________________________")
        for article, supermarket in sorted(self.best_list,
                                           key=lambda x: x[1].name):
            res.append("\n{}".format(str(article)))
            res.append(",\t Supermarket: {}".format(
                supermarket.name))
        res.append("\n__________________________________________________")
        res.append("\nTOTAL: {0:.2f}€".format(
            sum([article.price for article, _ in self.best_list])))
        return ''.join(res)


class UserInteraction:
    """
    Class that handles all the user interaction with the program.
    """

    def __init__(self, supermarkets):
        self.shopping_list = ShoppingList(
            self._get_list_name(),
            self._articles_to_buy(),
            supermarkets,
            self._max_supermarkets_to_visit(
                len(supermarkets)))

    def _max_supermarkets_to_visit(self, total_of_supermarkets):
        """
        Function that ask the user for the supermarkets that is willing to
        visit.
        """
        while True:
            n = input("\nFrom 1 to {}, how many supermarkets are "
                      "you willing to visit: ".format(total_of_supermarkets))
            try:
                supermarkets_to_visit = int(n)
                if supermarkets_to_visit in range(
                        1, total_of_supermarkets + 1):
                    break
                else:
                    print("The number of supermarkets must be"
                          "between 1 and {}".format(total_of_supermarkets))
            except ValueError:
                print("Please, type a number")

        return supermarkets_to_visit

    def _yes_or_no(self, query):
        """
        Function that ask the user a query that must answer with yes or no.
        """
        while True:
            answer = input("{} Y or N  ".format(query))
            try:
                if answer.lower() == 'y':
                    result = True
                    break
                elif answer.lower() == 'n':
                    result = False
                    break
                else:
                    print("Please, type a Y or N")
            except ValueError:
                print("Please, type a Y or N")
        return result

    def _articles_to_buy(self):
        """
        Function that ask the user for the articles to add to the list.
        """
        articles = []
        print("\nAnswer Y or N:")
        print("_______________________________________")
        while True:
            articles.extend([article['name'] for article in FAKE_ARTICLES if
                             self._yes_or_no("Would you like to buy {}?"
                                             "".format(article['name']))])
            if articles:
                break
            else:
                print("You must choose at least one article")

        return articles

    def _get_list_name(self):
        """
        Function that ask the user for the shopping list name.
        """

        return input("Give a name for your list: ")


class Region:

    def __init__(self):
        self.supermarkets = self._create_supermarkets()
        self._populate_supermarkets()

    def _create_supermarkets(self):
        return [Supermarket('Supermarket {}'.format(i))
                for i in range(1, TOTAL_SUPERMARKETS)]

    def _populate_supermarkets(self):
        for supermarket in self.supermarkets:
            for article in FAKE_ARTICLES:
                # Random price
                fake_price = article['price'] * random.uniform(0.8, 1.2)
                supermarket.add(
                    Article(
                        name=article['name'],
                        price=fake_price))

    def __str__(self):
        """
        Returns the string representation of all the supermarkets within the
        region.
        """
        res = ["\n**********************************************"]
        res.append("\nALL SUPERMARKETS")
        res.append("\n**********************************************")
        for supermarket in self.supermarkets:
            res.append(str(supermarket))
        res.append("\n**********************************************")
        return ''.join(res)


def main():
    region = Region()
    print(region)
    userInteraction = UserInteraction(region.supermarkets)
    print(userInteraction.shopping_list)


if __name__ == '__main__':
    main()
