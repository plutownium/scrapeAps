# https://www.w3schools.com/tags/ref_urlencode.ASP

x = "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

print(x.replace("%22", '"').replace("%7B", "{").replace("%7D", "}"))

x = "insideBoundingBox=%5B%5B45.45344020494669%2C-73.65633240761402%2C45.6491408097154%2C-73.46235505165698%5D%5D"

print(x.replace("%5B", "[").replace("%2C", ",").replace("%5D", "]"))
