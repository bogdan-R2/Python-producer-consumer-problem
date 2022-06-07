# Producer-Consumer Problem

In clasa producer am verificat daca exista loc in coada de produse si daca da se va publica un produs dupa timpul specificat pentru fiecare. In caz contrar se asteapta un timp dat si se incearca din nou

In clasa consumer am efectuat operatiile de add si remove parcurgand lista de cart-uri

In clasa marketplace am generat un id pentru fiecare producer.
In publish adaug un produs daca exista loc in lista, in caz contrar intorc false. In new_cart am generat un id pentru fiecare cart, in add_to_cart adaug produsul daca exista pe "lista de cumparaturi" a consumatorului, astfel devenind
rezervat.
Remove from cart va inlatura produsul din lista de produse rezervate
Dupa procesarea produselor se va lansa operatia de place_order.

Sincronizarea se va realiza prin lock-uri dar si prin operatiile threadsafe din python.

Printre dificultatile intampinate se numara nevoia de a returna un produs la producator.
Am reusit sa rezolv aceasta problema prin utilizarea unui dictionar, atasand fiecarui produs, id-ul producatorului sau.
