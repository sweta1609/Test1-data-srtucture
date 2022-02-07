'''Does s contain t ?
Send Feedback
Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
Return true or false.
Do it recursively.
E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.'''

def contains(s, t):
    if(len(t) > len(s)):
        return False
    if(len(t) == len(s) and t == s):
        return True
    if(len(t) == 0):
        return True
    for i in range(len(s)):
        if s[i] == t[0]:
            return True and contains(s[i+1:], t[1:])
    return False
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')
