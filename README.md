# Async Python Testing Tutorial

I've been working on some async code in Python recently, and I noticed that testing it is tricker than I suspected, so I thought I'd share my notes.

## Brief review of async

### What is async?

Asynchronous code, or async code, is code that runs in parallel with other code.  This is in contrast to synchronous code, which runs in sequence with other code.  In synchronous code, one line of code runs, then the next, then the next, and so on.  In asynchronous code, one line of code runs, then another line of code runs, then another line of code runs, and so on.  The difference is that in asynchronous code, the lines of code don't necessarily run in order.

This allows you to wait for results from something that may be running elsewhere, such as an API call or the result of a long running calculation, without stopping the rest of your code from running.

#### Synchonous code


graph LR
A[Start] --> B{Condition}
B -- True --> C[Action]
C --> D[Next Action]
D --> B
B -- False --> E[End]

#### Asynchronous code

graph TB
A[Start] --> B{Condition}
B -- True --> C[Action]
C --> D[Next Action]
D -.-> B
B -- False --> E[End]


### When do you need it?

### How do you use it?


async_python_testing_tutorial
