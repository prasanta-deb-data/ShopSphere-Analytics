ALTER TABLE Customers
ADD DateOfBirth DATE NULL,
    IsPrimeMember BIT DEFAULT 0,
    LastLoginDate DATETIME NULL,
    CustomerStatus VARCHAR(20) DEFAULT 'Active';

ALTER TABLE Products
ADD SKU VARCHAR(30),
    WeightKg DECIMAL(5,2),
    LaunchDate DATE,
    IsActive BIT DEFAULT 1;

ALTER TABLE Orders
ADD OrderAmount DECIMAL(12,2),
    TaxAmount DECIMAL(10,2),
    ShippingCharge DECIMAL(10,2),
    FinalAmount DECIMAL(12,2);

ALTER TABLE OrderDetails
ADD CostPrice DECIMAL(10,2);

ALTER TABLE Inventory
ADD LastRestockedDate DATE;

ALTER TABLE CustomerSupport
ADD Priority VARCHAR(20),
    AssignedAgent VARCHAR(100);

ALTER TABLE WebsiteTraffic
ADD DeviceType VARCHAR(20),
    TrafficSource VARCHAR(30);