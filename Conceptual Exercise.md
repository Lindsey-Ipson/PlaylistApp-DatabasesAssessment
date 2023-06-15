### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

PostgreSQL is an open source relational database management system. It's a tool for creating and managing databases for an application. It allows you to define tables, columns, and relationships for data and then query and manipulate data as well as add delete data.

- What is the difference between SQL and PostgreSQL?

SQL is a standardized language that provides syntax and commands for managing and manipulating relationship databases. It is a specified language but does not implement anything. On the other hand, PostgreSQL is an implementation of a relational database management system following the standard specifications of the SQL language.

- In `psql`, how do you connect to a database?

`\c name_of_database`

- What is the difference between `HAVING` and `WHERE`?

The clauses `HAVING` and `WHERE` are both used to filter data from a query, with the main difference being that `WHERE` filters rows before any grouping or aggregation, while `HAVING` filters grouped data after the grouping/aggregation has taken place. In other words, 	`HAVING` is used when `GROUP BY` can also be found in the query, while `WHERE` can not. Moreover, `WHERE` operates on individual rows and `HAVING` operatea on groups of rows.
 
- What is the difference between an `INNER` and `OUTER` join?

An 	`INNER` join combines rows from tables based on a related column between them. It returns only the rows where values match on both sides. An `OUTER` join can either be a `LEFT JOIN`, `RIGHT JOIN`, OR `FULL JOIN`. It combines rows as well but returns not only the matching rows but also non-matching rows from the left, right, or both sides of the table depending on the type of join (left, right, or full). It uses NULL values for columns of the non-matching table(s).

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

A `LEFT` join returns all of the rows from the first table (left), combined with matching rows from the second table (right). A `RIGHT` join returns matching rows from the first table (left), combined with all the rows from the second table (right).

- What is an ORM? What do they do?

ORM stands for Object-Relational Mapping and it facilitates the relationship between object-oriented languages and relational database management systems. Usually, object-oriented programming languages work with objects, which are instances of classes containing data and methods. However, data is typically stored in relational databases consisting of tables of rows and columns. ORM frameworks facilitate that relationship by providing a mechanism to map objects to database tables and vice versa.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
  
AJAX requests are usually used for client-side interactions with APIs, allowing for a more interactive user experience, while server-side requests are usually used for server-to-server communication or when the request invlives server-side logic and/or resources.

- What is CSRF? What is the purpose of the CSRF token?

CSRF tokens help prevent any site submitting a form to any other site. To combat this, most websites include a CSRF (cross-site request forgery) token in the HTML of the form whenever a form is shown, which is then checked by the server upon form submission. For example, in Flask-
WTF, the method `validate_on_submit` checks for CSRF tokens.

- What is the purpose of `form.hidden_tag()`?

`form.hidden_tag()` includes a hidden input field inside a form which allows for the addition of extra data or metadata that's not directly visible or editable by the user. This hidden input field does not get displayed on the web page but is still included when the form's submitted, allowing the server-side code access to the hidden data.

