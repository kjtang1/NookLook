import requests
import psycopg2
from db_config import connect_to_db 

def fetch_villager_data():
    url = "http://acnhapi.com/v1/villagers/" # this is just for villagers

    # request villager data
    response = requests.get(url)
    villagers = response.json()

    return villagers

# populate the villager table
def populate_database(villagers):
    connection = connect_to_db()
    cursor = connection.cursor()

    for villager in villagers:
        cursor.execute("""
            INSERT INTO villager (
                    id,
                    name,
                    gender,
                    personality,
                    species,
                    birthday,
                    catchphrase,
                    icon_uri,
                    image_uri
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, 
            villager['id'], villager['name']['name-USen'], villager['gender'], 
            villager['personality'], villager['species'], villager['birthday'],
            villager['catch-phrase'], villager['icon_uri'], villager['image_uri']
        )
    
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    villagers = fetch_villager_data()
    populate_database(villagers)
