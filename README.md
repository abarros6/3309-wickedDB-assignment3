3309 Assignment 3 - WickedDB_2 - November 2021

Authors: Anthony Barros, Prabh Simran Bhatia, Swarit Dholakia, Ryan Hayter, Andrew Tobar

QUESTION 2, 7 and 8 BELOW:

2.
<img width="632" alt="Screen Shot 2021-11-27 at 12 00 55 AM" src="https://user-images.githubusercontent.com/37852687/143668694-40029ade-5275-439c-aa46-73cd22855238.png">

7.
The first 2 views are updatable as they select from only one table and include the primary
keys with none of the missing data being set to not null, The third is not as it is composite
from 2 tables and does not include the primary key of either table.

8.
In MySQL, you are able to use indexed views which is not possible using MySQL. We
are able to create views and delete views, however, you are not able to edit the created
views that did not have the primary keys. Some other quirks about transaction support in
MySQL is that transactions do not roll back after errors and updates for create view
doesn’t work for GROUP BY but it still works for joining tables
