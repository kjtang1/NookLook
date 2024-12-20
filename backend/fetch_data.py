import requests
import psycopg2
from db_config import connect_to_db 

def fetch_villager_data():
    url = "https://api.nookipedia.com/villagers" # this is just for villagers
    headers = {"X-API-KEY": 'cab01a40-0521-4845-8d65-bf0b2dde61d0'}
    params = {"game": 'NH'}

    # request villager data
    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        print("API call was a success!")
    else:
        print(response.status_code)
        print(response.text)
        exit(1)

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
                    birthday_month,
                    birthday_day,
                    catchphrase,
                    image_url
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, 
            (
                villager['id'], 
                villager['name'], 
                villager['gender'], 
                villager['personality'], 
                villager['species'], 
                villager['birthday_month'],
                villager['birthday_day'],
                villager['phrase'], 
                villager['image_url']
            )
        )
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Successfully populated the Villager table.")

if __name__ == "__main__":
    villagers = fetch_villager_data()
    populate_database(villagers)
