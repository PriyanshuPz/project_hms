import mysql.connector as sql


def create_database_and_tables():
    try:
        conn = sql.connect(host="localhost", user="root", passwd="password")
        cursor = conn.cursor()

        print("Creating database...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS hms_db")
        cursor.execute("USE hms_db")

        patient_table = """
        CREATE TABLE IF NOT EXISTS patient_details (
            p_name VARCHAR(100) NOT NULL,
            p_age INT NOT NULL,
            p_problems VARCHAR(200),
            p_phono BIGINT NOT NULL,
            PRIMARY KEY (p_phono)
        )
        """
        cursor.execute(patient_table)
        print("✓ Patient table created/verified")

        doctor_table = """
        CREATE TABLE IF NOT EXISTS doctor_details (
            d_name VARCHAR(100) NOT NULL,
            d_age INT NOT NULL,
            d_department VARCHAR(100),
            d_phono BIGINT NOT NULL,
            PRIMARY KEY (d_phono)
        )
        """
        cursor.execute(doctor_table)
        print("✓ Doctor table created/verified")

        worker_table = """
        CREATE TABLE IF NOT EXISTS worker_details (
            w_name VARCHAR(100) NOT NULL,
            w_age INT NOT NULL,
            w_workname VARCHAR(100),
            w_phono BIGINT NOT NULL,
            PRIMARY KEY (w_phono)
        )
        """
        cursor.execute(worker_table)
        print("✓ Worker table created/verified")

        print("\nInserting sample data...")

        sample_patients = [
            ("John Doe", 35, "Fever", 9876543210),
            ("Jane Smith", 28, "Headache", 9876543211),
            ("Bob Johnson", 45, "Back Pain", 9876543212),
        ]

        sample_doctors = [
            ("Dr. Kumar", 45, "Cardiology", 9123456789),
            ("Dr. Sharma", 38, "Neurology", 9123456790),
            ("Dr. Patel", 42, "Orthopedics", 9123456791),
        ]

        sample_workers = [
            ("Ram Singh", 30, "Cleaner", 9555666777),
            ("Maya Devi", 35, "Nurse", 9555666778),
            ("Ravi Kumar", 25, "Security", 9555666779),
        ]

        cursor.execute("SELECT COUNT(*) FROM patient_details")
        if cursor.fetchone()[0] == 0:  # type: ignore
            cursor.executemany(
                "INSERT INTO patient_details VALUES (%s, %s, %s, %s)", sample_patients
            )
            print("✓ Sample patient data inserted")

        cursor.execute("SELECT COUNT(*) FROM doctor_details")
        if cursor.fetchone()[0] == 0:  # type: ignore
            cursor.executemany(
                "INSERT INTO doctor_details VALUES (%s, %s, %s, %s)", sample_doctors
            )
            print("✓ Sample doctor data inserted")

        cursor.execute("SELECT COUNT(*) FROM worker_details")
        if cursor.fetchone()[0] == 0:  # type: ignore
            cursor.executemany(
                "INSERT INTO worker_details VALUES (%s, %s, %s, %s)", sample_workers
            )
            print("✓ Sample worker data inserted")

        conn.commit()
        print("\n✓ Database initialization completed successfully!")

        cursor.close()
        conn.close()

    except sql.Error as e:
        print(f"Error initializing database: {e}")
        return False

    return True


if __name__ == "__main__":
    print("=== HMS Database Initialization ===")
    create_database_and_tables()
