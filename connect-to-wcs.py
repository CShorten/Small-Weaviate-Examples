from getpass import getpass
import weaviate
from weaviate.wcs import WCS

my_creds = weaviate.auth.AuthClientPassword(username=input("User name: "), password=getpass("Password: "))

my_wcs = WCS(my_creds)

client = weaviate.Client("https://abstract-vectors.semi.network")
