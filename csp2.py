from constraint import Problem

# Define variables for the CSP problem
problem = Problem()
problem.addVariable("E1", ["A", "R", "M", "P"])
problem.addVariable("E2", ["A", "R", "M", "P"])
problem.addVariable("E3", ["A", "R", "M", "P"])
problem.addVariable("E4", ["A", "R", "M", "P"])
problem.addVariable("E5", ["A", "R", "M", "P"])
problem.addVariable("E6", ["A", "R", "M", "P"])
problem.addVariable("E7", ["A", "R", "M", "P"])
problem.addVariable("E8", ["A", "R", "M", "P"])
problem.addVariable("E9", ["A", "R", "M", "P"])
problem.addVariable("E10", ["A", "R", "M", "P"])
problem.addVariable("E11", ["A", "R", "M", "P"])
problem.addVariable("E12", ["A", "R", "M", "P"])
problem.addVariable("E13", ["A", "R", "M", "P"])
problem.addVariable("E14", ["A", "R", "M", "P"])
problem.addVariable("E15", ["A", "R", "M", "P"])

def lJunction(x, y):
    if x == "R" and y == "P":
        return True
    elif x == "R" and y == "R":
        return True
    elif x == "P" and y == "R":
        return True
    elif x == "A" and y == "M":
        return True
    elif x == "A" and y == "A":
        return True
    elif x == "M" and y == "A":
        return True
    return False

def arrowJunction(x, y, z):
    if x == "A" and y == "P" and z == "A":
        return True
    elif x == "M" and y == "P" and z == "M":
        return True
    elif x == "P" and y == "M" and z == "P":
        return True
    return False

def forkJunction(x, y, z):
    if x == "A" and y == "A" and z == "M":
        return True
    elif x == "M" and y == "A" and z == "A":
        return True
    elif x == "A" and y == "M" and z == "A":
        return True
    elif x == "P" and y == "P" and z == "P":
        return True
    elif x == "M" and y == "M" and z == "M":
        return True
    return False

# Define the constraints for the CSP problem 
problem.addConstraint(lambda E1, E2: lJunction(E1, E2), ("E1", "E2"))
problem.addConstraint(lambda E5, E6: lJunction(E5, E6), ("E5", "E6"))
problem.addConstraint(lambda E7, E8: lJunction(E7, E8), ("E7", "E8"))
problem.addConstraint(lambda E4, E3, E14: forkJunction(E4, E3, E14), ("E4", "E3", "E14"))
problem.addConstraint(lambda E9, E11, E15: forkJunction(E9, E11, E15), ("E9", "E11", "E15"))
problem.addConstraint(lambda E12, E13, E15: forkJunction(E12, E13, E15), ("E12", "E13", "E15"))
problem.addConstraint(lambda E8, E9, E1: arrowJunction(E8, E9, E1), ("E8", "E9", "E1"))
problem.addConstraint(lambda E2, E10, E3: arrowJunction(E2, E10, E3), ("E2", "E10", "E3"))
problem.addConstraint(lambda E4, E15, E5: arrowJunction(E4, E15, E5), ("E4", "E15", "E5"))
problem.addConstraint(lambda E6, E13, E7: arrowJunction(E6, E13, E7), ("E6", "E13", "E7"))
problem.addConstraint(lambda E12, E14, E11: arrowJunction(E12, E14, E11), ("E12", "E14", "E11"))

# Solve the CSP problem
solutions = problem.getSolutions()
print(solutions)