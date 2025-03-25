# Card_collection

This is a free program to store the data of your card collection of a game, like Magic: The gathering.

To add cards to your collection you must have a .txt file with the quantity and the name of the card, for instance:
```
3 Duress
2 Negate
```
this way you can add full decks to your collection at once. The .txt file must be in this format (MTGO Format of decks).

Then to actually add the cards you type
```
python3 add.py deck.txt
```
this will add the cards to your collection.txt, which already is in the repositore (empty), if you already have some of the cards, it will just increase the number os the card.

If you want to delete some of the cards, you must have a .txt file with the quantity and the cards that you want to take out of your collection, and then type
```
python3 delete.py deck.txt
```
this will move the cards away from your collection and put in a trash.txt. This trash.txt is useful for the next thing that our prorgram can do.

If you want to buy new cards, giving up of some complete deck that you have, you can delete the deck that you will give up with delete.py, this will store the cards in trash.txt, and then
```
python3 swap.py deck.txt
```
where this time, deck.txt is the new deck that you want to buy. This function will print which cards you already have, and which ones you need to buy.

Another function is the minus.py. Suppose that you have a big .txt file with some cards and want to take out a list of the, with another .txt file you can take out the cards from the big.txt with the cards of small.txt, doing
```
python3 minus.py big.txt small.txt
```
I recommend doing this with temporary files so you dont mess up with your collection.txt (not that it's difficult to redo the collection with add.py, it is just a recomendation).

Other function is compare.py, which will takes two .txt deck files and compare then, and say which cards are in both lists and wich ones are not, you do
```
python3 compare.py 1.txt 2.txt
```
this will print the cards that are in both lists, the cards that are only in the first .txt and the cards that are only in the second .txt.

If you have any tips or recomendations of how to improve the program, feel free to add issues or pull requests.


## How I use the program

After cloning the repositore, I create a directory called 'decks' and copy and paste the lists .txt of all the decks that I have. Then added one by one with add.py. Now, anytime that I want to buy a new deck,
giving up of one or more of mine, I can delete then and the use swap.py to check which cards I already have, then if I want to add back the cards from the trash that I will not use on the new deck on my collection,
I create a temporary file with the cards that I already have (compared with the new deck), and then I minus.py from the trash.txt, and then add the trash.txt back to my collection with add.py.

Maybe there is something or another that you want to do with your collection that the functions that I wrote don't cover up, in this case you will have to edit the file by hand, and feel free to make a pull request explaning
what you wanted that the functions could do to help.
