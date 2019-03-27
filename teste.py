import utils as u
from visitedlinks import VistedLinks

vl = VistedLinks()

print(vl.repeated_links("https"))
print(vl.repeated_links("http"))
print(vl.repeated_links("a"))
