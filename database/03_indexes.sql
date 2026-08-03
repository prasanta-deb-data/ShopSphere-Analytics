/*
=========================================================
ShopSphere Analytics
03_indexes.sql

Indexes for Performance Optimization
=========================================================
*/

USE ShopSphereAnalytics;
GO

CREATE UNIQUE NONCLUSTERED INDEX IX_Categories_CategoryName
ON Categories(CategoryName);
GO

CREATE NONCLUSTERED INDEX IX_SubCategories_CategoryID
ON SubCategories(CategoryID);

CREATE UNIQUE NONCLUSTERED INDEX IX_SubCategories_Name
ON SubCategories(CategoryID, SubCategoryName);
GO

CREATE UNIQUE NONCLUSTERED INDEX IX_Brands_Name
ON Brands(BrandName);
GO

CREATE NONCLUSTERED INDEX IX_Suppliers_CityID
ON Suppliers(CityID);

CREATE UNIQUE NONCLUSTERED INDEX IX_Suppliers_Email
ON Suppliers(Email);
GO

CREATE NONCLUSTERED INDEX IX_Warehouses_CityID
ON Warehouses(CityID);
GO

CREATE NONCLUSTERED INDEX IX_Customers_RegistrationDate
ON Customers(RegistrationDate);

CREATE NONCLUSTERED INDEX IX_Customers_LastLogin
ON Customers(LastLoginDate);

CREATE NONCLUSTERED INDEX IX_Customers_Segment
ON Customers(CustomerSegment);

CREATE NONCLUSTERED INDEX IX_Customers_IsActive
ON Customers(IsActive);
GO

CREATE NONCLUSTERED INDEX IX_CustomerAddresses_CustomerID
ON CustomerAddresses(CustomerID);

CREATE NONCLUSTERED INDEX IX_CustomerAddresses_CityID
ON CustomerAddresses(CityID);
GO

CREATE NONCLUSTERED INDEX IX_Cities_StateID
ON Cities(StateID);
GO

CREATE NONCLUSTERED INDEX IX_Products_Category
ON Products(CategoryID);

CREATE NONCLUSTERED INDEX IX_Products_SubCategory
ON Products(SubCategoryID);

CREATE NONCLUSTERED INDEX IX_Products_Brand
ON Products(BrandID);

CREATE NONCLUSTERED INDEX IX_Products_Supplier
ON Products(SupplierID);

CREATE NONCLUSTERED INDEX IX_Products_Price
ON Products(SellingPrice);

CREATE NONCLUSTERED INDEX IX_Products_Active
ON Products(IsActive);
GO

CREATE NONCLUSTERED INDEX IX_Inventory_Product
ON Inventory(ProductID);

CREATE NONCLUSTERED INDEX IX_Inventory_Warehouse
ON Inventory(WarehouseID);

CREATE NONCLUSTERED INDEX IX_Inventory_Stock
ON Inventory(StockQuantity);
GO

CREATE NONCLUSTERED INDEX IX_Orders_Customer
ON Orders(CustomerID);

CREATE NONCLUSTERED INDEX IX_Orders_OrderDate
ON Orders(OrderDate);

CREATE NONCLUSTERED INDEX IX_Orders_Status
ON Orders(OrderStatus);

CREATE NONCLUSTERED INDEX IX_Orders_PaymentStatus
ON Orders(PaymentStatus);

CREATE NONCLUSTERED INDEX IX_Orders_Channel
ON Orders(OrderChannel);

CREATE NONCLUSTERED INDEX IX_Orders_FinalAmount
ON Orders(FinalAmount);
GO

CREATE NONCLUSTERED INDEX IX_OrderItems_Order
ON OrderItems(OrderID);

CREATE NONCLUSTERED INDEX IX_OrderItems_Product
ON OrderItems(ProductID);
GO

CREATE NONCLUSTERED INDEX IX_Payments_Order
ON Payments(OrderID);

CREATE NONCLUSTERED INDEX IX_Payments_Method
ON Payments(PaymentMethodID);

CREATE NONCLUSTERED INDEX IX_Payments_Date
ON Payments(PaymentDate);

CREATE NONCLUSTERED INDEX IX_Payments_Status
ON Payments(PaymentStatus);
GO

CREATE NONCLUSTERED INDEX IX_Shipments_Order
ON Shipments(OrderID);

CREATE NONCLUSTERED INDEX IX_Shipments_Courier
ON Shipments(CourierID);

CREATE NONCLUSTERED INDEX IX_Shipments_Status
ON Shipments(ShippingStatus);

CREATE NONCLUSTERED INDEX IX_Shipments_Delivery
ON Shipments(DeliveredDate);
GO

CREATE NONCLUSTERED INDEX IX_Reviews_Product
ON Reviews(ProductID);

CREATE NONCLUSTERED INDEX IX_Reviews_Customer
ON Reviews(CustomerID);

CREATE NONCLUSTERED INDEX IX_Reviews_Rating
ON Reviews(Rating);
GO

CREATE NONCLUSTERED INDEX IX_Returns_OrderItem
ON Returns(OrderItemID);

CREATE NONCLUSTERED INDEX IX_Returns_Status
ON Returns(ReturnStatus);

CREATE NONCLUSTERED INDEX IX_Returns_Date
ON Returns(ReturnDate);
GO

CREATE NONCLUSTERED INDEX IX_Coupons_Active
ON Coupons(IsActive);

CREATE NONCLUSTERED INDEX IX_Coupons_StartDate
ON Coupons(StartDate);

CREATE NONCLUSTERED INDEX IX_Coupons_EndDate
ON Coupons(EndDate);
GO

CREATE NONCLUSTERED INDEX IX_SupportTickets_Customer
ON SupportTickets(CustomerID);

CREATE NONCLUSTERED INDEX IX_SupportTickets_Order
ON SupportTickets(OrderID);

CREATE NONCLUSTERED INDEX IX_SupportTickets_Status
ON SupportTickets(TicketStatus);

CREATE NONCLUSTERED INDEX IX_SupportTickets_Priority
ON SupportTickets(Priority);
GO

CREATE NONCLUSTERED INDEX IX_WebsiteTraffic_Customer
ON WebsiteTraffic(CustomerID);

CREATE NONCLUSTERED INDEX IX_WebsiteTraffic_Date
ON WebsiteTraffic(SessionDate);

CREATE NONCLUSTERED INDEX IX_WebsiteTraffic_Source
ON WebsiteTraffic(TrafficSource);

CREATE NONCLUSTERED INDEX IX_WebsiteTraffic_Device
ON WebsiteTraffic(DeviceType);

CREATE NONCLUSTERED INDEX IX_WebsiteTraffic_City
ON WebsiteTraffic(CityID);

CREATE NONCLUSTERED INDEX IX_WebsiteTraffic_Converted
ON WebsiteTraffic(Converted);
GO

CREATE NONCLUSTERED INDEX IX_Calendar_Date
ON Calendar(CalendarDate);

CREATE NONCLUSTERED INDEX IX_Calendar_Year
ON Calendar(YearNumber);

CREATE NONCLUSTERED INDEX IX_Calendar_Festival
ON Calendar(FestivalID);
GO

