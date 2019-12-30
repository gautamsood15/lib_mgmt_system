#lib_mgmt_system

This is a library management system designed using PyQt and python.
To store the book info we use the mysql database and it also has a login system.

In this you can register/remove a book as well as borrow it for a certain period  of time.



PROJECT STRUCTURE

Library Management System :
	- add new book
	- editing book
	- deleting book
	- categories
	- search
	- users , login , signup
	- settings [categories , author , publisher]
	- day to day operations
	- generate reports [excel files]


	book :
		- code
		- title
		- description
		- category
		- price
		- author
		- publisher

	users :
		- username
		- password
		- email addr

	day_to_day :
		- book name
		- retrieve / rent
		- days

	category :
		- category name

	publisher :
	 	- publisher name

	 author :
	 	- author name