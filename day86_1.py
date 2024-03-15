class Solution:
    def average(self, salary: List[int]) -> float:
        # Sort the list of salaries in ascending order
        salary.sort()
        
        # Initialize variables to count the number of employees and the total salary
        emp = 0
        total = 0
        
        # Iterate through the sorted list of salaries, excluding the first and last elements
        for i in range(1, len(salary)-1):
            emp += 1  # Increment the employee count for each salary
            total += salary[i]  # Add the salary to the total
        
        # Calculate and return the average salary
        return total / emp
