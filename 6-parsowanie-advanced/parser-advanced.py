import re


file = open('input.txt', 'r').read()
file = file.replace('\n', ',')

ticket_details, rest = file.split(',your ticket:,')
your_ticket, nearby_tickets = rest.split(',,nearby tickets:,')
ticket_details = ticket_details.replace(',', ':,')

ticket_details = ticket_details.split(',')
your_ticket = your_ticket.split(',')
nearby_tickets = nearby_tickets.split(',')

print('Ticket_details: ', ticket_details)
print('Your_ticket: ', your_ticket)
print('Nearby_tickets: ', nearby_tickets, '\n')

passes, failes = [], []
for number in nearby_tickets:
    for detail in ticket_details:
        if detail != '':
            searcher1 = re.findall(r'\:\ (\d*)\-', detail)[0]
            searcher2 = re.findall(r'\-(\d*)\ ', detail)[0]
            searcher3 = re.findall(r'\ (\d*)\-', detail)[0]
            searcher4 = re.findall(r'\-(\d*)\:', detail)[0]
            if searcher1 <= number <= searcher2 or searcher1 <= number <= searcher2:
                passes.append(number)
                break
            else:
                failes.append(number)
                break

failes_int = [int(var) for var in failes if var]
print('Number of passes: ', len(passes))
print('Number of failes: ', len(failes))
print('Sum of failes: ', sum(failes_int))
