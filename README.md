# obole
Give your stuff, don't sell it: we take care of Charon's obol.

# API

Models are:

- users
- objects
- groups
- transactions

Actions are:

- user give object to user
- user lend object to user
- user exchange object against object with user (3 steps: offer/answer/confirm?)
- set transaction visibility
- set object permissions (permissions are to be defined)
- set object visibility
- set object custom visibility
- set user settings (settings are to be defined)
  - default permissions for newly acquired objects
  - default permissions for newly received (lend) objects
  - default permissions for newly created objects
  - default visibility for newly acquired objects
  - default visibility for newly received (lend) objects
  - default visibility for newly created objects
- user leave group
- user add user to group (private group)
- user request joining group (private group)? (would require Request model)
- user join group (public group)
- get user inventory
- get object tracking (limit ... me ... limit)
- get top givers/lenders/receivers/exchangers
- get user giving/lending/exchanging reputation
- get group giving/lending/exchanging reputation
- get user activity
- get group activity
- get user friends
- get group members

Hints:

- HTTP uses verbs: GET, POST, PUT, DELETE, PATCH,
  (http://www.restapitutorial.com/lessons/httpmethods.html), don't duplicate URLs.
  Example:  
  `api/users/thomas/objects` (GET) to see all objects,  
  `api/users/thomas/objects` (POST) to create an object,  
  `api/users/thomas/objects/ID` (GET) to see one object,  
  `api/users/thomas/objects/ID` (DELETE) to delete an object,  
  etc.
- Always use plural form: `api/users` instead of `api/user`. Be consistent.
- Use parameters wisely: http://stackoverflow.com/questions/4024271/rest-api-best-practices-where-to-put-parameters
- Use shortcuts when for many and often used parameters.