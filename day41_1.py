from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Initialize class attributes
        self.numCourses = numCourses
        self.prerequisites = prerequisites
        self.graph = defaultdict(list)  # Adjacency list to represent the graph
        self.in_degree = [0] * numCourses  # Array to store in-degrees of courses
        self.build_graph()  # Build the graph based on prerequisites
        return self.can_finish()  # Check if it's possible to finish all courses

    def build_graph(self):
        # Populate the graph and in-degree array based on prerequisites
        for course, prereq in self.prerequisites:
            self.graph[prereq].append(course)  # Add directed edge from prereq to course
            self.in_degree[course] += 1  # Increment in-degree of the course

    def can_finish(self):
        # Initialize a queue with courses having in-degree 0
        queue = deque([course for course in range(self.numCourses) if self.in_degree[course] == 0])

        while queue:
            current_course = queue.popleft()
            for neighbor in self.graph[current_course]:
                self.in_degree[neighbor] -= 1  # Reduce in-degree of the neighbor
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)  # If in-degree becomes 0, add to the queue

        # Check if all courses have in-degree 0, indicating it's possible to finish all courses
        return sum(self.in_degree) == 0

# Example usage
numCourses = 2
prerequisites = [[1, 0]]

solution = Solution()
output = solution.canFinish(numCourses, prerequisites)
print(output)  # Output: True
