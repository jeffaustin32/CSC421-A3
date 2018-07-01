from constraint import Problem

# Define variables for the CSP problem
problem = Problem()
problem.addVariable("f", [1])
problem.addVariable("t", [1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable("u", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable("w", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable("r", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable("o", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
problem.addVariable("c10", [0, 1])
problem.addVariable("c100", [0, 1])
problem.addVariable("c1000", [0, 1])

# Define the constraints for the CSP problem 
problem.addConstraint(lambda o, r, c10: o + o == r + (10*c10), ("o", "r", "c10"))
problem.addConstraint(lambda w, u, c10, c100: c10 + w + w == u + (10*c100), ("w", "u", "c10", "c100"))
problem.addConstraint(lambda o, t, c100, c1000: c100 + t + t == o + (10*c1000), ("o", "t", "c100", "c1000"))
problem.addConstraint(lambda f, c1000: f == c1000, ("f", "c1000"))
# All diff
problem.addConstraint(lambda f, t, u, w, r, o: len(set([f, t, u, w, r, o])) == 6, ("f", "t", "u", "w", "r", "o"))

# Solve the CSP problem
solutions = problem.getSolutions()
print(solutions)
print(len(solutions))
print(solutions)