"""
RADOI BOGDAN-MIHAI 333CB
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

import threading

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.producer_id = -1
        self.cart_id = -1
        self.product_list = []
        self.taken_product_list = []

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        lock = threading.Lock()
        lock.acquire()
        self.product_list.append([])
        lock.release()
        self.producer_id += 1
        return self.producer_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        lock = threading.Lock()
        if len(self.product_list[producer_id]) < self.queue_size_per_producer:
            lock.acquire()
            self.product_list[producer_id].append(product)
            lock.release()
            return True
        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        lock = threading.Lock()
        lock.acquire()
        self.taken_product_list.append([])
        lock.release()
        self.cart_id += 1
        return self.cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        lock = threading.Lock()
        for id_prod in range(0, len(self.product_list)):
            for i in self.product_list[id_prod]:
                if i == product:
                    lock.acquire()
                    self.product_list[id_prod].remove(i)
                    self.taken_product_list[cart_id].append(
                        {"idprodus" : id_prod, "produs" : product})
                    lock.release()
                    return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        lock = threading.Lock()
        for i in self.taken_product_list[cart_id]:
            if i["produs"] == product:
                lock.acquire()
                self.product_list[i["idprodus"]].append(product)
                self.taken_product_list[cart_id].remove(i)
                lock.release()
                break

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        lock = threading.Lock()
        final_list = []
        for i in self.taken_product_list[cart_id]:
            lock.acquire()
            final_list.append(i["produs"])
            lock.release()
        return final_list
