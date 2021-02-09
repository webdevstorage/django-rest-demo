# API

### GET /api/
Get a list of all endpoints in the API

### POST /api-token-auth/
Get authentication token using 'username' and 'password'

### GET /api/customers/
Get a list of customers

### POST /api/customers/
Create a customer object with 'name', 'address'

### GET /api/data-sheet/
Get a list of data sheets

### POST /api/data-sheet/
Create a new data sheet

### GET /api/documents/
Get a list of documents. This path requires authentication.
Attach authentication token to your header. 'Authorization: Token {Your token}'

