class Solution:
    # Gaurav Saini
    # Explanation: https://www.youtube.com/watch?v=nz5V5pOiT8w
    def dfs(self, n, x, done):
        if done[n] == 1: # If we are already visiting this node, then there is cycle
            return False
        done[n] = 1 # Mark current node as visiting
        for child in x[n]:
            if done[child] != 2: # If the child is not visited
                if not self.dfs(child, x, done): # If any of my child has a cycle, we do not need to check other children.
                    return False
        done[n] = 2 # All children of this node are processed, mark it visited
        return True

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        x = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            x[edge[1]].append(edge[0])
        done = [0]*numCourses # 0 = unvisited, 1 = visiting, 2 = visited
        for n in range(numCourses): # Run through all the courses to check if there is a cycle anywhere
            if done[n] == 0: # If the course is not complete (i.e. graph is unvisited on this node, perform DFS)
                no_cycle = self.dfs(n, x, done)
                if no_cycle == False:
                    return False
        return True

if __name__ == "__main__":
    soln = Solution()
    numCourses = 2
    preprerequisites = [[1, 0]]
    print(soln.canFinish(numCourses, preprerequisites))