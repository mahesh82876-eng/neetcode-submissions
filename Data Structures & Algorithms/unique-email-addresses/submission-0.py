class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap=set()

        for e in emails:
            local,domain=e.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            hashmap.add((local,domain))
        return len(hashmap)