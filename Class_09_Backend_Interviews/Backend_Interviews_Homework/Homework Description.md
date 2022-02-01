# Backend Interview Homework

- Write down your answers for the following questions and then paste your answers into the "Backend Assignment" quiz on learningsuite. You can use the internet.

1. What is CI/CD? What are some good CI/CD practices?
    My answer: CI stands for continuous integration. It refers to the process of constantly integrating a teams changes to a project into a central repository of code. CD stands for continuous delivery. It is a software dev practice where changes are automatically prepared for deployment to production. This will combine with CI to constantly update the code and constantly test that code for production.
    Good CI/CD practices include:
    - commit early, commit often.
    - keep the builds green (automated tests on committed changes to ensure code is being built on functional base)
    - build only once (don't restart from a new build, use the previous one and add to it)
    - streamline your tests (don't test in depth for every change, just quick testing)
    - clean your environments
    - make it the only way to deploy to production
    - monitor and measure your pipeline
    - make it a team effort
    sources: atlassian.com, aws.amazon.com, jetbrains.com
2. What is and what are the benefits of using a binary tree?
    My answer: A binary tree is a hierarchical data structure with a root (the parent node) which connects with every node through it's children elements. Each node has at most 2 children elements and only one parent element. If a node has no children elements, it is a leaf node.
    Benefits of using a binary tree include 
    - hierarchical way of storing data (helpful for reflecting some structural reslationships that exist in the given data set)
    - quick insertion/deletion (compared to lists/arrays)
    - flexible way of holding and moving data
    - can store many nodes
    - faster than linked lists, (but slower than arrays) when accessing elements
    source: upgrad.com
3. What does SOLID mean?
    My answer: 
    SOLID stands for: 
    - Single responsibility principle (a class should have one, and only one, reason to change - a class should solve only one problem)
    - Open-closed principle (you should be able to extend a class' behavior without modifying it)
    - Liskov substitution principle (every derived class should be substitutable for its parent class)
    - Interface segregation principle (make fine grained interfaces that are client-specific. clients should not be forced to implement interfaces  they do not use)
    - Dependency inversion principle (developers should depend on abstractions, not on concretions)
    source: bmc.com
4. What is abstraction? Give an example.
    My answer: Abstraction is the idea that complexity is handled without the user having to worry about it or understand it. This hides the unneccessary information from the user. For example, the sum() function in many languages is used without the user having to worry about exactly how things are summed behind the scenes.
    source: stackify.com
5. What is a singleton? Give an example of when to use this principle.
    My answer: A singleton is a class that only allows itself to be instantiated once. It seems that the most common example of when to use this principle would be have a sort of global variable that is actually a singleton's one instantiation.
    source: techopedia.com