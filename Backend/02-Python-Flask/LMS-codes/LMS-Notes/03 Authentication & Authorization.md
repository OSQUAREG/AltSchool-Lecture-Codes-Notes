# 01 AUTHENTICATION & AUTHORIZATION

## Definitions:

**Authentication**: is the act of validating that users are whom they claim to be. This is the first step in any security process.

- **_Passwords_**: Usernames and Passwords are the most common authentication factors.
- **_One Time Pins (OTP)_**: grants access for only one session or transaction.
- **_Authentication Apps_**: generates authentication codes via app biometrics (fingerprints or eye scans)

**Authorization**: is the process of giving the user permission to access a specific resource or function. This term is often used interchangeably with "Access Control" or "Client Privilege".

## Handling User Passwords, Encrypting Sensitive Data and Sessions

### **SESSION**:

In apps generally, login sessions are maintained so that once a user logs in, they can continue to access different parts of the app without having to log in (i.e authenticate) again and again for each subsequent "http" requests made to the server.

**_How Session Works:_**

The Server:

- generates a "sessionID" (signs it using "secret key"), and
- saves the sessionID in a "sessionDB", and
- sends a cookie with the sessionID to the browser (client side).

The Browser (client side):

- receives the "cookie" storage.
- then includes the "cookie" within every subsequent request to the server.

### **JWT AUTHENTICATION:**

JWT (JSON Web Token): is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.

**_How JWT Works:_**

The Server:

- generates an "accessToken", encrypting the "userId" and "expiresIn", with the ACCESS_TOKEN_SECRET, and
- sends the "accessToken" to the browser (client side).

The Browser (client side):

- receives the "accessToken" and saves it on the browser.
- the "accessToken" is included in every subsequent request to the server.

**_Adding JWT to our code:_**

- Install the following: bcrypt and jwt
  We use:
- bcrypt for hashing user passwords, and
- jwt for signing tokens, retrieving and verifying JWT tokens.

### **JWT vs Sessions:**

- JWT is "stateless", since no "state" or "session" is saves within a DB (it is contained within the JWT token itself)
- In Session, the sessionId does not contain any userId info, but is a random string generated and signed by the "secret key". The sessionId is then saved within a sessionDB. The sessionDB is a DB table that maps "sessionId" to the "userId".

- Session lookup can be slower because of lookups to SessionBD
- JWT allows for multiple servers to be scaled up separately and without the need to have a current copy of the sessionId DB on all servers, or have all servers access a common sessionDB.

**Pros and Cons for Sessions:**

**_Advantages_**:

- Logout occurs at the moment the sessionID is removed from the sessionDB.

**_Disadvantages:_**

- Needs additional DB lookup within the table to get the userID. DB lookups are relatively slower.
- Individual servers cannot be scaled separately since they would need to share the sessionDB.

**Pros and Cons of JWT**

**_Advantages:_**

- No DB call is required to get userID, so it makes it faster.
- Servers can be scaled separately, without the need to share sessionDB. Great option for micro-services architecture.
- The same token can be used to authenticate on different servers, as long as the server has the ACCESS_TOKEN_SECRET.
- It allows for a separate authentication server, that can be used to issue "access" and "refresh" tokens.

**_Disadvantages:_**

- JWT Tokens can be invalidated without maintaining them in the shared DB.

In JWT approach, the logout length precision is set by the expiration length of the access_token.

JWT Tokens should primarily contain the user info and the data authorize to be accessed by the user that should be provisioned and managed as a respective server.

### **BEARER AUTHENTICATION:**

Bear Auth (or Token Authentication) is an HTTP authentication scheme which comprises of security tokens called "bearer tokens". These tokens are usually cryptic strings and are generated in response to successful login on the part of the user.

A client must include this token in the Authorization header when making requests to any protected resources on the server.

**How To Handle Logging Out When Using JWTs:**

**_Logout in JWT_**

- A popular saying in JWT logout is that "One does not simply logout" becuase it is stateless!
- Whenever a token is created, it can be used forever or until it expires. JWT generator can get an option to invalidate the token after a specified time.

**_What to do if you want to invlidate an existing token? What you really need to do when the user opts to log out or let's say change password?_**

_Logout in JWT is Tricky, so..._

- Set a reasonable expiration time on tokens.
- Delete the stored token from client side upon log out.
- Have a DB of no longer active tokgitens that still have some time to live.
- Query provided token against the Blacklist on every authorized request.

### **OAUTH2 (OPEN AUTHORIZATION)**

OAUTH2 is a standard design to allow a website or app to access resources hosted by other web apps on behalf of a user.

