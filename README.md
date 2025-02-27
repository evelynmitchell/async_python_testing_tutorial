# Async Python Testing Tutorial

I've been working on some async code in Python recently, and I noticed that testing it is tricker than I suspected, so I thought I'd share my notes.

## Brief review of async

### What is async?

Asynchronous code, or async code, is code that runs in parallel with other code.  This is in contrast to synchronous code, which runs in sequence with other code.  In synchronous code, one line of code runs, then the next, then the next, and so on.  In asynchronous code, one line of code runs, then another line of code runs, then another line of code runs, and so on.  The difference is that in asynchronous code, the lines of code don't necessarily run in order.

This allows you to wait for results from something that may be running elsewhere, such as an API call or the result of a long running calculation, without stopping the rest of your code from running.

#### Synchonous code


```mermaid
---
Synchronous
---
graph LR
A[Start] --> B{Condition}
B -- True --> C[Action]
C --> D[Next Action]
D --> B
B -- False --> E[End]
```

#### Asynchronous code

```mermaid
graph LR
A[Start] --> B{Condition}
B -- True --> C[Action]
C --> D[Next Action]
D -.-> B
B -- False --> E[End]
```

The dotted line from Next Action to Condition in the asynchronous code indicates that the code is not waiting for the result of the action before moving on to the next action.


### When do you need it?

You need synchronous code when you have code that needs to wait for something to happen before it can continue.  For example, if you have a function that needs to wait for a response from an API call before it can continue, you need sync'd code.  If you have a function that needs to wait for the result of a long running calculation before it can continue, you need synchronous code.

But, in modern code, you often need async code, because it allows you to run code in parallel with other code.  For example, if you have a web server that needs to handle a large number of requests, you can use async code to handle each request in parallel, rather than waiting for each request to finish before starting the next one.

Machine learning tools often use async code, because they need to wait for the results of long running calculations before they can continue, or because they are using agents to run tasks in parallel. AutoGPT and Langchain are two examples of machine learning tools that use async code.

### How do you use it?

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
```
```
Examples$ python3 hello_async.py 
Hello ...
... World!
```

You can't read the delay, but if you run the exaple, you'll see that the second print statement  '...World' is delayed by one second.

## Testing async code

First will create a little hello world function that is not async, and test it.

```python
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    print(hello_world())
```

```

```

```python

async_python_testing_tutorial
