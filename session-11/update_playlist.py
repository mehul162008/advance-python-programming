import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="music_stream",
        autocommit=False
    )

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE playlists
        SET name = %s
        WHERE name = %s
    """, ("Chill Hits", "Chill Vibes"))

    connection.commit()

    if cursor.rowcount > 0:
        print("Playlist name updated successfully")
    else:
        print("Playlist not found")

except pymysql.MySQLError as e:
    if connection:
        connection.rollback()

    print("Database error:", e)

finally:
    if connection:
        connection.close()