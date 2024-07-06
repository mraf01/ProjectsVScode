from datetime import datetime

class DateDatabase:
    def __init__(self):
        self.dates = {}

    def add_date(self, date_str):
        date = self._str_to_date(date_str)
        if date:
            self.dates[date_str] = date
        else:
            raise ValueError("Invalid date format. Use gg.mm.aaaa")

    def delete_date(self, date_str):
        if date_str in self.dates:
            del self.dates[date_str]
        else:
            raise ValueError("Date not found in the database.")

    def modify_date(self, old_date_str, new_date_str):
        if old_date_str in self.dates:
            new_date = self._str_to_date(new_date_str)
            if new_date:
                del self.dates[old_date_str]
                self.dates[new_date_str] = new_date
            else:
                raise ValueError("Invalid new date format. Use gg.mm.aaaa")
        else:
            raise ValueError("Old date not found in the database.")

    def query_date(self, date_str):
        if date_str in self.dates:
            return date_str
        else:
            raise ValueError("Date not found in the database.")

    def _str_to_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            return None

if __name__ == "__main__":
    db = DateDatabase()
    db.add_date("01.01.2024")
    print(db.query_date("01.01.2024"))
    db.modify_date("01.01.2024", "02.02.2024")
    db.delete_date("02.02.2024")