It enables applications - such as Facebook, GitHun, Google - to obtain limited access to user accounts on an HTTPS service. It works by delegating user authentication to the service that hosts the user account, and authorizing third party applications to access that user account.

OAUTH2 uses Access Tokens. An Access Token is a piece of data that represents the authorization to access resources on behalf of the end-user. It doesn't define a specific format for Access Tokens. However, in some contexts, the JWT format is often used.

**OAUTH2 Roles**

**_Resource Owner_**: is the user who authorizes an application to access their account. The application access to the user's account is limited to the scope of the authorization granted, i.e. read or write access.

**_Client_**: is the application that wants to access the user's account. Before it can do so, it must be authorized by the user and validated by the API.

**_Resource Server_**: hosts the protected user accounts.

**_Authorization Server_**: verifies the identity of the user, then issues access tokens to the application.

**_Adding Google OAUTH2_**

- Register your app with the OAUTH GCP.
- Search for OAUTH consent screen.
- Pick External and Ignore domain setup.
- Add scopes.
- Go to credentials and create new OAUTH Client ID.
- Add local redirect and origin URLs.
- Get client ID and Secret.
- Use in your app.

### **BEST PRACTICES FOR AUTHENTICATION**

- Hash your passwords
- Allow for third-party identity providers if possible.
- Separates the concepts of user identity and user account.
- Don't block long or complex passwords.
- Don't impose unreasonable rules for usernames.
- Allow users to change their username.
- Let your users delete their accounts.
- Make a conscious decision on session length.
- Use 2-Step Verification.
- Make user IDs case-insensitive.
- Build a secure auth system.

## Third-Party Authentication Services, Libraries with Auth0, AWS & Fire Base

**Why 3rd Party Authentication?**

- You're a startup or simply can't bear the financial overhead.
- You can't ensure the proper data mgmt and security.
- A data breach can break your organization.

**Examples of Third-Party Auth providers**

- Firebase
- Auth0
- AWS Cognito
- Supabase
- Authy
- Okta
- One Login

### **Third Party Authentication Services with Auth0**

**_Steps:_**

- Register on Auth0, and goto dashboard
- A free account offers you:
  - 7,000 free active users and unlimited logins
  - Auth0 Universal Login for Web, iOS & Android.
  - Up to 2 social identity providers like Google, GiHub and Twitter.
  - Unlimited Serverless Rules to customize and extend Auth0's capabilities.

# 02 DATA VALIDATION
This ensures the data you receive is i a proper format. You can either use a manual way or a validation library or package to code it.

For example, flask_restx, flask_pydantic etc can be used for data validation.

## Rate Limiting

this is a very powerful feature for securing backend APIs from malicious attacks and handling unwanted streams of request from users.

Generally, it is used to control the rate at which users request are processed by the server.

**Why Use Rate Limiting**

- There is better flow of data.
- There is a reduced risk of attack, i.e., improved security.
- The server is never overloaded.

**Application of Rate Limiting**
Rate Limiting can be applied on:
- **_Users_** - constraint is user specific, and implemented using a unique user identifier.
- **_Location_** - constraint is based on geography, and implemented based on the location from which the request is made.
- **_IP Addresses_** - constraint is based on the IP address of the device that initiates a request.

**Rate Limiting Techniques**
- **_Fixed Window Counter_** - tracks the _number_ of requests a user makes in each window.
- **_Sliding Logs_** - tracks the _timestamp_ for each request a user makes.
- **_Sliding Window Counter_** - combines fixed counter window and sliding logs.
- **_Leaky Bucket_** - this algorithm makes use of a queue that accepts and processes requests in a first in, first out (FIFO) manner. The limit is enforced on the queue size.

## Logging - Why and How
In computing, a **_Log File_** is a file that records either events that occur in an operating system, or software that runs, or messages between different users of communication software.

**_Logging_** is an act of keeping a log.

### **Why Logging in Important**
- Reading and analyzing and making sense of errors when they happen and when they break is your first line of defense when battling production downtime.
- Logs tells you what happens, what is misbehaving in your app and the root cause of the issue you want to fix.
- Logs helps you solve problems and maintain maximum uptime.

### **What Data to Log**
- Log as much data as you can.
- With more data, you can visualize issues easier.
- The better structure you create for the logs, the easier you can solve issues like errors, infos and debugs.

### **What Not to Log**
- Credit card info, passwords, secret keys, user's personal data.
- Logs are considered data by law, and laws like GDPR require you not to expose or misuse user data.

### **Where to Save Logs**
- Store logs in a persistent place where you can easily search, e.g. **_Elasticsearch_**.
- You can host it yourself or use a hosted setup, or use a Log Management Systems like: **_Sentry, Logly, McAfee Enterprise, Graylog, Splunk, Logmatic, or Logstash_**

