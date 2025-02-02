from profil3r.app.search import search_get
import time

class Wikipedia:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['wikipedia']['rate_limit'] / 1000
        # https://en.wikipedia.org/wiki/User:{username}
        self.format = config['plateform']['wikipedia']['format']
        # Wikipedia usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # Collaborative
        self.type = config['plateform']['wikipedia']['type']

    # Generate all potential wikipedia usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        wikipedia_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            r = search_get(username)
            if not r:
                continue
                
            
            # If the account exists
            if r.status_code == 200:
                wikipedia_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return wikipedia_usernames