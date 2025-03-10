class Ticket:
    def __init__(self, flight_number, departure_station, arrival_station, departure_time, available_seats):
        self.flight_number = flight_number
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.available_seats = available_seats

class Passenger:
    def __init__(self, last_name, first_name, departure_station, arrival_station, desired_departure_time, ticket_purchased=False, flight_number=None):
        self.last_name = last_name
        self.first_name = first_name
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.desired_departure_time = desired_departure_time
        self.ticket_purchased = ticket_purchased
        self.flight_number = flight_number
    def __add__(self, passengers):
        passengers.append(self)

def load_data(filename, class_type):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                parts = line.strip().split()
                if class_type == Ticket:
                    data.append(Ticket(parts[0], parts[1], parts[2], parts[3], int(parts[4])))
                elif class_type == Passenger:
                    ticket_purchased = parts[5] != 'No'
                    flight_number = parts[5] if ticket_purchased else None
                    data.append(Passenger(parts[0], parts[1], parts[2], parts[3], parts[4], ticket_purchased, flight_number))
            if class_type == Ticket:
                data.sort(key=lambda x: x.departure_time)
            return data
    except FileNotFoundError:
        return []

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item.flight_number} {item.departure_station} {item.arrival_station} {item.departure_time} {item.available_seats}\n")

def save_passengers(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item.last_name} {item.first_name} {item.departure_station} {item.arrival_station} {item.desired_departure_time} {item.flight_number if item.ticket_purchased else 'No'}\n")

def add_passenger(passengers):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    departure_station = input("Введите станцию отправления: ")
    arrival_station = input("Введите станцию прибытия: ")
    desired_departure_time = input("Введите желаемое время отправления (HH:MM): ")
    Passenger(last_name, first_name, departure_station, arrival_station, desired_departure_time)+passengers
    print("Пассажир добавлен.")

def add_flight(tickets):
    flight_number = input("Введите номер рейса: ")
    departure_station = input("Введите станцию отправления: ")
    arrival_station = input("Введите станцию прибытия: ")
    departure_time = input("Введите время отправления (HH:MM): ")
    available_seats = int(input("Введите количество свободных билетов: "))
    tickets.append(Ticket(flight_number, departure_station, arrival_station, departure_time, available_seats))
    tickets.sort(key=lambda x: x.departure_time)
    print("Рейс добавлен.")

def compare_time(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    return (h1 * 60 + m1) <= (h2 * 60 + m2)

def match_tickets(passengers, tickets):
    for passenger in passengers:
        if not passenger.ticket_purchased:
            for ticket in tickets:
                if (passenger.departure_station == ticket.departure_station and
                    passenger.arrival_station == ticket.arrival_station and
                    compare_time(passenger.desired_departure_time, ticket.departure_time) and
                    ticket.available_seats > 0):
                    passenger.ticket_purchased = True
                    passenger.flight_number = ticket.flight_number
                    ticket.available_seats -= 1
                    print(f"Билет для {passenger.last_name} {passenger.first_name} на рейс {ticket.flight_number} куплен.")
                    break

def delete_flight(tickets, passengers, flight_number):
    found = False
    for ticket in tickets:
        if ticket.flight_number == flight_number:
            found = True
            break

    if not found:
        print(f"Рейс {flight_number} не найден.")
        return

    tickets[:] = [t for t in tickets if t.flight_number != flight_number]

    for passenger in passengers:
        if passenger.flight_number == flight_number:
            passenger.ticket_purchased = False
            passenger.flight_number = None

    print(f"Рейс {flight_number} удален.")

def print_table(data, headers):
    col_widths = [len(header) for header in headers]
    for row in data:
        for i, item in enumerate(row):
            if len(str(item)) > col_widths[i]:
                col_widths[i] = len(str(item))


    header_row = ""
    for i, header in enumerate(headers):
        header_row += f"{header:<{col_widths[i]}}  "
    print(header_row)


    separator = ""
    for width in col_widths:
        separator += "-" * width + "  "
    print(separator)


    for row in data:
        row_str = ""
        for i, item in enumerate(row):
            row_str += f"{str(item):<{col_widths[i]}}  "
        print(row_str)


tickets = load_data('tickets.txt', Ticket)
passengers = load_data('passengers.txt', Passenger)

while True:
    print("\n1 - Вывести список всех поездов\n2 - Вывести список всех пассажиров\n3 - Добавить пассажира\n4 - Добавить поезд\n5 - Вывести пассажиров рейса\n6 - Подобрать билеты всем пассажирам\n7 - Удалить рейс\n0 - Завершить работу")
    choice = input("Выберите действие: ")
    if choice == '1':
        print_table([[t.flight_number, t.departure_station, t.arrival_station, t.departure_time, t.available_seats] for t in tickets], ["Номер рейса", "Отправление", "Прибытие", "Время", "Свободные места"])
    elif choice == '2':
        print_table([[p.last_name, p.first_name, p.departure_station, p.arrival_station, p.desired_departure_time, p.flight_number if p.ticket_purchased else 'No'] for p in passengers], ["Фамилия", "Имя", "Отправление", "Прибытие", "Желаемое время", "Рейс"])
    elif choice == '3':
        add_passenger(passengers)
    elif choice == '4':
        add_flight(tickets)
    elif choice == '5':
        flight_number = input("Введите номер рейса: ")
        print_table([[p.last_name, p.first_name] for p in passengers if p.flight_number == flight_number], ["Фамилия", "Имя"])
    elif choice == '6':
        match_tickets(passengers, tickets)
    elif choice == '7':
        flight_number = input("Введите номер рейса для удаления: ")
        delete_flight(tickets, passengers, flight_number)
    elif choice == '0':
        save_data('tickets.txt', tickets)
        save_passengers('passengers.txt', passengers)
        break
    else:
        print("Неверный ввод. Пожалуйста, попробуйте снова.")