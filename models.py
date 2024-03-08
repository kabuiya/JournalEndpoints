# storing entries in memory not database
class Entries:
    def __init__(self):
        self.items = []

    # get
    def get_entries(self):
        return self.items

    # post
    def add_entries(self, new_entry):
        if len(self.items) == 0:
            new_entry['id'] = 0
            self.items.append(new_entry)
        else:
            new_entry['id'] = (len(self.items))
            self.items.append(new_entry)
        return self.items

    # get a certain entry by its id
    def get_entry(self, entry_id):
        for ent in self.items:
            if ent.get('id') == entry_id:
                return ent
        return None

    # update an entry first check if element you want to update exists
    def update_entry(self, entry_id, update_with):
        for ele in self.items:
            if ele.get('id') == entry_id:
                ele_to_update = ele
                update_with['id'] = entry_id
                ele_to_update.update(update_with)
                return self.items
        return None

    # delete enty
    def delete_entry(self, entry_id):
        for ele in self.items:
            if ele.get('id') == entry_id:
                ele_to_del = ele
                self.items.remove(ele_to_del)
                return self.items
        return None
