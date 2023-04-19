## **Multi-armed bandit**
Gracz wchodzi do kasyna i staje przed rzędem automatów do gry, z różnymi wskaźnikami wypłat. Gracz nie wie, który automat da mu najwięcej pieniędzy, ale ma określony czasu i ograniczoną ilość pieniędzy do wydania.

Problem wielorękiego bandyty polega na próbie znalezienia automatu, który da graczowi najwięcej pieniędzy, minimalizując jednocześnie straty. Każdy automat to jakby "ręka" bandyty, a gracz musi zdecydować, która ręka ma zostać pociągnięta (lub który automat ma zostać wybrany) w celu uzyskania jak największej sumy pieniędzy.

Jednak gracz nie zna dokładnego wskaźnika wypłat każdego automatu, więc musi eksperymentować i próbować różnych maszyn, aby dowiedzieć się, które z nich są najbardziej dochodowe. Im więcej gra, tym lepiej poznaje automaty, które dają najwięcej pieniędzy, i dostosowuje swoją strategię odpowiednio.

To jak próba zrównoważenia eksploracji (próbowania nowych automatów, aby poznać ich wskaźniki wypłat) i eksploatacji (grania na automatach, które już wiadomo, że mają wysoki wskaźnik wypłat) w celu maksymalizacji całkowitej wygranej.