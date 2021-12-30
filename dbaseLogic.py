entries = []


def addEntry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})


def getEntries():
    return entries
