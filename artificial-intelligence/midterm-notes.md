## Topics
### Chapter 1 and 2
- Understand 4 approaches to AI: acting humanly, thinking humanly, thinking, rationally, and acting rationally
- Example AI approach into one of the four approaches
- identify which other disciplines contributed ideas, viewpoints, and techinques to AI and how
- Given a real-world problem, discuss if it is easy, difficult, or almost impossible for the state-of-the-art AI to do it automatically
- Discuss some example risks and benefits of AI
- Understand the "gorilla problem" and "King Midas problem" in the context of risks and benefits of AI
    - Kind midas problem: Get what you literally ask for and then regret it
    - Gorilla problem: the branch which lead to gorillas and to humans. Gorillas are not too happy about the human branch
        - they have no control over their future.
        - Fear of creating something more intelligent than us will lead us to having no control over our own
- Understand the concepts: environment, percept sequence, agent function, and agent program
    - Percept: content an agent's sensors are perceiving
    - Environment: part of the universe whose state we carre about when designing the agent
    - Percept Sequence: complete history of everything the agent has ever perceived
    - Agent function: maps any given percept sequence to an action; abstract mathematical description
    - Agent Program: concrete implementation, running within some physical system
- Understand the definition and concept of a rational agent; also understand why a rational agent is not an omniscient/clairvoyant/successful agent
    - Rational agent is one that does the right thing. The right thing to an agent is based on consequentialism
        - evaluate an agent's behavior by its consequences
- Given an example agent type (and its description), specify task environment (PEAS) for it
    - Performance, Environment, Actuators, Sensors
- Clearly understand the conceptual differences between (and schematic diagrams of) the various kinds of agent programs:
    1. simple reflex agents
        - select actions based on current percept, ignoring rest of percept history.
    2. model-based reflex agents
        - adds two models:
            - Transition: updates internal state information as tiem goes by based on agents actions
            - Sensor: collect information about hwo state of the world is reflected in agent's percepts
    3. goal-based agents
        - keep track of the world state and set of goals it is trying to achieve
            - choose action that will (eventually) lead to achievement of goals
    4. utility-based agents and
    5. learning agents
### Chapter 3
- Concepts and definitions of search problem, state space, initial state, goal states, actions, transition model, action/path cost function, and optimal solution
- Concepts of abstraction and level of abstraction
- Understand states, initial state, actions, transition model, goal states, and action cost for the two-cell vacuum world problem and sokoban 8-puzzle problem
- Differentiate (with examples) route-finding problem, touring problem, VLSI layout, robot navigation, and automatic assembly sequencing
- Understand the distinction between state space vs. search tree
- Understand concepts and the distinction between:
- leaf node vs. frontier vs. state
- three types of queues
- Concepts and definitions of the four criteria used to evaluate a search algorithm's performance
- Intuition, concept, and comparison of the uninformed search strategies: BFS, UCS, DFS, Depth-limited, and Iterative deepening search
- Understand why and how iterative deepening search combines many benefits of depth-first and breadth-first search, including why repeating the previous levels is usually not actually wasteful
- Learn the correct reasons for all values of the cells in Figure (table) 3.15
    - precisely understand all parameters: b, d, m, C* (it is cost, not the solution),
- The concept of greedy best-first search
- Understand the concept of the A* search algorithm
- Learn how to trace the A* search algorithm, i.e., build a search tree for a given problem
- Concept of heuristic functions; h1 and h2 heuristic for 8/15 puzzle
### Chapter 4
- concept and definition of the following terms: local search, optimization problems, objective function, state-space landscape, global maximum/minimum, and local maximum/minimum
- Understand the 8-queen and n-queen problem
- Clearly understand the purpose of Figure 4.1 and all the terms and concepts associated with the figure
- Analyze and understand the concept of hill-climbing search
- Understand the HILL-CLIMBING algorithm enough to be able to trace it and implement it for a well-defined problem; for example, for the "finding the weights of AND gate" problem
- Learn the key idea of the simulated annealing algorithms and the purpose of all the parameters:
- The purpose of temperature and schedule
- The reason to calculate delta E
- The purpose of the probability component
- Understand the SIMULATED-ANNEALING algorithm enough to be able to trace it and implement it for a well-defined problem; for example, for the "finding the weights of AND gate" problem
- Learn the core idea of the local beam search and why it is different from k random restarts
- Understand the concepts of the fundamental ideas of evolution algorithms: recombination, population, fitness function, selection, crossover, and mutation (see Figure 4.6) 
- Understand the GENETIC-ALGORITHM algorithm well enough to be able to trace and implement it for a well-defined problem such as the 8-Queens problem
- Learn to calculate each step in Figure 4.6 (genetic algorithm) for any new set of random initial states
