CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(255),
    Username VARCHAR(50),
    Password VARCHAR(255),
    DateOfBirth DATE,
    Gender ENUM('Male', 'Female', 'Other')
);
