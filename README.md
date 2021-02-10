# API

Customer database API example.

Create a customer object and link any data sheet, profession, and documents.

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

### GET /api/professions/
Get a list of professions that can be registered on customer objects.
This url requires admin account.

### GET /api/documents/
Get a list of documents. 

### POST /api/documents/
Create a document object. This url requires authentication.
Attach authentication token to your header. 'Authorization: Token {Your token}'
