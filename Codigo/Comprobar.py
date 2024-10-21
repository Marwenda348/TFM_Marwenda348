import re



def whitelist(self):

    for i in self:
        Whitelist = re.search(r"[a-zA-Z0-9./]",i)
        if not Whitelist:
            return None
    
    if Whitelist:
        return self