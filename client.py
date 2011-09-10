class Client:
  import shelve
  
  filename = "clients.shelve"
  client = dict()

  def __setattr__(self, key, value):
    self.client[key] = value

  def __getattr__(self, key):
    return self.client[key]

  def getNewClientId(self):
    d = self.shelve.open(self.filename)

    if (d.has_key("seq")):
      id = d["seq"] + 1
    else:
      id = 1

    d.close()

    return id

  def save(self):
    id = self.getNewClientId()
    self.client["id"] = id

    d = self.shelve.open(self.filename)
    d["seq"] = id
    d[str(id)] = self.client

    d.close()
