# Magic collection manager

This is a free program to manage your card collection of Magic: The gathering.

To add cards to your collection you must have a .txt file in MTGO format
```
3 Duress
2 Negate
```
this way you can add full decks to your collection at once.

Then to actually add the cards to your collection you do
```
python3 add.py path_to_decklist.txt path_to_collection.txt
```
this will create and add the cards to a collection.txt (if doesn't exist yet). If you already have some of the cards, it will just increase the number of the card. You don't need to use this function only to add cards to your collection, you can add any .txt files. 

If you want to take out some of the cards of a list, you use a smaller .txt file with the cards and the quantity that you want to take out from a bigger file, you do
```
python3 take_out.py smaller_list.txt bigger_list.txt
```
which means, 'bigger_list - smaller_list', be careful to not change the order of the files, either a menssage will be prompt showing which list will be reduced, and you will have to confirm.

If you want to compare two deck lists, to check wich cards are in both lists and wich are not, you do
```
python3 compare.py 1.txt 2.txt
```
this will print the cards that are in both lists, the cards that are only in the first list and the cards that are only in the second list.

## How I use the program

I usually import decks from sites like mtgo.com, mtggoldfish.com, mtgtop8.com, etc..., you can download the .txt file or copy and paste by yourself. Then once I use add.py to update my collection.

If you already have a good collection you can use compare.py to check which cards are on your collection, and then copy and paste the cards that you already have into a .txt file and then use take_out.py to take out the cards that you have from the list of the deck that you want to build. 

When I want to build a new deck giving up of one of mines, I take out (with take_out.py) the deck that I have from my collection.txt, and them I compare to the deck that I want to build to check which cards I need to buy.

## Conclusion

I know that MTGO / MTG Arena already their own collection manager, but my thought are more about who plays physical mtg and those who want to take a look at the code.

This is a personal project to practice my programming skills, but in a way or another it might be useful to you, so feel free to use the way that you want.

If you have any tips or recomendations of how to improve the program, feel free to add issues or pull requests.
