### **Project Setup and Requirements**

1. **Environment Setup**

   - Ensure you have Python 3.7 installed.
   - Install required packages with `pip3 install -r requirements.txt`.
   - Start the server with `API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app`.

2. **Resources to Read/Watch**
   - **REST API Authentication Mechanisms**
   - **Base64 in Python**
   - **HTTP header Authorization**
   - **Flask Documentation**
   - **Base64 - Concept**

### **Learning Objectives**

By the end of this project, you should be able to:

- Explain what authentication is.
- Understand Base64 encoding and how to use it in Python.
- Know how Basic Authentication works and how to implement it.
- Send and handle the Authorization header in requests.

### **Tasks Breakdown**

1. **Simple Basic API**

   - Download and set up the provided project.
   - Test the API endpoints to ensure they are working.

2. **Error Handler: Unauthorized (401)**

   - Modify `api/v1/app.py` to add a custom error handler for 401 status codes.
   - Add a new route in `api/v1/views/index.py` that triggers this error.

3. **Error Handler: Forbidden (403)**

   - Update `api/v1/app.py` to handle 403 status codes.
   - Add a route in `api/v1/views/index.py` to trigger a 403 error.

4. **Auth Class**

   - Create an `Auth` class in `api/v1/auth/auth.py` with placeholder methods.
   - Implement methods like `require_auth`, `authorization_header`, and `current_user`.

5. **Define Routes Without Authentication**

   - Update the `require_auth` method in the `Auth` class to handle paths that don’t require authentication.

6. **Request Validation**

   - Implement request validation in `api/v1/app.py` using the `Auth` class.
   - Set up `before_request` hooks to handle authorization and authentication checks.

7. **BasicAuth Class**

   - Create a `BasicAuth` class inheriting from `Auth` in `api/v1/auth/basic_auth.py`.
   - Implement Base64-related methods to extract and decode credentials from the Authorization header.

8. **Base64 Decode**
   - Complete the Base64 decoding functionality in the `BasicAuth` class to handle authentication properly.

### **Example Implementations**

**Error Handler for 401:**

In `api/v1/app.py`:

```python
from flask import Flask, jsonify

@app.errorhandler(401)
def unauthorized_error(error):
    return jsonify({"error": "Unauthorized"}), 401
```

**Adding a Route that Triggers 401:**

In `api/v1/views/index.py`:

```python
from flask import abort

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    abort(401)
```

**BasicAuth Class:**

In `api/v1/auth/basic_auth.py`:

```python
import base64

class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header):
        if (authorization_header is None or
            not isinstance(authorization_header, str) or
            not authorization_header.startswith('Basic ')):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self, base64_authorization_header):
        if (base64_authorization_header is None or
            not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
```

### **Testing Your Implementation**

1. **Run the Server:**

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

2. **Test Endpoints:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   curl "http://0.0.0.0:5000/api/v1/unauthorized"
   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64_credentials>"
   ```

### **Routes**

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
