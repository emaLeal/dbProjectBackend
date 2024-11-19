CREATE TABLE Role (
    rol_id INT PRIMARY KEY AUTO INCREMENT,
    description VARCHAR(30) NOT NULL
);

CREATE TABLE User (
    document_id VARCHAR(15) PRIMARY KEY,
    name VARCHAR(130) NOT NULL,
    email VARCHAR(130) NOT NULL,
    status ENUM('pending', 'active', 'inactive') DEFAULT 'pending' NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES Role(rol_id)
);

CREATE TABLE Student (
    code VARCHAR(15) PRIMARY KEY,
    academic_register VARCHAR(15),
    user_id VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES User (document_id)
);

CREATE TABLE Request (
    request_id INT PRIMARY KEY AUTO INCREMENT,
    request_status ENUM('accepted', 'rejected', 'pending') DEFAULT 'pending' NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(document_id)
);

CREATE TABLE Institution (
    institution_id INT PRIMARY KEY AUTO INCREMENT,
    name VARCHAR(120),
    address VARCHAR(150)
);

CREATE TABLE Course (
    course_id INT PRIMARY KEY AUTO INCREMENT,
    course_name VARCHAR(150),
    institution_id INT,
    FOREIGN KEY (institution_id) REFERENCES Institution(institution_id)
);

CREATE TABLE Class (
    class_id INT PRIMARY KEY AUTO INCREMENT,
    class_name VARCHAR(120),
    room VARCHAR(10),
    schedule VARCHAR(200),
    date DATE,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Material (
    material_id INT PRIMARY KEY AUTO INCREMENT,
    file_name VARCHAR(100),
    file_path VARCHAR(100),
    file_type VARCHAR(15),
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES Class (class_id)
);

CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO INCREMENT,
    student_code VARCHAR(15),
    status ENUM ('attended', 'not attended'),
    hour TIME NOT NULL,
    location VARCHAR(60) NOT NULL,
    class_id INT,
    FOREIGN KEY (student_code) REFERENCES Student(code),
    FOREIGN KEY (class_id) REFERENCES Class(class_id)
);

CREATE TABLE User_class (
    id INT PRIMARY KEY AUTO INCREMENT,
    course_id INT,
    student_code VARCHAR(15),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (student_code) REFERENCES Student(code)
);  