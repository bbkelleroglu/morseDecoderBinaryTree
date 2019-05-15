# morseDecoderBinaryTree
A python module that creates a complete and balanced binary tree for morse code. By using that module you can decode or translate morse code string to its sentence.


<img width="900" alt="Screen Shot 2019-05-15 at 20 26 17" src="https://user-images.githubusercontent.com/47689166/57795916-d0c1e300-774f-11e9-8989-7d2dc6b7e531.png">


The above decision tree is in the form of complete and balanced binary tree like a binary-heap. Starting root node does not contain any value, all the left nodes have a dot (.) and right nodes have a line (-) as a decision expansion. Some characters may have 1, some may have 2, 3, 4 or 5 notations.
For example:
A : .-
X : -..-

A python code which I used this binary tree while decoding Morse alphabet. Finding left and right child of each node indexes in this tree with the formulas that I used in binary heap (i.e. left= 2j, right= 2j+1)

You can test my code by using this morse code string :  .-- .. - .... .-.- -- -.-- .-.- -... . ... - .-.- .-- .. ... .... . ...
