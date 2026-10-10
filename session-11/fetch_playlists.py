import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="music_stream"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, song_count
        FROM playlists
        WHERE song_count > 10
    """)

    playlists = cursor.fetchall()

    for playlist in playlists:
        print("Playlist Name:", playlist[0])
        print("Song Count:", playlist[1])

except pymysql.MySQLError as e:
    print("Database error:", e)

finally:
    if connection:
        connection.close()