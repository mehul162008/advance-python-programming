import pymysql


def delete_playlist(playlist_id):
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

        cursor.execute(
            "DELETE FROM playlists WHERE id = %s",
            (playlist_id,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Playlist deleted successfully")
        else:
            print("Playlist ID does not exist")

    except pymysql.MySQLError as e:
        if connection:
            connection.rollback()

        print("Database error:", e)

    finally:
        if connection:
            connection.close()


delete_playlist(1)