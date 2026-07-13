s=list(map(int,input()).split())
        stack=[]
        pairs={")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in "([{":
                stack.append(ch)    """Stack.append(ch)-- to store every opening bracket because we don't know 
                when it will be closed. We save it so we can match it later when a closing bracket appears."""
            else:
                if not stack or stack[-1]!=pairs[ch]: """stack[-1] means top element stack says last in first out 
                    We check if not stack to avoid accessing stack[-1] when the stack is empty. Otherwise,
                    Python throws an IndexError."""
                    return False
                stack.pop()     """to remove the opening bracket after it has been successfully matched
                                    with a closing bracket.
                                    Matched → Remove
                                    Not Matched → Return False"""
        return not stack
    """At the end, if the stack is empty, it means every opening bracket 
                              found its matching closing bracket, so the string is valid."""



def isValid(s):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for ch in s:

        if ch in "([{":

            # Store every opening bracket.
            # We don't know when it will be closed.
            stack.append(ch)

        else:

            # If stack is empty, or top doesn't match
            if not stack or stack[-1] != pairs[ch]:
                return False

            # Brackets matched.
            # Remove the opening bracket.
            stack.pop()

