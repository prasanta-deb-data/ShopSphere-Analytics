/*
=========================================================
 ShopSphere Analytics
 Enterprise SQL Server Database Schema
 Author  : Prasanta Kumar Deb
 Version : 1.0
=========================================================
*/

IF DB_ID('ShopSphereAnalytics') IS NULL
BEGIN
    CREATE DATABASE ShopSphereAnalytics;
END
GO

USE ShopSphereAnalytics;
GO

/*=========================================================
1. Categories
=========================================================*/

CREATE TABLE Categories
(
    CategoryID INT IDENTITY(1,1) PRIMARY KEY,

    CategoryName NVARCHAR(100) NOT NULL,

    Description NVARCHAR(500),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
2. SubCategories
=========================================================*/

CREATE TABLE SubCategories
(
    SubCategoryID INT IDENTITY(1,1) PRIMARY KEY,

    CategoryID INT NOT NULL,

    SubCategoryName NVARCHAR(100) NOT NULL,

    Description NVARCHAR(500),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
3. Brands
=========================================================*/

CREATE TABLE Brands
(
    BrandID INT IDENTITY(1,1) PRIMARY KEY,

    BrandName NVARCHAR(150) NOT NULL,

    Country NVARCHAR(100),

    Website NVARCHAR(255),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
4. Suppliers
=========================================================*/

CREATE TABLE Suppliers
(
    SupplierID INT IDENTITY(1,1) PRIMARY KEY,

    SupplierName NVARCHAR(150) NOT NULL,

    ContactPerson NVARCHAR(100),

    Email NVARCHAR(150),

    Phone NVARCHAR(20),

    CityID INT NOT NULL,

    GSTNumber NVARCHAR(20),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
5. Warehouses
=========================================================*/

CREATE TABLE Warehouses
(
    WarehouseID INT IDENTITY(1,1) PRIMARY KEY,

    WarehouseName NVARCHAR(150) NOT NULL,

    CityID INT NOT NULL,

    Capacity INT,

    ManagerName NVARCHAR(100),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
6. Customers
=========================================================*/

CREATE TABLE Customers
(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,

    FirstName NVARCHAR(100) NOT NULL,

    LastName NVARCHAR(100) NOT NULL,

    Gender NVARCHAR(20),

    DateOfBirth DATE,

    Email NVARCHAR(150),

    Phone NVARCHAR(20),

    RegistrationDate DATE NOT NULL,

    RegistrationSource NVARCHAR(30),

    CustomerSegment NVARCHAR(50),

    LoyaltyPoints INT NOT NULL DEFAULT 0,

    LastLoginDate DATETIME2(0),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
7. CustomerAddresses
=========================================================*/

CREATE TABLE CustomerAddresses
(
    AddressID INT IDENTITY(1,1) PRIMARY KEY,

    CustomerID INT NOT NULL,

    AddressType NVARCHAR(30) NOT NULL,

    AddressLine1 NVARCHAR(255) NOT NULL,

    AddressLine2 NVARCHAR(255),

    Landmark NVARCHAR(150),

    CityID INT NOT NULL,

    Country NVARCHAR(50) DEFAULT 'India',

    IsDefault BIT NOT NULL DEFAULT 0,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO
/*=========================================================
8. Products
=========================================================*/

CREATE TABLE Products
(
    ProductID INT IDENTITY(1,1) PRIMARY KEY,

    SKU NVARCHAR(50) NOT NULL,

    ProductName NVARCHAR(255) NOT NULL,

    ProductDescription NVARCHAR(1000),

    CategoryID INT NOT NULL,

    SubCategoryID INT NOT NULL,

    BrandID INT NOT NULL,

    SupplierID INT NOT NULL,

    MRP DECIMAL(18,2) NOT NULL,

    SellingPrice DECIMAL(18,2) NOT NULL,

    CostPrice DECIMAL(18,2) NOT NULL,

    Weight DECIMAL(10,2),

    Color NVARCHAR(50),

    Size NVARCHAR(30),

    LaunchDate DATE,

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
9. Inventory
=========================================================*/

CREATE TABLE Inventory
(
    InventoryID BIGINT IDENTITY(1,1) PRIMARY KEY,

    ProductID INT NOT NULL,

    WarehouseID INT NOT NULL,

    StockQuantity INT NOT NULL,

    ReservedQuantity INT NOT NULL DEFAULT 0,

    ReorderLevel INT NOT NULL,

    SafetyStock INT NOT NULL,

    LastRestocked DATE,

    LastStockUpdated DATETIME2(0),

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
10. Orders
=========================================================*/

CREATE TABLE Orders
(
    OrderID BIGINT IDENTITY(1000001,1) PRIMARY KEY,

    CustomerID INT NOT NULL,

    OrderDate DATETIME2(0) NOT NULL,

    OrderStatus NVARCHAR(30) NOT NULL,

    OrderChannel NVARCHAR(30) NOT NULL,

    TotalAmount DECIMAL(18,2) NOT NULL,

    DiscountAmount DECIMAL(18,2) NOT NULL DEFAULT 0,

    ShippingCharge DECIMAL(18,2) NOT NULL DEFAULT 0,

    TaxAmount DECIMAL(18,2) NOT NULL DEFAULT 0,

    FinalAmount DECIMAL(18,2) NOT NULL,

    PaymentStatus NVARCHAR(30) NOT NULL,

    ExpectedDeliveryDate DATE,

    DeliveredDate DATE,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
11. OrderItems
=========================================================*/

CREATE TABLE OrderItems
(
    OrderItemID BIGINT IDENTITY(1,1) PRIMARY KEY,

    OrderID BIGINT NOT NULL,

    ProductID INT NOT NULL,

    Quantity INT NOT NULL,

    UnitPrice DECIMAL(18,2) NOT NULL,

    Discount DECIMAL(18,2) NOT NULL DEFAULT 0,

    Tax DECIMAL(18,2) NOT NULL DEFAULT 0,

    TotalPrice DECIMAL(18,2) NOT NULL,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO
/*=========================================================
12. Payments
=========================================================*/

CREATE TABLE Payments
(
    PaymentID BIGINT IDENTITY(1,1) PRIMARY KEY,

    OrderID BIGINT NOT NULL,

    PaymentMethodID INT NOT NULL,

    PaymentDate DATETIME2(0) NOT NULL,

    AmountPaid DECIMAL(18,2) NOT NULL,

    PaymentStatus NVARCHAR(30) NOT NULL,

    TransactionReference NVARCHAR(150) NOT NULL,

    PaymentGateway NVARCHAR(100),

    GatewayResponseCode NVARCHAR(50),

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
13. Shipments
=========================================================*/

CREATE TABLE Shipments
(
    ShipmentID BIGINT IDENTITY(1,1) PRIMARY KEY,

    OrderID BIGINT NOT NULL,

    CourierID INT NOT NULL,

    WarehouseID INT NOT NULL,

    TrackingNumber NVARCHAR(100),

    ShippingDate DATETIME2(0),

    ExpectedDeliveryDate DATE,

    DeliveredDate DATETIME2(0),

    ShippingStatus NVARCHAR(30) NOT NULL,

    ShippingCost DECIMAL(18,2) NOT NULL DEFAULT 0,

    DeliveryAttempts TINYINT NOT NULL DEFAULT 0,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
14. Reviews
=========================================================*/

CREATE TABLE Reviews
(
    ReviewID BIGINT IDENTITY(1,1) PRIMARY KEY,

    ProductID INT NOT NULL,

    CustomerID INT NOT NULL,

    OrderItemID BIGINT NOT NULL,

    Rating TINYINT NOT NULL,

    ReviewTitle NVARCHAR(200),

    ReviewText NVARCHAR(MAX),

    ReviewDate DATETIME2(0) NOT NULL,

    HelpfulVotes INT NOT NULL DEFAULT 0,

    IsVerifiedPurchase BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
15. Returns
=========================================================*/

CREATE TABLE Returns
(
    ReturnID BIGINT IDENTITY(1,1) PRIMARY KEY,

    OrderItemID BIGINT NOT NULL,

    ReturnReasonID INT NOT NULL,

    ReturnDate DATETIME2(0) NOT NULL,

    RefundAmount DECIMAL(18,2) NOT NULL,

    ReturnStatus NVARCHAR(30) NOT NULL,

    RefundStatus NVARCHAR(30) NOT NULL,

    PickupDate DATE,

    RefundProcessedDate DATE,

    Remarks NVARCHAR(500),

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO
/*=========================================================
16. Coupons
=========================================================*/

CREATE TABLE Coupons
(
    CouponID INT IDENTITY(1,1) PRIMARY KEY,

    CouponCode NVARCHAR(50) NOT NULL,

    CouponDescription NVARCHAR(500),

    DiscountType NVARCHAR(20) NOT NULL,

    DiscountValue DECIMAL(18,2) NOT NULL,

    MinimumOrderValue DECIMAL(18,2) NOT NULL DEFAULT 0,

    MaximumDiscount DECIMAL(18,2),

    StartDate DATE NOT NULL,

    EndDate DATE NOT NULL,

    UsageLimit INT,

    UsedCount INT NOT NULL DEFAULT 0,

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
17. OrderCoupons
=========================================================*/

CREATE TABLE OrderCoupons
(
    OrderCouponID BIGINT IDENTITY(1,1) PRIMARY KEY,

    OrderID BIGINT NOT NULL,

    CouponID INT NOT NULL,

    DiscountAmount DECIMAL(18,2) NOT NULL,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
18. SupportTickets
=========================================================*/

CREATE TABLE SupportTickets
(
    TicketID BIGINT IDENTITY(1,1) PRIMARY KEY,

    CustomerID INT NOT NULL,

    OrderID BIGINT NULL,

    SupportIssueID INT NOT NULL,

    TicketStatus NVARCHAR(30) NOT NULL,

    Priority NVARCHAR(20) NOT NULL,

    AssignedAgent NVARCHAR(100),

    CreatedDate DATETIME2(0) NOT NULL,

    FirstResponseDate DATETIME2(0),

    ResolvedDate DATETIME2(0),

    ResolutionNotes NVARCHAR(MAX),

    CustomerSatisfactionRating TINYINT,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
19. WebsiteTraffic
=========================================================*/

CREATE TABLE WebsiteTraffic
(
    SessionID BIGINT IDENTITY(1,1) PRIMARY KEY,

    CustomerID INT NULL,

    SessionDate DATETIME2(0) NOT NULL,

    DeviceType NVARCHAR(30) NOT NULL,

    TrafficSource NVARCHAR(50) NOT NULL,

    Browser NVARCHAR(50),

    OperatingSystem NVARCHAR(50),

    CityID INT NOT NULL,

    IPAddress NVARCHAR(50),

    PagesVisited INT NOT NULL,

    SessionDurationSeconds INT NOT NULL,

    Bounce BIT NOT NULL DEFAULT 0,

    Converted BIT NOT NULL DEFAULT 0,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
20. PaymentMethods
=========================================================*/

CREATE TABLE PaymentMethods
(
    PaymentMethodID INT IDENTITY(1,1) PRIMARY KEY,

    PaymentMethodName NVARCHAR(50) NOT NULL,

    Description NVARCHAR(255),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
21. Couriers
=========================================================*/

CREATE TABLE Couriers
(
    CourierID INT IDENTITY(1,1) PRIMARY KEY,

    CourierName NVARCHAR(100) NOT NULL,

    ContactNumber NVARCHAR(20),

    Website NVARCHAR(255),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
22. ReturnReasons
=========================================================*/

CREATE TABLE ReturnReasons
(
    ReturnReasonID INT IDENTITY(1,1) PRIMARY KEY,

    ReturnReasonName NVARCHAR(100) NOT NULL,

    Description NVARCHAR(255),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
23. SupportIssues
=========================================================*/

CREATE TABLE SupportIssues
(
    SupportIssueID INT IDENTITY(1,1) PRIMARY KEY,

    SupportIssueName NVARCHAR(100) NOT NULL,

    Description NVARCHAR(255),

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
24.  FestivalCalendar
=========================================================*/

CREATE TABLE FestivalCalendar
(
    FestivalID INT IDENTITY(1,1) PRIMARY KEY,

    FestivalName NVARCHAR(100) NOT NULL,

    FestivalDate DATE NOT NULL,

    FestivalType NVARCHAR(50),

    IsNationalHoliday BIT NOT NULL DEFAULT 0,

    IsShoppingEvent BIT NOT NULL DEFAULT 0,

    Description NVARCHAR(500),

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO

/*=========================================================
25. Calendar
=========================================================*/

CREATE TABLE Calendar
(
    DateID INT PRIMARY KEY,              -- Example: 20250101

    CalendarDate DATE NOT NULL,

    DayNumber TINYINT NOT NULL,

    DayName NVARCHAR(20) NOT NULL,

    DayOfWeek TINYINT NOT NULL,

    WeekNumber TINYINT NOT NULL,

    MonthNumber TINYINT NOT NULL,

    MonthName NVARCHAR(20) NOT NULL,

    QuarterNumber TINYINT NOT NULL,

    QuarterName NVARCHAR(10) NOT NULL,

    YearNumber SMALLINT NOT NULL,

    FiscalYear NVARCHAR(20),

    FiscalQuarter NVARCHAR(10),

    IsWeekend BIT NOT NULL,

    IsHoliday BIT NOT NULL DEFAULT 0,

    FestivalID INT NULL,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE()
);
GO

/*=========================================================
26. States
=========================================================*/

CREATE TABLE States
(
    StateID INT PRIMARY KEY,

    StateCode NVARCHAR(5) NOT NULL,

    StateName NVARCHAR(100) NOT NULL,

    Region NVARCHAR(50) NOT NULL,

    StateType NVARCHAR(30) NOT NULL,

    IsActive BIT NOT NULL,

    CreatedAt DATETIME2(0) DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0)
);
GO

/*=========================================================
27. Cities
=========================================================*/

CREATE TABLE Cities
(
    CityID INT IDENTITY(1,1) PRIMARY KEY,

    StateID INT NOT NULL,

    CityName NVARCHAR(100) NOT NULL,

    Pincode NVARCHAR(10),

    Tier NVARCHAR(20),

    IsMetro BIT NOT NULL DEFAULT 0,

    IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2(0) NOT NULL DEFAULT GETDATE(),

    UpdatedAt DATETIME2(0) NULL
);
GO