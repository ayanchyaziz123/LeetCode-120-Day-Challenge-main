class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0  # Counter to track the number of operations needed
        for i in range(len(logs)):
            if logs[i] == "../":
                # Move to the parent folder (if not already in the main folder)
                if cnt == 0:
                    continue
                cnt -= 1
            elif logs[i] == "./":
                # Remain in the same folder
                continue
            elif logs[i] == "x/":
                # Move to the child folder
                while logs[i] != "x/" and i < len(logs):
                    i += 1
                    cnt += 1
            else:
                # Move to a named folder
                cnt += 1
        return cnt