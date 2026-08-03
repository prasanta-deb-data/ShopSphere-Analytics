-- ECommerce_Analytics SQL Server Schema
CREATE DATABASE ECommerce_Analytics;
GO
USE ECommerce_Analytics;
GO

CREATE TABLE Customers(
    CustomerID INT IDENTITY PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Email NVARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    City NVARCHAR(50),
    State NVARCHAR(50),
    SignupDate DATE,
    CustomerSegment VARCHAR(30)
);

CREATE TABLE Categories(
    CategoryID INT IDENTITY PRIMARY KEY,
    CategoryName NVARCHAR(100) UNIQUE
);

CREATE TABLE Suppliers(
    SupplierID INT IDENTITY PRIMARY KEY,
    SupplierName NVARCHAR(100),
    Country NVARCHAR(50),
    Rating DECIMAL(3,2)
);

CREATE TABLE Products(
    ProductID INT IDENTITY PRIMARY KEY,
    ProductName NVARCHAR(150),
    CategoryID INT,
    SubCategory NVARCHAR(100),
    Brand NVARCHAR(100),
    CostPrice DECIMAL(10,2),
    SellingPrice DECIMAL(10,2),
    SupplierID INT,
    FOREIGN KEY(CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY(SupplierID) REFERENCES Suppliers(SupplierID)
);


CREATE TABLE Coupons(
    CouponID INT IDENTITY PRIMARY KEY,
    CouponCode NVARCHAR(30),
    DiscountPercent DECIMAL(5,2),
    StartDate DATE,
    EndDate DATE
);

CREATE TABLE Payments(
    PaymentID INT IDENTITY PRIMARY KEY,
    PaymentMethod VARCHAR(30),
    PaymentStatus VARCHAR(30),
    TransactionDate DATETIME
);

CREATE TABLE Shipping(
    ShippingID INT IDENTITY PRIMARY KEY,
    Courier NVARCHAR(50),
    ShippingCost DECIMAL(10,2),
    DeliveryDays INT,
    DeliveryStatus VARCHAR(30)
);

CREATE TABLE Orders(
    OrderID INT IDENTITY PRIMARY KEY,
    CustomerID INT,
    OrderDate DATETIME,
    DeliveryDate DATETIME NULL,
    OrderStatus VARCHAR(30),
    PaymentID INT,
    ShippingID INT,
    CouponID INT NULL,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY(PaymentID) REFERENCES Payments(PaymentID),
    FOREIGN KEY(ShippingID) REFERENCES Shipping(ShippingID),
    FOREIGN KEY(CouponID) REFERENCES Coupons(CouponID)
);



CREATE TABLE OrderDetails(
    OrderDetailID INT IDENTITY PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    Discount DECIMAL(5,2),
    TotalAmount DECIMAL(12,2),
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);



CREATE TABLE Returns(
    ReturnID INT IDENTITY PRIMARY KEY,
    OrderID INT,
    ReturnReason NVARCHAR(200),
    RefundAmount DECIMAL(12,2),
    ReturnDate DATE,
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID)
);

CREATE TABLE Reviews(
    ReviewID INT IDENTITY PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Rating INT CHECK(Rating BETWEEN 1 AND 5),
    ReviewDate DATE,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Inventory(
    ProductID INT PRIMARY KEY,
    Warehouse NVARCHAR(100),
    StockAvailable INT,
    ReorderLevel INT,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);



CREATE TABLE CustomerSupport(
    TicketID INT IDENTITY PRIMARY KEY,
    CustomerID INT,
    IssueType NVARCHAR(100),
    Status VARCHAR(30),
    ResolutionTime INT,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
);



CREATE TABLE WebsiteTraffic(
    TrafficDate DATE PRIMARY KEY,
    Visitors INT,
    Sessions INT,
    BounceRate DECIMAL(5,2),
    ConversionRate DECIMAL(5,2)
);

