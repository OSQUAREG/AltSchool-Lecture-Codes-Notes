##01 AUTHENTICATION & AUTHORIZATION##

**DEFINITIONS:**
AUTHENTICATION: is the act of validating that users are whom they claim to be. This is the first step in any security process.

- Passwords: Usernames and Passwords are the most common authentication factors.
- One Time Pins (OTP): grants access for only one session or transaction.
- Authentication Apps: generates authentication codes via app biometrics (fingerprints or eye scans)

AUTHORIZATION: is the process of giving the user permission to access a specific resource or function. This term is often used interchangeably with "Access Control" or "Client Privilege".

**HANDLING USER PASSWORDS, ENCRYPTING SENSITIVE DATA AND SESSIONS:**

**Sessions**:
In apps generally, login sessions are maintained so that once a user logs in, they can continue to access different parts of the app without having to log in (i.e authenticate) again and again for each subsequent "http" requests made to the server.

**How Session Works:\***
The Server:

- generates a "sessionID" (signs it using "secret key"), and
- saves the sessionID in a "sessionDB", and
- sends a cookie with the sessionID to the browser (client side).
  The Browser (client side):
- receives the "cookie" storage.
- then includes the "cookie" within every subsequent request to the server.

**JWT Authentication:**
JWT (JSON Web Token): is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.

**How JWT Works:**
The Server:

- generates an "accessToken", encrypting the "userId" and "expiresIn", with the ACCESS_TOKEN_SECRET, and
- sends the "accessToken" to the browser (client side).
  The Browser (client side):
- receives the "accessToken" and saves it on the browser.
- the "accessToken" is included in every subsequent request to the server.

**Adding JWT to our code:**

- Install the following: bcrypt and jwt
  We use:
- bcrypt for hashing user passwords, and
- jwt for signing tokens, retrieving and verifying JWT tokens.

\*\*JWT vs Sessions:

- JWT is "stateless", since no "state" or "session" is saves within a DB (it is contained within the JWT token itself)
- In Session, the sessionId does not contain any userId info, but is a random string generated and signed by the "secret key". The sessionId is then saved within a sessionDB. The sessionDB is a DB table that maps "sessionId" to the "userId".

- Session lookup can be slower becuase of lookups to SessionBD
- JWT allows for multiple servers to be scaled up separately and without the need to have a current copy of the sessionId DB on all servers, or have all servers access a common sessionDB.

\**Pros and Cons for Sessions:
*Advantages:

- Logout occurs at the moment the sessionID is removed from the sessionDB.

\*Disadvantages:

- Needs additional DB lookup within the table to get the userID. DB lookups are relatively slower.
- Individual servers cannot be scaled separately since they would need to share the sessionDB.

\**Pros and Cons of JWT
*Advantages:

- No DB call is required to get userID, so it makes it faster.
- Servers can be scaled separately, without the need to share sessionDB. Great option for micro-services architecture.
- The same token can be used to authenticate on different servers, as long as the server has the ACCESS_TOKEN_SECRET.
- It allows for a separate authentication server, that can be used to issue "access" and "refresh" tokens.

\*Disadvantages:

- JWT Tokens can be invalidated without maintaining them in the shared DB.

In JWT approach, the logout length precision is set by the expiration length of the access_token.

JWT Tokens should primarily contain the user info and the data authorize to be accessed by the user that should be provisioned and managed as a respective server.

\*\*Bearer Authentication:
Bear Auth (or Token Authentication) is an HTTP authentication scheme which comprises of security tokens called "bearer tokens". These tokens are usually cryptic strings and are generated in response to successful login on the part of the user.

A client must include this token in the Authorization header when making requests to any protected resources on the server.

\**How To Handle Logging Out When Using JWTs:
*Logout in JWT

- A popular saying in JWT logout is that "One does not simply logout" becuase it is stateless!

- Whenever a token is created, it can be used forever or until it expires. JWT generator can get an option to invalidate the token after a specified time.

\*What to do if you want to invlidate an existing token? What you really need to do when the user opts to log out or let's say change password?
Logout in JWT is Tricky, so

- Set a reasonable expiration time on tokens.
- Delete the stored token from client side upon log out.
- Have a DB of no longer active tokgitens that still have some time to live.
- Query provided token against the Blacklist on every authorized request.

\*\*OAUTH2 (Open Authorization)
OAUTH2 is a standard design to allow a website or app to access resources hosted by other web apps on behalf of a user.

It enables applications - such as Facebook, GitHun, Google - to obtain limited access to user accounts on an HTTPS service. It works by delegating user authentication to the service that hosts the user account, and authorizing third party applications to access that user account.

OAUTH2 uses Access Tokens. An Access Token is a piece of data that represents the authorization to access resources on behalf of the end-user. It doesn't define a specific format for Access Tokens. However, in some contexts, the JWT format is often used.

\*OAUTH2 Roles
Resource Owner: is the user who authorizes an application to access their account. The application access to the user's account is limited to the scope of the authorization granted, i.e. read or write access.

Client: is the application that wants to access the user's account. Before it can do so, it must be authorized by the user and validated by the API.

Resource Server: hosts the protected user accounts.

Authorization Server: verifies the identity of the user, then issues access tokens to the application.
