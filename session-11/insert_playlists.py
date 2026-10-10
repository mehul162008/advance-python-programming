import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        autocommit=False
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS music_stream")
    cursor.execute("USE music_stream")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            song_count INT
        )
    """)

    playlists = [
        ("Chill Vibes", 15),
        ("Workout Hits", 20),
        ("Sad Songs", 8)
    ]

    cursor.executemany(
        "INSERT INTO playlists (name, song_count) VALUES (%s, %s)",
        playlists
    )

    connection.commit()

    print("Three playlists inserted successfully")

except pymysql.MySQLError as e:
    if connection:
        connection.rollback()

    print("Database error:", e)

finally:
    if connection:
        connection.close()