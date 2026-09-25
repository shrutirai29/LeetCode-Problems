class Solution:
    def braceExpansionII(self, expression: str):
        
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    # Parse everything inside braces
                    inside, i = parse(i + 1)

                    # Concatenate current × inside
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                elif expression[i] == ',':
                    # Union current into result
                    result |= current
                    current = {""}
                    i += 1

                else:
                    # A single lowercase letter
                    current = {
                        s + expression[i]
                        for s in current
                    }
                    i += 1

            # Add the last concatenated part
            result |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)