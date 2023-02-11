# npuzzle-search
Exploring a variety of search techniques variants of the (modified) N-puzzle for CS534 (Artificial Intelligence). Team members are Neil Kale, Lauren Stanley, Ankit Mittal, Ashkan Ganj, and Rutwik Kulkarni.

![Alt text](tiles.PNG?raw=true "Title")


Please run our program by calling `npuzzle.py`, in the `code` folder from the main `npuzzle-search` folder. The arguments are:
* Board file name, with the board located in the main npuzzle-search folder.
* Heuristic method 
  * `sliding` will run A* using the manhattan distance heuristic detailed in Part 1
  * `part2` will run the hill climbing search detailed in Part 3
  * `greedy` will run A* using the greedy search heuristic detailed in Part 3 
* Weighted tile boolean
  * `false` will use a strict Manhattan distance
  * `true` will use the weighted Manhattan distance

For example:
`python .\code\npuzzle.py board1.csv greedy false`

Will solve board 1 using the greedy search heuristic with the strict Manhattan distance.
