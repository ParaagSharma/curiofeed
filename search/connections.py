from elasticsearch_dsl import connections
from decouple import config

# Read ES host from env
ELASTICSEARCH_HOST = config("ELASTICSEARCH_HOST", default="http://localhost:9200")

# Create a default ES connection
connections.create_connection(hosts=[ELASTICSEARCH_HOST])
