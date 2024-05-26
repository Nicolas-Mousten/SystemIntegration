OAuth:
The end-user or the entity that owns the resource.
The resource server (OAuth Provider) is the entity hosting the resource.
The client (OAuth Consumer) is the entity looking to consume the resource after getting authorization from the client.


JWT (Jason web tokens)
Pros: Compact, self-contained tokens that can carry authentication and authorization information. Stateless, which can improve scalability.
Cons: Tokens can grow large if too much information is included. Requires careful implementation to avoid security vulnerabilities like token leakage.


API Keys
Pros: Simple and easy to implement. Suitable for scenarios where there's no need for user-specific access control.
Cons: Lack of fine-grained access control. Vulnerable to interception if not transmitted securely.


HTTP Basic Authentication:
Pros: Simple to implement and widely supported by HTTP servers and clients. No need for additional libraries.
Cons: Credentials are sent with every request, which can be a security risk if not transmitted over HTTPS. No built-in mechanism for token expiration or revocation.





https://docs.google.com/document/d/1wlAqZnkBAwj4WtJx0MSK_S0_sRkxcMRQ2mafoNnqETQ/edit?usp=sharing
