
# get url function 

host = "157.230.209.171"
user = "curie_944"
password = "A6LUTZA9MPbUSy89niNy0Fd9qyI2tF8h"

def get_url(database):
    host = "157.230.209.171"
    user = "curie_944"
    password = "A6LUTZA9MPbUSy89niNy0Fd9qyI2tF8h"
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'