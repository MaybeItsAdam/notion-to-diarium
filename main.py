import os
from datetime import datetime

all_days = os.listdir("./days")

all_data = []


def convert_date(input_date):
  date_obj = datetime.strptime(input_date, '%B %d, %Y')

  yyyy_mm_dd = date_obj.strftime('%Y-%m-%d')
  dd_month = date_obj.strftime('%e %B')
  weekday = date_obj.strftime('%A')

  return [yyyy_mm_dd, dd_month, weekday]


for day in all_days:
  # [2023-10-19,19 October,Thursday,23:40,good,"","Title","day stuff"]

  date = day[1:len(day) - 36]

  day_data = convert_date(date)

  day_data += ["12:00", "none", "\"\""]

  with open("./days/" + day, "r", encoding="utf-8") as day_file:
    notes = []
    for i, line in enumerate(day_file):

      if i == 4:
        day_data.append(line[3:len(line) - 1])
      if i >= 8:
        notes.append(line)
      if "<aside>" in line:
        break

    day_data.append(''.join(notes[:len(notes) - 2]).replace("\n\n",
                                                            "\n").replace(
                                                                "\n", "<br>"))

  final_data = ",".join([
      day_data[0], day_data[1], day_data[2], day_data[3], day_data[4],
      day_data[5], "\"" + day_data[6] + "\"", "\"" + day_data[7][:-4] + "\"",
      "\n"
  ])

  all_data.append(final_data)

with open("output.csv", "a", encoding="utf-8") as plate:
  for data in all_data:
    plate.write(data)
