REST API using Python EVE

REGISTRATION

	endpoint: /users/register
	method: POST
	parameters: 
		firstname
		lastname
		mobile
		email
		birthday
		password

USER
	Get user details
	
	method: GET
	endpoint: users/<users_id>

	return:
		full details of user


STORE
	
	Get store details

	endpoint: /stores/<store_id>
	method: GET

	return:
		full details of the store

	--

	endpoint: /stores
	method: POST
	parameters:
		storename
		address
		contact

MYSTORE

	endpoint: /users/<users_id>/mystore
	method: POST
	parameters:
		storename

	--
	
	Get specific my store of the user
	
	endpoint: /users/<int:id>/mystore
	method: GET

	return:
		store name

HEALTH ADVISORS
	
	endpoint: /stores/<store_id>/healthadvisors
	method: POST
	parameters:
		name
		specialty

	--

	endpoint: /stores/<store_id>/healthadvisors
	method: GET

	return:
		full details of the health advisors

