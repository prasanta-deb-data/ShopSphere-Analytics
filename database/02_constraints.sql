/*
=========================================================
 ShopSphere Analytics
 Constraints
=========================================================
*/

USE ShopSphereAnalytics;
GO

/*
=======================================
1. Foreign Keys
=======================================
*/

ALTER TABLE SubCategories
ADD CONSTRAINT FK_SubCategories_Categories
FOREIGN KEY (CategoryID)
REFERENCES Categories(CategoryID);
GO

ALTER TABLE CustomerAddresses
ADD CONSTRAINT FK_CustomerAddresses_Customers
FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID);
GO

ALTER TABLE Products
ADD CONSTRAINT FK_Products_Categories
FOREIGN KEY(CategoryID)
REFERENCES Categories(CategoryID);

ALTER TABLE Products
ADD CONSTRAINT FK_Products_SubCategories
FOREIGN KEY(SubCategoryID)
REFERENCES SubCategories(SubCategoryID);

ALTER TABLE Products
ADD CONSTRAINT FK_Products_Brands
FOREIGN KEY(BrandID)
REFERENCES Brands(BrandID);

ALTER TABLE Products
ADD CONSTRAINT FK_Products_Suppliers
FOREIGN KEY(SupplierID)
REFERENCES Suppliers(SupplierID);
GO

ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Products
FOREIGN KEY(ProductID)
REFERENCES Products(ProductID);

ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Warehouses
FOREIGN KEY(WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO

ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Customers
FOREIGN KEY(CustomerID)
REFERENCES Customers(CustomerID);
GO

ALTER TABLE OrderItems
ADD CONSTRAINT FK_OrderItems_Orders
FOREIGN KEY(OrderID)
REFERENCES Orders(OrderID);

ALTER TABLE OrderItems
ADD CONSTRAINT FK_OrderItems_Products
FOREIGN KEY(ProductID)
REFERENCES Products(ProductID);
GO

ALTER TABLE Payments
ADD CONSTRAINT FK_Payments_Orders
FOREIGN KEY(OrderID)
REFERENCES Orders(OrderID);

ALTER TABLE Payments
ADD CONSTRAINT FK_Payments_PaymentMethods
FOREIGN KEY(PaymentMethodID)
REFERENCES PaymentMethods(PaymentMethodID);
GO

ALTER TABLE Shipments
ADD CONSTRAINT FK_Shipments_Orders
FOREIGN KEY(OrderID)
REFERENCES Orders(OrderID);

ALTER TABLE Shipments
ADD CONSTRAINT FK_Shipments_Couriers
FOREIGN KEY(CourierID)
REFERENCES Couriers(CourierID);

ALTER TABLE Shipments
ADD CONSTRAINT FK_Shipments_Warehouses
FOREIGN KEY(WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO

ALTER TABLE Reviews
ADD CONSTRAINT FK_Reviews_Customers
FOREIGN KEY(CustomerID)
REFERENCES Customers(CustomerID);

ALTER TABLE Reviews
ADD CONSTRAINT FK_Reviews_Products
FOREIGN KEY(ProductID)
REFERENCES Products(ProductID);

ALTER TABLE Reviews
ADD CONSTRAINT FK_Reviews_OrderItems
FOREIGN KEY(OrderItemID)
REFERENCES OrderItems(OrderItemID);
GO

ALTER TABLE Returns
ADD CONSTRAINT FK_Returns_OrderItems
FOREIGN KEY(OrderItemID)
REFERENCES OrderItems(OrderItemID);

ALTER TABLE Returns
ADD CONSTRAINT FK_Returns_ReturnReasons
FOREIGN KEY(ReturnReasonID)
REFERENCES ReturnReasons(ReturnReasonID);
GO

ALTER TABLE OrderCoupons
ADD CONSTRAINT FK_OrderCoupons_Orders
FOREIGN KEY(OrderID)
REFERENCES Orders(OrderID);

ALTER TABLE OrderCoupons
ADD CONSTRAINT FK_OrderCoupons_Coupons
FOREIGN KEY(CouponID)
REFERENCES Coupons(CouponID);
GO

ALTER TABLE SupportTickets
ADD CONSTRAINT FK_SupportTickets_Customers
FOREIGN KEY(CustomerID)
REFERENCES Customers(CustomerID);

ALTER TABLE SupportTickets
ADD CONSTRAINT FK_SupportTickets_Orders
FOREIGN KEY(OrderID)
REFERENCES Orders(OrderID);

ALTER TABLE SupportTickets
ADD CONSTRAINT FK_SupportTickets_SupportIssues
FOREIGN KEY(SupportIssueID)
REFERENCES SupportIssues(SupportIssueID);
GO

ALTER TABLE WebsiteTraffic
ADD CONSTRAINT FK_WebsiteTraffic_Customers
FOREIGN KEY(CustomerID)
REFERENCES Customers(CustomerID);
GO

ALTER TABLE Calendar
ADD CONSTRAINT FK_Calendar_FestivalCalendar
FOREIGN KEY(FestivalID)
REFERENCES FestivalCalendar(FestivalID);
GO

ALTER TABLE Cities
ADD CONSTRAINT FK_Cities_States
FOREIGN KEY(StateID)
REFERENCES States(StateID);
GO

ALTER TABLE CustomerAddresses
ADD CONSTRAINT FK_CustomerAddresses_Cities
FOREIGN KEY(CityID)
REFERENCES Cities(CityID);
GO

ALTER TABLE Suppliers
ADD CONSTRAINT FK_Suppliers_Cities
FOREIGN KEY(CityID)
REFERENCES Cities(CityID);
GO

ALTER TABLE Warehouses
ADD CONSTRAINT FK_Warehouses_Cities
FOREIGN KEY(CityID)
REFERENCES Cities(CityID);
GO

ALTER TABLE WebsiteTraffic
ADD CONSTRAINT FK_WebsiteTraffic_Cities
FOREIGN KEY(CityID)
REFERENCES Cities(CityID);
GO

/*
=======================================
2. Unique Constraint
=======================================
*/
ALTER TABLE Customers
ADD CONSTRAINT UQ_Customers_Email UNIQUE (Email);

ALTER TABLE Customers
ADD CONSTRAINT UQ_Customers_Phone UNIQUE (Phone);

ALTER TABLE Products
ADD CONSTRAINT UQ_Products_SKU UNIQUE (SKU);

ALTER TABLE Coupons
ADD CONSTRAINT UQ_Coupons_Code UNIQUE (CouponCode);

ALTER TABLE Payments
ADD CONSTRAINT UQ_Payments_TransactionReference
UNIQUE(TransactionReference);

ALTER TABLE Shipments
ADD CONSTRAINT UQ_Shipments_TrackingNumber
UNIQUE(TrackingNumber);
GO

/*
=======================================
3. CHECK Constraints
=======================================
*/
ALTER TABLE Reviews
ADD CONSTRAINT CK_Reviews_Rating
CHECK (Rating BETWEEN 1 AND 5);

ALTER TABLE Products
ADD CONSTRAINT CK_Product_Prices
CHECK
(
    SellingPrice <= MRP
    AND
    CostPrice <= SellingPrice
);

ALTER TABLE Inventory
ADD CONSTRAINT CK_Inventory_Stock
CHECK
(
    StockQuantity >= 0
);

ALTER TABLE Inventory
ADD CONSTRAINT CK_Inventory_Reorder
CHECK
(
    ReorderLevel >= 0
);

ALTER TABLE Inventory
ADD CONSTRAINT CK_Inventory_Safety
CHECK
(
    SafetyStock >= 0
);

ALTER TABLE OrderItems
ADD CONSTRAINT CK_OrderItems_Qty
CHECK
(
    Quantity > 0
);

ALTER TABLE WebsiteTraffic
ADD CONSTRAINT CK_WebsiteTraffic_Pages
CHECK
(
    PagesVisited > 0
);

ALTER TABLE WebsiteTraffic
ADD CONSTRAINT CK_WebsiteTraffic_Duration
CHECK
(
    SessionDurationSeconds >= 0
);

ALTER TABLE Coupons
ADD CONSTRAINT CK_Coupon_Discount
CHECK
(
    DiscountValue >= 0
);

ALTER TABLE Returns
ADD CONSTRAINT CK_Return_Refund
CHECK
(
    RefundAmount >= 0
);
GO

