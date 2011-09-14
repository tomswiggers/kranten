class Client:
  import shelve
  
  filename = "clients.shelve"
  client = dict()

  def __setattr__(self, key, value):
    self.client[key] = value

  def __getattr__(self, key):
    if key in self.client:
      return self.client[key]
    else:
      return ""

  def getValue(self, key):
    if key in self.client:
      return self.client[key]
    else:
      return ""

  def setValue(self, key, value):
    self.client[key] = value

  def getNewClientId(self):
    d = self.shelve.open(self.filename)

    if (d.has_key("seq")):
      id = d["seq"] + 1
    else:
      id = 1

    d.close()

    return id

  def getClientById(self, id):
    d = self.shelve.open(self.filename)
    id = str(id)

    if (d.has_key(id)):
      client = d[id]

      for k, v in client.items():
        self.client[k] = v

    d.close()

    return self.client

  def save(self):
    id = self.getNewClientId()
    self.client["id"] = id

    d = self.shelve.open(self.filename)
    d["seq"] = id
    d[str(id)] = self.client

    d.close()
