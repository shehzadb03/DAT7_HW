Using chipotle.tsv in the data subdirectory:

1. Look at the head and the tail, and think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

** Each column is represented as an item. We notice, by looked at head, that there are multiple items with order # 1.  
``` head chipotle.tsv``` ```tail chipotle.tsv``` **



How many orders do there appear to be? ** 1834 Based on the last order by executing ```tail chipotle.tsv``` **

How many lines are in the file? ** 4523 ```wc -l chipotle.tsv```**

Which burrito is more popular, steak or chicken? ** Chicken. ```grep -c "Chicken Burrito" chipotle.tsv ``` = 553, whereas ```grep -c "Steak Burrito" chipotle.tsv``` = 368 **

Do chicken burritos more often have black beans or pinto beans? ** Black Beans. 

``` grep "Chicken Burrito" chipotle.tsv | grep -c "Black Beans" ``` = 282
``` grep "Chicken Burrito" chipotle.tsv | grep -c "Pinto Beans" ``` = 105 **

Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.

** ``` ls -a **/*sv ``` **

Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo. 

** 16 ```grep -rohi 'Dictionary' dat7 | wc -w ``` **