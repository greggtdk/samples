"""
Expand encoded string

Recursive solution to expand encoded string.
"""

class ExpandEncoded:
   
    def expand(self, s):
        i = 0
        
        def parse():
            nonlocal i  # this is needed to modify the i in the outer scope
            
            answer = []
            while i < len(s) and s[i] != "]":
                # read consecutive digits to get the number of repetitions
                # didn't mention this during our discussion
                if s[i].isdigit():
                    d = 0
                    while s[i].isdigit():
                        d = 10 * d + int(s[i])
                        i += 1
                
                    # skip the [ after the digits - always there in a well formed and valid input          
                    i += 1
                    
                    # recursively call parse to get the string inside the brackets
                    string = parse()
                
                    # skip the ] after the string - always there in a well formed and valid input
                    i += 1

                    # repeat the segment d times
                    answer.extend(string for _ in range(d))
                else:
                    answer.append(s[i])
                    i += 1
            return "".join(answer)
        
        return parse()


if __name__ == '__main__':
     
    expandEncoded = ExpandEncoded()

    test1 = "3[a]"
    print(expandEncoded.expand(test1))

    test2 = "2[b]1[c]"
    print(expandEncoded.expand(test2))

    test3 = "4[5[d]e]"
    print(expandEncoded.expand(test3))