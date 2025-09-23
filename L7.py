import sqlite3


def crate_tables():
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)


def add_student(name, age, city):
    conn.execute(
        "INSERT INTO students (name, age, city) VALUE (?, ?, ?)",
        (name, age, city)
    )
    conn.commit()

def delete_students():
    conn.execute("DELETE FROM students WHERE id = ?", (2,))
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

crate_tables()

add_student("Aibek", 17, "Bishkek")

conn.close()

# есть ошибка посмотреть в чем проблема