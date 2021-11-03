'''
kind of a dumb question

Time complexity: O(N) because split function requires O(N) time and O(N) space
space complexity: O(N) because split function 
'''

class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        
        if '.' in IP:
            spl = IP.split('.')    
            
            if len(spl) != 4:
                return 'Neither'
            
            for ele in spl:
                if len(ele) > 1:
                    if ele[0] == '0':
                        return 'Neither'
                if not ele.isdigit():
                    return 'Neither'
                if int(ele) > 255 or int(ele) < 0:
                    return 'Neither'
                    
            return 'IPv4'
            
        elif ':' in IP:
            spl = IP.split(':')
            hexdigits = '0123456789abcdefABCDEF'
            
            if len(spl) != 8:
                return 'Neither'
            
            for ele in spl:
                if len(ele) > 4 or len(ele) < 1:
                    return 'Neither'
                for letter in ele:
                    if letter not in hexdigits:
                        return 'Neither'
            
            return 'IPv6'
            
        else:
            return 'Neither'