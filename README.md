REST - Representational State Transfer

## cafe management
## Source - https://github.com/TechGram-Academy/Rest-APIs-with-database
get-items - get all items in the cafe menu
get-item  - get given item from menu
add-items - add item to the menu
delete-item - delete te given item.

db
CREATE TABLE item
(
   id varchar(32) primary key,
   name varchar(100),
   price int
)

insert into item (id, name, price) values ('f87498038e0044f3bb49add503aa1520', 'apple', 160)
insert into item (id, name, price) values ('f87498038e0044f3bb49add503aa1521', 'orange', 100)
SELECT * FROM item WHERE id = 'f87498038e0044f3bb49add503aa1520'
