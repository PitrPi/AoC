import re

from Helpers.helpers import read_newest
# import os
# os.chdir('y2020/task_16')
if __name__ == '__main__':

    data = read_newest()

    def parse_data(data):
        instructions = {"global_mins": [], "global_maxs": []}
        your_ticket = []
        nearby_tickets = []
        target = 'instructions'
        for dat in data:
            if dat == 'your ticket:':
                target = 'your_ticket'
                continue
            elif dat == 'nearby tickets:':
                target = 'nearby_tickets'
                continue
            elif dat == '':
                continue
            if target == 'instructions':
                ranges = re.findall("[0-9]+", dat)
                mins = ranges[::2]
                mins = [int(x) for x in mins]
                maxs = ranges[1::2]
                maxs = [int(x) for x in maxs]
                instructions[re.findall(".*(?=:)", dat)[0]] = {
                    'mins': mins,
                    'maxs': maxs
                }
                instructions["global_mins"].extend(mins)
                instructions["global_maxs"].extend(maxs)
            elif target == 'your_ticket':
                your_ticket.append(dat.split(','))
            elif target == 'nearby_tickets':
                nearby_tickets.append(dat.split(','))
        return instructions, your_ticket, nearby_tickets

    def check_value_in_range(value, mins, maxs):
        for mn, mx in zip(mins, maxs):
            if mn <= value <= mx:
                return True
        return False

    instructions, your_ticket, nearby_tickets = parse_data(data)
    # Part 1
    failed_numbers = []
    for ticket in nearby_tickets:
        for y in ticket:
            y_int = int(y)
            if check_value_in_range(y_int, instructions["global_mins"], instructions["global_maxs"]):
                continue
            else:
                failed_numbers.append(y_int)

    print(sum(failed_numbers))

    # Part 2

    valid_tickets = []
    for idx, ticket in enumerate(nearby_tickets):
        valid = True
        for y in ticket:
            y_int = int(y)
            if check_value_in_range(y_int, instructions["global_mins"], instructions["global_maxs"]):
                continue
            else:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    def decide_fields(valid_tickets, instructions):
        """Given valid tickets and restrictions in instructions
        decide which positions could be filled be which field
        Returns list of possible field names for each index
        """
        # Start with transposing. So transposed[0] is first values in each ticket
        transposed = list(map(list, zip(*valid_tickets)))
        possible_fields_all = []
        for field_values in transposed:
            # For every value on first position check validity in every possible field
            possible_fields = []
            for instruction_nm, instruction_val in instructions.items():
                if instruction_nm == 'global_mins' or instruction_nm == 'global_maxs':
                    continue
                # If all values for given fields satisfy requirement for given field
                # add name of that field to possible fields
                if all([
                        check_value_in_range(
                        int(value), instruction_val['mins'], instruction_val['maxs'])
                        for value
                        in field_values]):
                    possible_fields.append(instruction_nm)
            possible_fields_all.append(possible_fields)
        return possible_fields_all

    def reduce_fields(possible_fields, final=None):
        """
        This eliminates possibilities from decide_fields
        :param possible_fields: What is still possible
        :param final: this dictionary contains solved elements. Key=name of field, value=index on ticket
        :return:
        """
        if final is None:
            final = {}
        final_len = len(final)
        # Map - find trivial pairings
        # If given index has only one possible name assing this to final
        for idx, possible_field in enumerate(possible_fields):
            if len(possible_field) == 1:
                final[possible_field[0]] = idx
        # Reduce
        # From possible fields remove field names, that was already assigned in final
        # This also ensures that we do not double assign, since possible fields for solved
        # indexes will be empty
        possible_fields = [[name
                            for name
                            in field
                            if name not in final.keys()]
                           for field in possible_fields]
        # If we made any progress, call this function again and further reduce the possibilities
        if len(final) > final_len:
            reduce_fields(possible_fields, final)
        # Once there are no trivial solutions return final
        return possible_fields, final


    possible_fields = decide_fields(valid_tickets, instructions)
    _, final_fields = reduce_fields(possible_fields)
    final_value = 1
    for k, v in final_fields.items():
        if k[:len('departure')] == 'departure':
            final_value *= int(your_ticket[0][v])
    print(final_value)