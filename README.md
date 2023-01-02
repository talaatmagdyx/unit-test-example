# Quick Example for Python tests

- [x] unittest/mocks [Intro to  Mocks](unittest/Intro%20to%20%20Mocks)
    - Intro to Python Mocks from unittest.mock library: what are Python mocks, why we have to use mocks, and when to do it.
    - How to write Python tests for functions that make a request to external API.
    - How to use the patch function to test Requests based functions with Python unittest.mock library. 

- [x] unittest/mocks [Mocking_Exceptions](unittest/Mocking_Exceptions)
    -  How to raise an exception from a test, and how to mock an exception using the .side_effect property.
    - Fixing the 'TypeError: catching classes that are not inherit from BaseException is not allowed' when mocking an exception.
    - Using the .raise_for_status() function from the requests library
    - Writing a test to test raise_for_status(), and mocking raise_for_status
    - Checking status codes within an except clause of the try/except block.

- [x] unittest/mocks [Mocking_Python_Requests_with_Responses](unittest/Mocking_Python_Requests_with_Responses)
    - Writing a test for a function that should return value if JSON object with a certain structure is provided
    - Testing the raise_for_status() function with Python Responses library.
    - Testing a logic when Exception is raised
### Why Python mocks are important:
- Mocks eliminate dependency on network, database calls, calls to OS (it will speed testing)
- we get isolated unit tests,
- we can test methods that have no return value
- reduce test complexity. We don't have to write complex logic to handle behavior of methods under tests.
- don't have to wait to implement other methods.
