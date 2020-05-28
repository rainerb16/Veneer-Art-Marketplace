# ---------- Art Marketplace Dealership Software ---------

# Create class Art
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  
  def __repr__(self):
    return "{}. {}. {}, {}, Owner: {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)


# Create class Marketplace
class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, remove_listing):
    self.listings.remove(remove_listing)

  def show_listings(self):
    for lists in self.listings:
      print(lists)


# Create class Client
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    if is_museum == True:
      self.location = location
    else:
      self.location = "Private Collection"


  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(Listing(artwork, price, self))

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
    for listing in veneer.listings:
      if listing.art == artwork: 
        art_listing = listing
        break
    if art_listing != None:
      artwork.owner = self
      veneer.remove_listing(art_listing)


# Create class Listing
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return "{}, {}".format(self.art.title, self.price)



#---------- Works of Art / Client ----------
veneer = Marketplace()

edytta = Client("Edytta Halpirt", False, None)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas.", edytta)
#print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "6M (USD)")

moma = Client("The MOMA", "New York", True)

moma.buy_artwork(girl_with_mandolin)



#---------- Testing: Uncomment to test----------
#print(girl_with_mandolin)
#print(veneer.show_listings())