#****************************** Python project Youtube manager with sqlite3*****************************
import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id integer primary key,
            name text not null,
            time text not null
    )
''')

def list_videos():
    cursor.execute("Select * from videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("insert into videos (name,time) values(?, ?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("update videos set name=?,time=? where id=?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("delete from videos where id=?",(video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        
        choice =input("Enter your choice: ")
        if choice=="":
            return {}
        elif choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter video ID to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice=='4':
            video_id=input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid choice.")

    conn.close()
if __name__=="__main__":
    main()