# REST API Summary Notes

## Overview
- **APIs (Application Programming Interfaces)** come in many forms and allow access to data, services, algorithms, media, and more through web URLs.
- **Postman** offers a public collection of APIs (including REST, GraphQL, and SOAP) to help newcomers learn and experiment.

## What is a REST API?
- REST (Representational State Transfer) is a **software architectural style** for creating web services.
- It uses HTTP methods and a uniform interface for interaction.
- REST APIs are widely used today in web, mobile, and device applications.

## History of REST APIs
- **Before REST**: Developers used SOAP, which was complex and XML-based.
- **2000**: Roy Fielding and others defined REST principles.
- **2002**: eBay and Amazon launched REST APIs.
- **2004-2006**: Flickr, Facebook, and Twitter introduced REST APIs.
- **Today**: REST is the standard, with tools like Postman simplifying API development and testing.

## REST API Standards
- **Uniform interface**: Unique resources via single URLs.
- **Client-server**: Separation of concerns.
- **Stateless**: Each request contains all necessary context.
- **Caching**: Responses are labeled as cacheable or not.
- **Layered system**: Components only see immediate layers.
- **Code on demand**: Servers can send executable code when needed.

## How REST APIs Work
- **Resources**: Named information (documents, images, collections, etc.).
- **Main HTTP methods**:
  - `GET`: Retrieve data.
  - `PUT`: Update data.
  - `POST`: Create new data.
  - `DELETE`: Remove data.

## REST vs. SOAP
- **SOAP**: Protocol, uses XML, strict, often enterprise.
- **REST**: Style, uses JSON, URLs, HTTP, flexible, widely adopted.

## Uses of REST APIs
- **Cloud applications**: Stateless, scalable.
- **Cloud services**: Bind services via URLs.
- **Web applications**: Client-agnostic, works on any platform.

## Benefits of REST APIs
- Scalability.
- Flexibility & portability.
- Independence between client and server.
- Lightweight and fast (supports JSON, XML, HTML).

## Challenges of REST APIs
- Maintaining consistent endpoint formats.
- Managing API versioning.
- Handling authentication.

## Common Authentication Methods
- **HTTP Authentication**:
  - Basic (username & password in header).
  - Bearer (token in header).
- **API Keys**: Unique identifiers, but can be intercepted.
- **OAuth**: Combines passwords and tokens for secure access.

## Security Considerations
- Ensure proper authentication.
- Implement rate limiting & throttling.
- Encrypt payload data.
- Correctly use HTTPS.
- Avoid exposing unnecessary data.

## Best Practices
- Use correct HTTP status codes (200, 404, 400, 500, 302, 401).
- Provide clear, informative error messages.
- Secure APIs with sanitization, authentication, role-based access.
- Version APIs to avoid breaking changes.
- Provide thorough documentation.
- Implement filtering, sorting, and pagination.
- Use nouns (not verbs) in endpoint paths.

## REST API Examples
- **Amazon S3**: AI, ML, data science services.
- **Twitter API**: Social media integration, marketing.
- **Instagram API**: Access to user profiles, media.
- **Plaid**: FinTech data integration.

## Final Thoughts
- REST APIs offer flexibility and power for both fun and business.
- Postman provides tools, collections, and glossaries to help you explore, test, and understand APIs more effectively.

Keep growing and learning about APIs to strengthen your development skills!

- Note: Follow this link to read the whole documentation: https://blog.postman.com/rest-api-examples/
