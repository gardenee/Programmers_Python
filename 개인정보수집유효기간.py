class day:
    def __init__(self, date):
        self.year, self.month, self.date = map(int, date.split("."))

    def end_date(self, period):
        self.date -= 1
        if self.date == 0:
            self.date = 28
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1

        self.month += period
        if self.month > 12:
            self.year += self.month//12
            self.month %= 12
            if self.month == 0:
                self.month = 12
                self.year -= 1

    def is_valid(self, today):
        result = True

        if self.year < today.year:
            result = False
        elif self.year == today.year:
            if self.month < today.month:
                result = False
            elif self.month == today.month:
                if self.date < today.date:
                    result = False

        return result


def solution(today, terms, privacies):
    answer = []
    today = day(today)

    term_dict = dict()
    for term in terms:
        term_type, months = term.split()
        term_dict[term_type] = int(months)

    for i in range(len(privacies)):
        privacy = privacies[i]
        date, term_type = privacy.split()

        date = day(date)
        date.end_date(term_dict[term_type])

        if not date.is_valid(today):
            answer.append(i+1)

    return answer
